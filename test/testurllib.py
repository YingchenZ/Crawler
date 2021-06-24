from nturl2path import url2pathname
import urllib.request

# 打开网页
# response = urllib.request.urlopen("http://www.baidu.com")

# print(response.read().decode('utf-8'))

# post请求
import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://www.httpbin.org/post", data = data)

# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://www.httpbin.org/get", timeout=0.01)
#     print(response.read().decode('utf-8'))
# except Exception as e:
#     print("Timeout")


# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Server"))

# 伪装成浏览器
# url = "http://www.httpbin.org/post"
headers = {
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-60c36625-7238d5c9449c90a7526effe2"
}
# data = bytes(urllib.parse.urlencode({'name':'eric'}), encoding="utf-8")
# req = urllib.request.Request(url = url, data = data, headers= headers)
# try:
#     response = urllib.request.urlopen(req)
#     print(response.read().decode('utf-8'))
# except Exception as e:
#     print("Timeout")


url = "http://www.douban.com"
req = urllib.request.Request(url = url, headers= headers)
try:
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))
except Exception as e:
    print("Timeout")
