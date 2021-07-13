# -*- coding: utf-8 -*-

'''def trim(s):
    start = 0
    end = 0
    for i1 in range(len(s)):
        if s[i1].isspace():
            pass
        else:
            start = i1
            print('start=', start)
            break

    for i2 in range(len(s)):
        i2 = i2 + 1
        if s[-i2].isspace():
            pass
        else:
            end = len(s) - i2 + 1
            print('end=', end)
            break
    
    s = s[start:end]
  
    print ('s=', s)

    return s
    
if trim('hello  ') != 'hello':
    print ('测试失败1')
elif trim('  hello  ') != 'hello':
    print ('测试失败2')
elif trim('  hello') != 'hello':
    print ('测试失败3')
elif trim(' ') != '':
    print ('测试失败4')
elif trim('   ') != '':
    print ('测试失败5')
else:
    print ('测试成功1')
    
'''

def trim2(s):

    if s[0] == ' ':
        if len(s) > 1:
            s = s[1:]
            return trim2(s)
        else:
            return ''

    elif s[-1] == ' ':
        s = s[:-1]
        return trim2(s)
    else:
        return s
     


if trim2('hello  ') != 'hello':
    print ('测试失败1')
elif trim2('  hello  ') != 'hello':
    print ('测试失败2')
elif trim2('  hello') != 'hello':
    print ('测试失败3')
elif trim2(' ') != '':
    print ('测试失败4')
elif trim2('   ') != '':
    print ('测试失败5')
else:
    print ('测试成功2')