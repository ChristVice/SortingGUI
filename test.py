from main import Rectangle
import random
from copy import copy


def counting_sort(arr, exp1):
    n = len(arr)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] / exp1
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] / exp1
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    print(output)
    for i in range(0, len(arr)):
        arr[i] = output[i]
        # self.select(i, "i", "red")
        # time.sleep(0.005)
        # arr[i].set_height(output[i].height)
        # arr[i].redraw()

        # self.unselect("i")


def radix_sort(arr):
    max1 = max(arr)

    exp = 1
    while max1 / exp > 0:
        counting_sort(arr, exp)
        exp *= 10


import time

amount = 6
arr = [x for x in range(1, amount + 1)]
random.shuffle(arr)
# print([x.height for x in arr])
print("B ", arr)
radix_sort(arr)
print("A ", arr)
# print([x.height for x in arr])
# print(max([x.height for x in arr]))
