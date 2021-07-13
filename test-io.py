
# -*- coding: utf-8 -*-

fpath = 'E:/python/test file.txt'

with open(fpath, 'r', errors='ignore') as f:
    s = f.read()
    print(s)

with open(fpath, 'r', encoding='UTF-8') as f:
    s = f.read()
    print(s)

#==========================
import os

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(os.path.abspath)

#===========================
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
s2 = json.dumps(obj, ensure_ascii=True)
s3 = json.dumps(obj)
print(s, '\n', s2, '\n', s3)