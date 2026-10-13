import gmpy2
from gmpy2 import mpz, mpfr, get_context, sqrt
import multiprocessing
import psutil
import time
import sys
import threading

# --- Chudnovsky 参数 ---
C = 640320
C3_24 = C ** 3 // 24
L = 13591409
X = 545140134

# 全局变量用于监控线程
current_cpu_peak = 0
keep_monitoring = False


def cpu_monitor_thread():
    """后台高频监控线程，捕捉计算期间的最高 CPU 占用"""
    global current_cpu_peak, keep_monitoring
    while keep_monitoring:
        # 每 0.1 秒采样一次，取测试期间的平均值或最高值
        load = psutil.cpu_percent(interval=0.1)
        if load > current_cpu_peak:
            current_cpu_peak = load


def chudnovsky_worker(a, b):
    """并行计算单元"""
    if b - a == 1:
        if a == 0:
            P = Q = mpz(1)
        else:
            P = mpz((6 * a - 5) * (2 * a - 1) * (6 * a - 1))
        Q = mpz(a ** 3 * C3_24)
        T = P * (L + X * a)
        if a % 2 == 1: T = -T
        return P, Q, T
    else:
        m = (a + b) // 2
        P1, Q1, T1 = chudnovsky_worker(a, m)
        P2, Q2, T2 = chudnovsky_worker(m, b)
        return P1 * P2, Q1 * Q2, T1 * Q2 + P1 * T2


def calculate_pi_parallel(digits, num_cores):
    """核心计算函数"""
    terms = int(digits / 14.181647) + 1
    precision_bits = int(digits * 3.322) + 100
    get_context().precision = precision_bits

    # 增加任务分片数量，确保 16 核被喂饱
    chunk_count = num_cores * 2
    chunk_size = terms // chunk_count
    ranges = []
    for i in range(chunk_count):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != chunk_count - 1 else terms
        if start < end:
            ranges.append((start, end))

    with multiprocessing.Pool(processes=num_cores) as pool:
        results = pool.starmap(chudnovsky_worker, ranges)

    # 主进程归并（这部分是单核，位数极高时会成为瓶颈）
    cur_P, cur_Q, cur_T = results[0]
    for next_P, next_Q, next_T in results[1:]:
        cur_T = cur_T * next_Q + cur_P * next_T
        cur_P = cur_P * next_P
        cur_Q = cur_Q * next_Q

    sqrt_M = sqrt(mpz(10005))
    pi = (mpfr(426880) * sqrt_M * cur_Q) / (mpz(L) * cur_Q + cur_T)
    return pi


def run_stress_test():
    global current_cpu_peak, keep_monitoring

    num_cores = multiprocessing.cpu_count()
    print("=" * 60)
    print(f"极限多核性能压测 (内核数: {num_cores} | 后端: gmpy2)")
    print("目标: 持续增加位数直到全核平均占用率 >= 98%")
    print("=" * 60)

    # 允许处理超长整数
    sys.set_int_max_str_digits(0)

    digits = 1000000  # 从100万位开始
    max_digits = 0

    try:
        while True:
            current_cpu_peak = 0
            keep_monitoring = True

            # 启动监控线程
            monitor = threading.Thread(target=cpu_monitor_thread)
            monitor.start()

            start_time = time.time()
            # 执行计算
            calculate_pi_parallel(digits, num_cores)
            duration = time.time() - start_time

            # 停止监控
            keep_monitoring = False
            monitor.join()

            print(
                f"规模: {digits / 1e6:>6.1f} 百万位 | 耗时: {duration:>7.2f}s | 捕捉峰值负载: {current_cpu_peak:>5.1f}%")

            if current_cpu_peak >= 98.0:
                print(f"\n[目标达成] CPU 占用率触顶: {current_cpu_peak}%")
                max_digits = digits
                break

            max_digits = digits
            # 阶梯式增加规模
            if digits < 10000000:
                digits += 2000000  # 1000万位以下每次加200万
            else:
                digits = int(digits * 1.4)  # 1000万位以上按 1.4 倍指数增长

    except KeyboardInterrupt:
        print("\n[手动停止] 捕捉到用户中断。")
    except MemoryError:
        print("\n[内存溢出] 物理内存已耗尽！")

    print("\n" + "=" * 60)
    print(f"最终压测报告:")
    print(f"1. 达到 98% 负载时的计算规模: {max_digits} 位")
    print(f"2. 最终系统记录负载: {current_cpu_peak}%")
    print(f"3. 提示: 如果由于内存限制无法达到 98%，请检查任务管理器的内存分页文件。")
    print("=" * 60)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    run_stress_test()