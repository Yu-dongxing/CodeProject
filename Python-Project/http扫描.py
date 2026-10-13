import asyncio
import aiohttp
import argparse
import sys
from datetime import datetime
from typing import Set, List, Tuple

class HTTPPortScanner:
    def __init__(self, target_ip: str, max_concurrent: int = 500, timeout: float = 3.0):
        self.target_ip = target_ip
        self.max_concurrent = max_concurrent
        self.timeout = timeout
        self.open_ports: Set[int] = set()
        self.total_ports = 65535
        self.scanned_count = 0
        self.lock = asyncio.Lock()
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.start_time = None
        
    async def check_port(self, session: aiohttp.ClientSession, port: int) -> Tuple[int, bool, str]:
        """检查单个端口是否开放并返回HTTP响应信息"""
        async with self.semaphore:
            is_open = False
            banner = ""
            try:
                # 依次尝试 HTTP 和 HTTPS
                urls = [
                    f"http://{self.target_ip}:{port}",
                    f"https://{self.target_ip}:{port}"
                ]
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                for url in urls:
                    try:
                        # 尝试 HEAD 请求 (速度更快)
                        async with session.head(url, headers=headers, allow_redirects=True) as resp:
                            is_open = True
                            banner = f"{resp.status} {resp.reason} ({url[:5].upper()})"
                            break
                    except (aiohttp.ClientError, asyncio.TimeoutError):
                        try:
                            # 如果 HEAD 失败，某些服务器可能只允许 GET 请求
                            async with session.get(url, headers=headers) as resp:
                                is_open = True
                                banner = f"{resp.status} {resp.reason} ({url[:5].upper()})"
                                break
                        except:
                            continue
            except Exception:
                pass
            finally:
                # 更新进度和统计信息
                async with self.lock:
                    self.scanned_count += 1
                    if is_open:
                        self.open_ports.add(port)
                    
                    # 每 500 个端口或扫描结束时刷新一次进度条，避免频繁 IO 导致卡顿
                    if self.scanned_count % 500 == 0 or self.scanned_count == self.total_ports:
                        progress = (self.scanned_count / self.total_ports) * 100
                        elapsed = (datetime.now() - self.start_time).total_seconds()
                        speed = self.scanned_count / elapsed if elapsed > 0 else 0
                        print(f"\r[*] 进度: {progress:.1f}% ({self.scanned_count}/{self.total_ports}) "
                              f"- 发现HTTP/S服务: {len(self.open_ports)} - 速度: {speed:.0f} 端口/秒", end='', flush=True)
            
            return port, is_open, banner
    
    async def scan(self) -> List[Tuple[int, str]]:
        """执行全端口扫描"""
        self.start_time = datetime.now()
        print(f"[*] 开始扫描目标: {self.target_ip}")
        print(f"[*] 端口范围: 1-{self.total_ports}")
        print(f"[*] 并发连接数: {self.max_concurrent}")
        print(f"[*] 超时时间: {self.timeout}秒")
        print("[*] 扫描中... (按 Ctrl+C 停止)\n")
        
        timeout_obj = aiohttp.ClientTimeout(total=self.timeout)
        # ssl=False 忽略证书校验，limit 限制底层连接池大小
        connector = aiohttp.TCPConnector(ssl=False, limit=self.max_concurrent)
        
        # 核心修复：整个应用复用同一个 ClientSession
        async with aiohttp.ClientSession(timeout=timeout_obj, connector=connector) as session:
            tasks = [asyncio.create_task(self.check_port(session, port)) for port in range(1, self.total_ports + 1)]
            
            try:
                results = await asyncio.gather(*tasks, return_exceptions=True)
            except asyncio.CancelledError:
                print("\n\n[!] 扫描被中止，正在清理资源...")
                return []
        
        # 汇总结果
        open_ports_info = []
        for result in results:
            if isinstance(result, Exception):
                continue
            port, is_open, banner = result
            if is_open:
                open_ports_info.append((port, banner))
        
        return sorted(open_ports_info)
    
    def save_results(self, open_ports_info: List[Tuple[int, str]], filename: str = None):
        """保存扫描结果"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scan_{self.target_ip.replace('.', '_')}_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"扫描目标: {self.target_ip}\n")
            f.write(f"扫描时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"发现HTTP/S服务数量: {len(open_ports_info)}\n")
            f.write("=" * 50 + "\n")
            for port, banner in open_ports_info:
                f.write(f"Port {port}: {banner}\n")
        
        return filename


async def async_main(args):
    scanner = HTTPPortScanner(args.target, args.concurrent, args.timeout)
    open_ports = await scanner.scan()
    
    # 打印最终结果
    if len(scanner.open_ports) > 0 or len(open_ports) > 0:
        print(f"\n\n[+] 扫描完成!")
        print(f"[+] 发现 HTTP/S 服务数量: {len(open_ports)}")
        print("\n[*] 开放端口列表:")
        for port, banner in open_ports:
            print(f"    {port}/tcp - {banner}")
        
        filename = scanner.save_results(open_ports, args.output)
        print(f"\n[+] 结果已保存至: {filename}")
    else:
        print("\n\n[-] 扫描完成，未发现任何 HTTP/S 服务")


def main():
    parser = argparse.ArgumentParser(description='高性能 HTTP/HTTPS 端口扫描器 (1-65535)')
    parser.add_argument('target', help='目标IP地址 (例如: 192.168.1.1)')
    parser.add_argument('-c', '--concurrent', type=int, default=500, 
                        help='最大并发连接数 (默认: 500)')
    parser.add_argument('-t', '--timeout', type=float, default=3.0,
                        help='连接超时时间 (默认: 3.0秒)')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='输出文件名 (可选)')
    
    args = parser.parse_args()
    
    # 验证IP地址格式
    import ipaddress
    try:
        ipaddress.ip_address(args.target)
    except ValueError:
        print("[-] 错误: 无效的IP地址格式")
        sys.exit(1)
    
    # 防止并发过高导致系统文件描述符(ulimit)耗尽
    if args.concurrent > 1000:
        print("[!] 警告: 并发数过高可能导致报错，已自动调整为 1000")
        args.concurrent = 1000

    # 兼容 Windows 系统的异步事件循环策略
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # 优雅捕获 Ctrl+C，避免打印一堆难以阅读的 Traceback
    try:
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        print("\n\n[!] 用户手动中止了程序。")
        sys.exit(0)


if __name__ == "__main__":
    main()