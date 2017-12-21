# -*- coding: utf-8 -*-
import os


def findall(path, str):
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    for x in files:
        if x.find(str) >= 0:
            print(os.path.join(path, x))
    for x in dirs:
        findall(os.path.join(path, x), str)
findall('C:\\Users\\swj\\PycharmProjects', '.py')


