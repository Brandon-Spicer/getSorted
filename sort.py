import math
import random


def bubble(arr):
    n = len(arr)
    count = 0
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            print('-'*10)
            print(f'count = {count}')
            print(f'i = {i}')
            print(f'j = {j}')
            count += 1

            if arr[j] > arr[j + 1]:
                swap = True
                print(f'swap {arr[j]} and {arr[j+1]}')
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            else:
                print('no swap')

            print(' '.join([str(i) for i in range(n)]))
            print(' '.join([str(a) for a in arr]))
        if not swap:
            print('DONE EARLY')
            break

    return arr
            
def insertion(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[i - j] < arr[i - j - 1]:
                temp = arr[i - j]
                arr[i - j] = arr[i - j - 1]
                arr[i - j - 1] = temp
            else:
                break

    return arr
            

# simple binary search
def binarySearch(arr, v):
    n = len(arr)

    if n == 0:
        return False
    if n == 1:
        return arr[0] == v

    return binarySearch(arr[:n//2], v) or binarySearch(arr[n//2:], v)

    

# binary search with index return
def binarySearch2(arr, v, index=0):
    n = len(arr)

    if n == 0:
        return math.inf
    if n == 1:
        if arr[0] == v:
            return index
        else:
            return math.inf

    left = binarySearch2(arr[:n//2], v, index) # returns n in range(-1, n)
    right = binarySearch2(arr[n//2:], v, index + n//2) # returns n in range(-1, n)

    return min(left, right)


# now what?
# binary insertion sort
# binary search the virtual list
# 
