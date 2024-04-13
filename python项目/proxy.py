# import json
# import logging
# import socket
# import sys
# import threading
# import time
# from urllib import request

# #import colorfulog

# XUN_PROXY_API_URL = "http://192.168.0.101:5010/all"
# proxyList = []


# def set_global_proxy_list(pl):
#     global proxyList
#     if not pl:
#         return
#     proxyList = []
#     for p in pl:
#         proxy = f"{p['ip']}:{p['port']}"
#         logging.info(f"add proxy {proxy}")
#         proxyList.append(proxy)
#     while len(proxyList) > 75:
#         logging.info(f"remove proxy {proxyList.pop()}")


# def update_upstream_proxy():
#     try:
#         with request.urlopen(XUN_PROXY_API_URL) as response:
#             body = response.read()
#             map_result = json.loads(body)
#             ERRORCODE = map_result.get("ERRORCODE")
#             logging.info(f"fetchUpstream errorcode {ERRORCODE}")
#             if ERRORCODE == "0":
#                 result = map_result.get("RESULT")
#                 if isinstance(result, list):
#                     logging.info(f"add proxyList : {result}")
#                     set_global_proxy_list(result)
#                 else:
#                     logging.warn(f"convert field {result}")
#     except Exception as e:
#         logging.warn(f"fetchUpstreamProxy {e}")


# def forward(conn, remote_addr):
#     try:
#         client = socket.create_connection(remote_addr)
#         logging.info(f"Forwarding from {conn.getsockname()} to {client.getpeername()}")
#         threading.Thread(target=_forward_data, args=(conn, client)).start()
#         threading.Thread(target=_forward_data, args=(client, conn)).start()
#     except Exception as e:
#         logging.error(f"Dial failed: {e}")
#         conn.close()


# def _forward_data(source, destination):
#     try:
#         while True:
#             data = source.recv(4096)
#             if not data:
#                 break
#             destination.sendall(data)
#     except Exception as e:
#         logging.error(f"Data forwarding error: {e}")
#     finally:
#         source.close()
#         destination.close()


# def update_proxy_list():
#     logging.info("启动代理更新协程")
#     while True:
#         update_upstream_proxy()
#         time.sleep(20)


# def main():
#     # 启动代理更新线程
#     threading.Thread(target=update_proxy_list).start()

#     listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         listener.bind(("", 12001))
#         listener.listen(5)
#         logging.info("Listening for connections on port 12001...")
#         while True:
#             conn, addr = listener.accept()
#             logging.info(f"Accepted connection from {addr}")
#             px = proxyList.pop(0) if proxyList else None
#             if px:
#                 px_host, px_port = px.split(":")
#                 threading.Thread(target=forward, args=(conn, (px_host, int(px_port)))).start()
#             else:
#                 # 随便设置个无效的代理
#                 threading.Thread(target=forward, args=(conn, ("127.0.0.1", 60001))).start()
#     except Exception as e:
#         logging.error(f"Error: {e}")
#         sys.exit(1)
#     finally:
#         listener.close()


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
#     main()
# import requests
# import http.server
# import socketserver

# def get_ip_list():
#     ip_list = []
#     try:
#         response = requests.get('http://192.168.0.101:5010/all')
#         data = response.json()
#         if isinstance(data, list):
#             for item in data:
#                 if 'proxy' in item:
#                     ip_list.append(item['proxy'])
#                 else:
#                     print("无数据！")
#         else:
#             print("Response JSON data is not a list.")
#     except Exception as e:
#         print("An error occurred:", str(e))
#     return ip_list

# def httpweb():
#     # HTML 代码
#     html_content = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Simple Webpage</title>
#     </head>
#     <body>
#     </body>
#     </html>
#     """

#     # 定义一个简单的 HTTP 请求处理器，返回内置的 HTML 代码
#     class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
#         def end_headers(self):
#             self.send_header('Content-type', 'text/html')
#             http.server.SimpleHTTPRequestHandler.end_headers(self)

#         def do_GET(self):
#             self.send_response(200)
#             self.end_headers()
#             self.wfile.write(html_content.encode('utf-8'))

#     # 设置服务器的端口
#     PORT = 8000

#     # 创建一个简单的 HTTP 服务器，使用上面定义的请求处理器
#     with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
#         print("Server started at port", PORT)
#         # 监听请求，直到手动终止服务器
#         httpd.serve_forever()


# # 测试函数
# if __name__ == "__main__":
#     ip_list = get_ip_list()
#     httpweb(ip_list)
#     #for ip in ip_list:
#     #    print(ip)
#     #print("IP List:", ip_list)
import requests
import http.server
import socketserver
import json

def get_ip_list():
    ip_list = []
    try:
        response = requests.get('http://192.168.0.101:5010/all')
        data = response.json()
        if isinstance(data, list):
            for item in data:
                if 'proxy' in item:
                    ip_list.append(item['proxy'])
                else:
                    print("无数据！")
        else:
            print("Response JSON data is not a list.")
    except Exception as e:
        print("An error occurred:", str(e))
    return ip_list[0]

# 定义一个简单的 HTTP 请求处理器，返回内置的 HTML 代码
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-type', 'application/json')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        ip_list = get_ip_list()
        ip_json = json.dumps(ip_list)
        self.wfile.write(ip_json.encode('utf-8'))

# 设置服务器的端口
PORT = 8000

# 创建一个简单的 HTTP 服务器，使用上面定义的请求处理器
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("Server started at port", PORT)
    # 监听请求，直到手动终止服务器
    httpd.serve_forever()
