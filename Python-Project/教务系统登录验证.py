import requests
import time
import rsa
import base64
import binascii
from bs4 import BeautifulSoup  # 新增：用于解析 HTML 提取 Token

class ZFSoftLoginSimulator:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        # 伪造浏览器 UA，保持与真实浏览器一致
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

    def get_timestamp(self):
        return str(int(time.time() * 1000))

    def encrypt_password(self, password, modulus_b64, exponent_b64):
        """还原前端 rsa.js 的加密逻辑"""
        modulus = int(binascii.hexlify(base64.b64decode(modulus_b64)), 16)
        exponent = int(binascii.hexlify(base64.b64decode(exponent_b64)), 16)
        
        pub_key = rsa.PublicKey(modulus, exponent)
        crypto = rsa.encrypt(password.encode('utf-8'), pub_key)
        encrypted_pwd_b64 = base64.b64encode(crypto).decode('utf-8')
        return encrypted_pwd_b64

    def standard_login(self, username, password, captcha_code=""):
        """常规账号密码登录完整流程"""
        
        login_page_url = f"{self.base_url}/xtgl/login_slogin.html"

        # ========================================================
        # Step 0: 访问登录页，初始化 Session (获取 Cookie) 并提取 Token
        # ========================================================
        print("[*] 0. 访问登录页面，提取动态 Token...")
        page_res = self.session.get(login_page_url, headers=self.headers)
        
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(page_res.text, 'html.parser')
        
        # 自动提取隐藏域中的 csrfToken 和 csrfTokenLogout
        # 这里使用 find 方法并通过 id 查找，如果没有找到则默认为空字符串
        csrf_token_input = soup.find('input', id='csrfToken')
        csrf_token_logout_input = soup.find('input', id='csrfTokenLogout')
        
        csrf_token = csrf_token_input.get('value') if csrf_token_input else ""
        csrf_token_logout = csrf_token_logout_input.get('value') if csrf_token_logout_input else ""
        
        print(f"    提取到 csrfToken: {csrf_token}")
        print(f"    提取到 csrfTokenLogout: {csrf_token_logout}")

        # ========================================================
        # Step 1: 获取 RSA 公钥
        # ========================================================
        print("[*] 1. 获取 RSA 公钥...")
        pk_url = f"{self.base_url}/xtgl/login_getPublicKey.html?time={self.get_timestamp()}"
        pk_res = self.session.get(pk_url, headers=self.headers).json()
        modulus = pk_res.get("modulus")
        exponent = pk_res.get("exponent")
        print(f"    获取成功: modulus={modulus[:10]}...")

        # Step 2: 预检账号状态 (纯前端逻辑模拟)
        print("[*] 2. 预检账号状态 (login_cxDlxgxx)...")
        check_url = f"{self.base_url}/xtgl/login_cxDlxgxx.html"
        check_res = self.session.post(check_url, data={"yhm": username}, headers=self.headers)
        if check_res.text == "0":
            print("[-] 用户不存在")
            return False
        
        # Step 3: 注销旧会话 (顶号逻辑) - 使用动态获取的 Token
        print("[*] 3. 清理旧登录状态...")
        logout_url = f"{self.base_url}/xtgl/login_logoutAccount.html"
        self.session.post(logout_url, data={"csrfTokenLogout": csrf_token_logout}, headers=self.headers)

        # Step 4: 密码加密
        print("[*] 4. 执行 RSA 密码加密...")
        encrypted_password = self.encrypt_password(password, modulus, exponent)
        
        # Step 5: 构建表单并最终提交登录
        print("[*] 5. 提交登录表单...")
        login_submit_url = f"{self.base_url}/xtgl/login_slogin.html?time={self.get_timestamp()}"
        
        # 构造 POST 负载，填入自动提取的 CSRF Token
        payload = {
            "yhm": username,
            "mm": encrypted_password,
            "hidMm": encrypted_password,
            "yzm": captcha_code,
            "language": "zh_CN",
            "mmsfjm": "1",                 
            "csrfToken": csrf_token,     # 动态注入抓取到的 CSRF Token
        }
        
        # 提交登录表单
        login_res = self.session.post(login_submit_url, data=payload, headers=self.headers)
        
        # 添加调试信息
        print(f"响应状态码: {login_res.status_code}")
        print(f"响应内容长度: {len(login_res.text)}")
        print(f"是否包含'首页': {'首页' in login_res.text}")
        print(f"是否包含'退出': {'退出' in login_res.text}")
        print(f"是否有重定向历史: {bool(login_res.history)}")

        # 判断是否登录成功 (正方教务系统成功后通常会发生 302 跳转或返回首页 HTML)
        if "首页" in login_res.text or "退出" in login_res.text or login_res.history: 
            print("[+] 账号密码登录成功！")
            return True
        else:
            print("[-] 登录失败，可能密码错误或需要图形验证码。")
            return False

# ================= 使用示例 =================
if __name__ == "__main__":
    # 替换为实际的教务系统域名，例如: http://jwgl.xxxx.edu.cn
    target_host = "https://jxgl.ahiib.edu.cn"
    simulator = ZFSoftLoginSimulator(target_host)
    
    # 执行自动登录
    simulator.standard_login("2304170638", "")