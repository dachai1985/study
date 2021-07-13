def findMinAndMax(L):
    if not isinstance(L, (list)):
        return (None, None)
    if len(L) == 0:
        return (None, None)
    else:
        imax = L[0]
        imin = L[0]
        for i in L:
            if isinstance(i, str):
                print ('1111')
                continue
            elif i >= imax:
                imax = i 
            elif i <= imin:
                imin = i
            
        return (imin, imax)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
elif findMinAndMax([7, 1, '', 9, 'eee']) != (1, 9):
    print('测试失败!')    
else:
    print('测试成功!')