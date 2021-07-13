
def move(n, a, b, c):
    if n ==1:
        print (a, '-->', c)
        return
    else:
        move(n-1, a, c, b)
        print (a, '-->', c)
        move(n-1, b, a, c)

move(3,'A','B','C')

'''
move(2, A, C, B)
A->C
move(2, B, A, C)

move(2, A, C, B)  ====>
2!=1
move(1, A, B, C) A->C
A->B
move(1, C, A, B) C->B
....
move(2, B, A, C)  ===>
2!=1
move(1, B, C, A) B->A
B->C
move(1, A, B, C) A->C
'''