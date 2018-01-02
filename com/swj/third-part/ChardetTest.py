# -*- coding: utf-8 -*-

# 对未知编码的bytes 要把他转为str 需要先猜测编码 猜测的方式是收集各种编码的特征字符 根据特征字符判断 就能有很大概率猜对
# chardet就是检测编码的第三方库
import chardet
if __name__ == '__main__':
    print(chardet.detect(b'Hello, World!'))  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''} encoding是编码 confidence是猜测准确的概率 language是语言
    print(chardet.detect('寿炜剑'.encode('utf-8')))  # {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
    print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))  # {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

