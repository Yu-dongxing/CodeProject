from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# 定义处理请求的类
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Python Web Server</title>
            </head>
            <body>
                <h1>Hello, welcome to the Python Web Server!</h1>
                <form action="/submit" method="post">
                    <label for="input_text">Enter some text:</label><br>
                    <input type="text" id="input_text" name="input_text"><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
            """

            self.wfile.write(html_content.encode())
        elif self.path == "/submit":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            length = int(self.headers['Content-length'])
            post_data = self.rfile.read(length).decode('utf-8')
            input_text = urllib.parse.parse_qs(post_data)['input_text'][0]

            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Python Web Server - Result</title>
            </head>
            <body>
                <h1>Your text was: {input_text}</h1>
            </body>
            </html>
            """

            self.wfile.write(html_content.encode())

# 启动服务器
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8215):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

# 在端口8000启动Web服务
if __name__ == '__main__':
    run()