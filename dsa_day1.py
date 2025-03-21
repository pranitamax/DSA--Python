# -*- coding: utf-8 -*-
"""DSA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cSqN54hfOxwabRIlv-X_cqjHa4PcGaiz
"""



def sort_by_tuple_sum(lst):
    n = len(lst)
    for i in range(n):

        for j in range(0, n-i-1):

            sum1 = lst[j][0] + lst[j][1]
            sum2 = lst[j+1][0] + lst[j+1][1]
            if sum1 > sum2:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

print(sort_by_tuple_sum([(3, 1), (2, 2), (5, -1), (0, 0)]))
print(sort_by_tuple_sum([(7, 3), (1, 2), (4, 5), (0, 1)]))
print(sort_by_tuple_sum([(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]))

def filter_strings(lst, k, m):
    vowel = ['a', 'e', 'i', 'o', 'u']
    new = []

    for item in lst:
        k1 = len(item)
        m1 = 0

        for char in item:
            if char in vowel:
                m1 += 1
        if k1 >= k and m1 >= m:
            new.append(item)

    return new

print(filter_strings(["apple", "hi", "world", "yes", "python"], 4, 2))
print(filter_strings(["education", "science", "art", "mathematics"], 5, 3))

def length_of_last_word(s):
    lst = s.split()
    length = len(lst[-1])
    return length


s= "Learn Python"
print(length_of_last_word(s))
s= " coding is fun "
print(length_of_last_word(s))
s= " fly me to the moon "
print(length_of_last_word(s))
6

def find_fist_last_pos(arr, x):
    n = len(arr)

    first = -1
    last = -1

    for i in range(n):

        if x != arr[i]:
            continue

        if first == -1:
            first = i

        last = i
    res = [first, last]
    return res

nums = [5,7,7,8,8,10]
target = 8
print(find_fist_last_pos(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(find_fist_last_pos(nums, target))

nums = []
target = 0
print(find_fist_last_pos(nums, target))