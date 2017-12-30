# -*- coding: utf-8 -*-
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('<%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')
# 特殊字符有两种表示 一种英文一种数字 &nbsp; &#1234;
# from html.parser import HTMLParser
# from urllib import request
# import re
#
#
# # class MyHTMLParser(HTMLParser):
# #     flag = False
# #     is_tag = ''
# #     is_data = []
# #
# #     def handle_starttag(self, tag, attrs):
# #         if tag == 'time':
# #             is_tag = 'time'
# #             self.flag = True
# #         if tag == 'h3':
# #             for i in attrs:
# #                 if i == 'event-title':
# #                     is_tag = 'title'
# #                     self.flag = True
# #         if tag == 'span':
# #             for i in attrs:
# #                 if i == 'event-title':
# #                     is_tag = 'address'
# #                     self.flag = True
# #
# #     def handle_data(self, data):
# #         if self.flag:
# #             self.is_data.append({self.is_tag: data})
# #
# #     def handle_endtag(self, tag):
# #         self.flag = False
# #
# # with request.urlopen('https://www.python.org/events/python-events/') as f:
# #     data = f.read().decode('utf-8')
# #
# # parser = MyHTMLParser()
# # parser.feed(data)
# # for item in MyHTMLParser.is_data:
# #     print(item)
#
# class MyHTMLParser(HTMLParser):
#     flag = 0
#     res = []
#     is_get_data = 0
#
#     def handle_starttag(self, tag, attrs):
#         # 首先找到包裹事件的元素
#         if tag == 'ul':
#             for attr in attrs:
#                 if re.match(r'list-recent-events', attr[1]):
#                     self.flag = 1
#
#         # 处理包裹事件名称的a元素
#         if tag == 'a' and self.flag == 1:
#             self.is_get_data = 'title'
#
#         # 处理时间的time元素
#         if tag == 'time' and self.flag == 1:
#             self.is_get_data = 'time'
#
#         # 处理包裹地点的time元素
#         if tag == 'span' and self.flag == 1:
#             self.is_get_data = 'addr'
#
#     def handle_endtag(self, tag):
#         if self.flag == 1 and tag == 'ul':
#             self.flag = 0
#
#     def handle_data(self, data):
#         if self.is_get_data and self.flag == 1:
#             if self.is_get_data == 'title':
#                 self.res.append({self.is_get_data: data})
#             else:
#                 self.res[len(self.res) - 1][self.is_get_data] = data
#             self.is_get_data = None
#
#
# parser = MyHTMLParser()
#
# with request.urlopen('https://www.python.org/events/python-events/') as f:
#     data = f.read().decode('utf-8')
#
# parser.feed(data)
# for item in MyHTMLParser.res:
#     print('---------------')
#     for k,v in item.items():
#         print("%s : %s" % (k,v))
# BeautifulSoup
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events/"


def crawl_page(url):
    return request.urlopen(url).read().decode("utf-8")


def parse_web(data):
    soup = BeautifulSoup(data, "html.parser")
    conference_list = soup.find('ul', attrs={'class': 'list-recent-events menu'})
    for li in conference_list.find_all("li"):
        print("meeting name:", li.find('h3', attrs={'class': 'event-title'}).getText())  # 名称
        print("time:", li.find('time').getText())
        print("address:", li.find('span', attrs={"class": "event-location"}).getText()+"\n")


if __name__ == '__main__':
    # print(crawl_page(url))
    parse_web(crawl_page(url))
