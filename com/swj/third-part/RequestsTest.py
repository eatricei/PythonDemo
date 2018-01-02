# -*- coding: utf-8 -*-

# 处理url更方便 自动检测编码
import requests
# r = requests.get('https://www.douban.com/')
# if __name__ == '__main__':
#     print(r.status_code)
#     print(r.text)
# 带参数的url 传入dict参数
# r = requests.get('https://www.douban.com/', params={'q': 'Python', 'cat': '1001'})
# print(r.url)
# print(r.encoding)
# 无论响应文本还是二进制内容 都可以用content属性获得bytes对象
# print(r.content)
# 对于特定的响应类型可以直接获取
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())
# 需要传入一个Http header时 我们传入一个dict作为headers参数
#r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
#print(r.text)
# 发送post请求只要把get改为post 传入data作为post的参数就行了 默认使用application/x-www-form-urlencoded 对post数据进行编码
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#print(r.text)
# 传递JSON 可以直接传入json参数 内部自动序列化为json
url = 'https://www.douban.com/'
# 上传文件需要更复杂的编码格式 简化为了files参数
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

r.headers
r.headers['Content-Type']

r.cookies['ts']
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)
r = requests.get(url, timeout=2.5)  # 2.5秒后超时
