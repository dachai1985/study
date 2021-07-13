# _*_ xoding: utf-8 _*_

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    zone = re.match(r'(UTC)([+-]\d+):(\d+)', tz_str)
    print('zone.group2=========', zone.group(2))
    tz = timezone(timedelta(hours=int(zone.group(2)))) #根据时区数生成timezone类实例
    print('tz========', tz)
    dz_utc = dt.replace(tzinfo=tz) 

    return dz_utc.timestamp()



t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

#==============================
import base64

def safe_base64_decode(s):
    if len(s)% 4 == 0:
        sb64 = base64.b64decode(s)
    else:
        #lens = len(s) + (len(s) % 4)
        #s = s.ljust(lens, '=')
        s = s + '=' * (4 - len(s)% 4)
        sb64 = base64.b64decode(s)

    return sb64


print('11111111111111=', safe_base64_decode('YWJjZA=='))
print('22222222222222=', safe_base64_decode('YWJjZA'))

assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

#============================
import struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    print('data[:2]=====', data[:2])
    if data[:2] == b'BM':
        bmpinfo = data[0:30]
        re_bmpinfo = struct.unpack('<ccIIIIIIHH', bmpinfo)
        print(re_bmpinfo)

        return{
            'width': re_bmpinfo[6],
            'height': re_bmpinfo[7],
            'color': re_bmpinfo[9]
        }
    return None

bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

#========================
import hashlib
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

#验证用户登录

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    print('calc_md5(password)=======', calc_md5(password))
    print("db['user']=========", db[user])

    return calc_md5(password) == db[user]

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

#===============================
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        print('self.salt============', self.salt)
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    #print('user.password==========', user.password )
    #print('get_md5(password)==========', get_md5(password) )

    return user.password == get_md5(password + user.salt)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

#========================
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48,122)) for i in range(20)])

        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]

    return user.password == hmac_md5(user.key, password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

#=========================
import itertools
#计算圆周率pi

def pi(N):
    '计算pi的值'
    #step 1：创建一个奇数序列：1， 3， 5， 7， 9， ...
    natuals = itertools.count(1, 2)

    #step 2: 取该序列的前N项：1, 3, 5, 7, 9, ..., 2*N -1.
    ns = list(itertools.takewhile(lambda x: x <= 2*N-1, natuals))
    #print('List===========', ns)

    #step 3: 添加正负符号并用4除：4/1， -4/3， 4/5， -4/7， 4/9， ...
    #step 4: 求和：
    sum = 0
    for i, value in enumerate(ns):
        # **i代表i次方， -1的0次方等于1
        sum += (-1)**i / value * 4

    return sum

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

#=================
#memo-遍历list

list1 = [1, 3, 5]
sum1 = 0
for i,value in enumerate(list1):
    print('i==========', i)
    print('(-1)**i===========', (-1)**i)
    print('value===========', value)
    print('(-1)**i / value * 4========', (-1)**i / value * 4)
    sum1 += (-1)**i / value * 4

print(sum1)
