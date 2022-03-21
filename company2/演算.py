# import copy
#
# list_1 = [1, 2, 3]
# list_2 = [list_1]
# list_3 = copy.copy(list_2)
# list_4 = copy.deepcopy(list_2)
# # Please write your code here
# print(list_1 is list_2[0])
# print(list_1 is list_3[0])
# print(list_1 is list_4[0])
# print(list_2 is list_3[0])
# print(list_2 is list_4[0])
# print(list_3)
# print(list_4)

# list1 = [1, 2]
# list2 = [1, 2]
# print(list1 == list2)
# print(list1 is list2)
#
# # 小整数对象池（pool) = [1......256]
# list_a = [7, 2, 5, 4, 3]  # O(n)
# for x in list_a:
#     if x == 8:
#         print(x)
# map = {1: 3, 7: 9, 8: 1}
# map[8]  # O(1)
#
# num_1 = 256  # const[255]
# num_2 = 256
# print(num_1 is num_2)
# num_1 = 257  # new object 257
# num_2 = 257  # new object 257
# print(num_1 is num_2)  # 同一个id
# print(num_1 == num_2)  # 值一样就可以
# num_1 = -5
# num_2 = -5
# print(num_1 is num_2)
# num_1 = -6
# num_2 = -6
# print(num_1 is num_2)
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print(power(3, 3))
#
# price = 70
# print(f'{price:.2f}')

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         return
#
#
# class SingleLink():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#         return
# def add(int_1):
#     return (int_1 * 4 + 3 * 10 * int_1 + 2 * 100 * int_1 + 1000 * int_1)
#
#
# print(add(5))

# a = b = c = 3334
# print(id(a), id(b), id(c))
# print(a is b)
date_time = str(input())
print(int(date_time[4:6])+1)
print(date_time[4:6])
# 20130314