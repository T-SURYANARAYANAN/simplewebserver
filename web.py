from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1>Laptop Con figuration</h1>
<table border="2px">
    <tr>
        <th>System configuration</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Processor</td>
        <td>12th Gen Intel(R) Core(TM) i5-1235U   1.30 GHz</td>
    </tr>
    <tr>
        <td>Primary memory</td>
        <td>16.0 GB (15.7 GB usable)</td>
    </tr>
    <tr>
        <td>Secondary memory</td>
        <td>512GB</td>
    </tr>
    <tr>
        <td>Operating system</td>
        <td>Windows 11 Home Single Language</td>
    </tr>
    <tr>
        <td>Graphics card</td>
        <td>INTEL IRIS</td>
    </tr>
</table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()