from functools import reduce
import time, functools

#name  = input("please enter your name: ")
#print("hello", name)

'''
print("1024*768=",1024*768) 
'''

#=====================
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2== ['hello','world','apple']:
    print('ce shi tong guo')
else:
    print('ce shi shi bai')

'''

#=====================
'''
def mul(*numbers):
    result = 1
    if len(numbers) == 0:
        raise TypeError
    else:
        for n in numbers:
            result = result * n
    
    return result

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
'''

#=====================
#map/reduce

def normalize(name):
    return name.title()
    #return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)

print (prod([3,5,7,9]))
if prod([3, 5, 7, 9]) == 945:
    print ("ce shi cheng gong1")
else:
    print ("ce shi shi bai1")


'''
def str2float(s):
    return float(s)
print (str2float('123.456'))
'''

#转化为folat
digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def str2float(s):
    index = s.index('.')
    s = s.replace('.', '')
    def fn(x, y):
        #print ('convert result === ', x*10 + y)
        return x*10 + y
    def char2num(s):
        #print ('digits result === ', digits[s])
        return digits[s]
    
    #print ('reduce result === ', reduce(fn, map(char2num, s)))
    #print ('divisor result === ', 10**(len(s)-index))
    return reduce(fn, map(char2num, s))/(10**(len(s)-index))   


print('zi fu chuan zhuan hua float',  str2float('123.456'))
if abs(str2float('123.456') - 123.456) <0.00001:
    print('ce shi cheng gong2')
else:
    print('ce shi shi bai2')

#==================
#filter

#筛选奇数
'''
def is_odd(n):
    return n%2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9,])))
print(list(map(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9,])))

#筛选回数
def is_palindrome(n):
        n = str(n)
        #print('111111', n)
        TF = False

        if len(n) == 1:
            TF = True
        else:
            for h in range(len(n)//2):
                #print('2222', n[h])
                #print('333333', n[-(h + 1)])
                if n[h] == n[-(h + 1)]:
                    TF = True 
                else:
                    break
            
        return TF

def is_palindrome2(n):
    return str(n) == str(n)[::-1] #字符串取倒叙!!!

output = filter(is_palindrome2, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome2, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('ce shi cheng gong3 ')
else:
    print('ce shi shi bai3')
'''

#===============
#sorted

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
results = []
def by_name(t):
    print('ttttttttttt==', t)
    #for i in range(len(t)):
        #results.append(t[i][0])
    return t[0]

def by_score(t):
    return t[1]

def by_score2(t):
    print('-t[1]==============', -t[1])
    return -t[1]

L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L, key=by_score, reverse=True)
print(L3)

L4 = sorted(L, key=by_score2)
print(L4)

#==============================
#返回函数 闭包 函数内嵌套函数
def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4, 5]:
    print('ce shi tong guo5!')
else:
    print('ce shi shi bai5!')

#=====================
#匿名函数 lambda 不用写return 一个表达式
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)

#========================
#装饰器 Decorator

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        print('Begin call %s' % fn.__name__)
        func = fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, end_time - start_time))
        print('End call %s' % fn.__name__)
        return func
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('ce shi shi bai 6')
elif s != 7986:
    print('ce shi shi bai 6')

#=====================
#偏函数 functools.partial
#把一个函数的某些参数给固定住，也就是设置默认值，返回一个新的函数，调用风简单

int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int('1000000'))

#===========================