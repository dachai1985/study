import random

# num = int(input("Enter a number: "))
#
# lst = []
#
# for i in range(num):
#     #value = int(random.randint(1,num))
#     value = int(input())
#     if value not in lst:
#         lst.append(value)
#
# lst = sorted(lst)
# for i in lst:
#     print(i)

# =======
# 回文数
def isPalindrome(x):
    return str(x) == str(x)[::-1]
print(isPalindrome(121))
# ======
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in a if num % 2!= 0]
even_numbers = [num for num in a if num % 2 == 0]
print(odd_numbers)
print(even_numbers)

# =======
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1): # 平方根取整后加1的所有整数
        if n % i == 0:
            return False
        return True


# Testing the function
print(is_prime(7)) # True
print(is_prime(10)) # False
print(is_prime(1)) # False
print(is_prime(2)) # True

# =======
def test(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # print(test(n-1), test(n-2))
        return test(n-1) + test(n-2)

# Testing the function
# print(feibonacci(0)) # 0
# print(feibonacci(1)) # 1
# print(feibonacci(2)) # 1
print(test(10)) # 2

def fibonacci1(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b
    return a

print(list(fibonacci1(10))) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# =======
def func(*args, **kwargs):
    print(args)
    print(kwargs)
func(1, 2, 3, a=4, b=5) # (1, 2, 3) {'a': 4, 'b': 5}

# =======
# 递归函数-阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        result = factorial(n-1) # 避免重复的递归调用和输出
        print("check data1：", n, result)
        # print("check data1：", n, factorial(n-1))
        # return n * factorial(n-1) # 递归调用 阶乘
        return n * result

print(factorial(3)) # 120

# 尾递归优化
def factorial(n, acc=1): # accumulative 累积参数
    if n == 0:
        return acc
    else:
        print("check data2：",n, acc)
        return factorial(n-1, n*acc)

print(factorial(5)) # 120

# =======
# 找出列表中第二大元素
def second_largest(lst):
    if len(lst) < 2:
        return None
    else:
        max1 = max(lst[0], lst[1])
        max2 = min(lst[0], lst[1])
        for i in range(2, len(lst)):
            if lst[i] > max1:
                max2 = max1
                max1 = lst[i]
            elif lst[i] > max2 and lst[i]!= max1:
                max2 = lst[i]
        return max2

print(second_largest([1, 2, 3, 4, 5])) # 4
print(second_largest([1, 2, 3, 4, 5, 6])) # 5
print(second_largest([1])) # None
print(second_largest([])) # None

# =======
# 应用场景 日志记录记录函数调用信息参数和返回值，性能监控测量函数执行时间，缓存提高性能。
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper


@decorator
def add(x, y):
    return x + y

print(add(2, 3)) # Before calling the function, 5, After calling the function, 5

# =======
def my_generator():
    for i in range(10):
        yield i

for i in my_generator():
    print(i)

# =======
# 闭包 内部函数引用外部函数的变量，外部函数返回内部函数的引用 应用场景 实现计数器
def outer():
    counter = 0
    def inner():
        print("Inner function")
        nonlocal counter
        counter += 1
        print(counter)
    return inner # 返回的是inner函数的引用

inner_func = outer() # 调用outer函数，并返回inner函数的引用
inner_func() # 调用inner函数 执行结果 Inner function 1
inner_func() # 调用inner函数 执行结果 Inner function 2

# =======
# 多线程 应用场景 并发处理
import threading

def my_func(name):
    print("Hello, ", name)

t1 = threading.Thread(target=my_func, args=("Alice1",))
t2 = threading.Thread(target=my_func, args=("Bob1",))

t1.start()
t2.start()

# =======
# 协程 应用场景 异步处理
import asyncio

async def my_coroutine(name):
    print("Hello, ", name)

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(my_coroutine("Alice2")),
    asyncio.ensure_future(my_coroutine("Bob2"))
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# =======
# 多进程 应用场景 并行处理
# import multiprocessing
#
# def my_func(name):
#     print("Hello, ", name)
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=my_func, args=("Alice3",))
#     p2 = multiprocessing.Process(target=my_func, args=("Bob3",))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()

# =======
# 排序算法 应用场景 排序
# 交换两个序列中a，b的元素，使得他们的和之差最小(也就是尽量使两个序列的和相等)
a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
b = [2, 7, 1, 8, 2, 8, 1, 4, 8, 4, 6]
def balance_sorted(sorted_list):
    if not sorted_list:
        return [], []
    big = sorted_list[-1]
    small = sorted_list[-2]
    list1, list2 = balance_sorted(sorted_list[:-2])
    list1.append(small)
    list2.append(big)
    if sum(list1) > sum(list2):
        return list1, list2
    else:
        return list2, list1

# 合并并排序
source = sorted(a + b)
a_new, b_new = balance_sorted(source)

# 输出结果
print(a_new) # [1, 1, 2, 2, 4, 4, 5, 5, 7, 8, 9]
print(b_new) # [1, 1, 2, 3, 3, 4, 5, 6, 6, 8, 8]

#通过迭代方式避免带来性能问题
def balance_sorted_iterative(sorted_list):
    list1 = []
    list2 = []
    for num in reversed(sorted_list):
        if sum(list1) > sum(list2):
            list1.append(num)
        else:
            list2.append(num)
    return list1, list2

# 输出结果
source = sorted(a + b)
a_new, b_new = balance_sorted_iterative(source)
print(a_new) # [1, 1, 2, 2, 4, 4, 5, 5, 7, 8, 9]
print(b_new) # [1, 1, 2, 3, 3, 4, 5, 6, 6, 8, 8]

# =======
# 二分查找 应用场景 查找元素
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 输出结果
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(lst, 5)) # 4
print(binary_search(lst, 10)) # -1

# =======
# 进制转换 应用场景 数字与字母的转换
def convertToTitle(columnNumber):
    result = []
    while columnNumber > 0:
        columnNumber -= 1           # 转为 0-based 索引
        remainder = columnNumber % 26  # 计算当前位的字母索引（0-25）
        result.append(chr(ord('A') + remainder))  # 转换为字母
        columnNumber = columnNumber // 26  # 更新为更高位的值
    return ''.join(reversed(result))  # 反转拼接结果

# 输出结果
print(convertToTitle(1)) # A
print(convertToTitle(28)) # AB
print(convertToTitle(701)) # ZY

# =======
# 移除元素 应用场景 数组元素的删除
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# 输出结果
nums = [3, 2, 2, 3]
print(removeElement(nums, 3)) # 2

# =======
# 旋转数组 应用场景 数组元素的旋转 --杨辉三角
def generate(numRows):
    if numRows == 0:
        return []

    result = [[1]]  # 初始化第一行

    for i in range(1, numRows):
        row = [1] * (i + 1)  # 创建当前行，首尾为1
        for j in range(1, i):
            # 中间元素等于上一行相邻两数之和
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)

    return result

# 输出结果
print(pgenerate(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# =======
# 寻找重复数 应用场景 数组元素的重复
def removeDuplicates(nums):
    if not nums:
        return 0
    j = 0  # 慢指针
    for i in range(1, len(nums)):  # 快指针从第二个元素开始
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]  # 覆盖重复项
    return j + 1  # 新长度
# 输出结果
nums = [1, 1, 2]
print(removeDuplicates(nums)) # 2

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
# 输出结果
print(singleNumber([2, 2, 1])) # 1

# =======
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # 处理空链表情况
    if not l1:
        return l2
    if not l2:
        return l1

    # 创建哑节点和当前指针
    dummy = ListNode(-1)
    curr = dummy

    # 遍历比较两个链表的节点
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next  # 移动当前指针

    # 将剩余非空链表直接接上
    curr.next = l1 if l1 else l2

    return dummy.next
# 输出结果
print(mergeTwoLists([1, 2, 4], [1, 3, 4]))

# =======
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # 避免重复使用同一元素
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# 输出结果
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target)) # [0, 1]

# =======


