# -*- coding: utf-8 -*-
# __author__ = 'k.'

def bublSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


a = [8, 6, 3, 1, 7, 9, 2, 5, 4]

def selectSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


'''i:刚抓索引'''
'''i-1:刚排好索引'''
'''j:正比较的索引'''
'''j--:前一张'''



def insertSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr

print(insertSort(a))

















