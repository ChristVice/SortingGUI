import random
import time
import numpy as np
from tkinter import *


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x + width
        self.completed_color = "#00b200"
        self.outline = "black"

    def __str__(self):
        return f"h:{self.height} | x:{self.x} | y:{self.y} | x2:{self.x2}"


class SortingAlgorithm:
    def __init__(self):
        self.width = 900
        self.height = 500
        self.window = Tk()
        self.window.title("Sorting Algorithms")
        self.window.geometry(f"{self.width}x{self.height}")  # WxH
        self.window.resizable(False, False)
        self.window.config(bg="#ffffff")
        self.window.iconphoto(False, PhotoImage(file="images/icon.png"))

        self.bars_recs = []
        self.chosen_ones = []
        self.ranints = []

        self.top_canvas = Canvas(self.window, width=self.width, height=50)
        self.bar_canvas = Canvas(self.window, width=self.width, height=500, bg="white")
        self.top_canvas.pack(side=TOP)
        self.bar_canvas.pack(side=BOTTOM)
        self.Sorting_GUI()

        self.window.mainloop()

    def sorting_completed(self):
        for index in range(len(self.bars_recs)):
            self.bar_canvas.delete(self.bars_recs[index][1])
            self.bar_canvas.update()
            self.bar_canvas.create_rectangle(
                self.bars_recs[index][0].x,
                self.bars_recs[index][0].y,
                self.bars_recs[index][0].x2,
                self.bars_recs[index][0].height,
                fill=self.bars_recs[index][0].completed_color,
                outline=self.bars_recs[index][0].completed_color,
                activefill="black",
            )
            self.bar_canvas.update()

    def chosen_bar(self, index, tag, color="blue"):
        self.chosen_ones.append(
            [
                tag,
                self.bar_canvas.create_rectangle(
                    self.bars_recs[index][0].x,
                    self.bars_recs[index][0].y,
                    self.bars_recs[index][0].x2,
                    self.bars_recs[index][0].height,
                    fill=color,
                    outline=color,
                ),
            ]
        )

        self.bar_canvas.update()

    def delete_chosen(self, tag):
        for arr in self.chosen_ones:
            if arr[0] == tag:
                self.bar_canvas.delete(arr[1])

    def replace_bar(self, index, fill="black", height=10):
        self.bar_canvas.delete(self.recs[index])
        self.bar_canvas.create_rectangle(
            self.bars[index].x,
            self.bars[index].y,
            self.bars[index].x2,
            height,
            fill=fill,
            outline=fill,
        )

    def switch_bars(self, i1, i2):
        og_x = self.bars_recs[i1][0].x
        des_x = self.bars_recs[i2][0].x

        while self.bars_recs[i1][0].x != des_x:
            if self.bars_recs[i1][0].x < des_x:  # moves bar to right
                self.bar_canvas.move(self.bars_recs[i1][1], 1, 0)  # moves i1 bar to i2
                self.bar_canvas.update()
                self.bars_recs[i1][0].x += 1
                self.bars_recs[i1][0].x2 += 1

                self.bar_canvas.move(self.bars_recs[i2][1], -1, 0)  # moves i2 to og_x
                self.bar_canvas.update()
                self.bars_recs[i2][0].x -= 1
                self.bars_recs[i2][0].x2 -= 1

            elif self.bars_recs[i1][0].x > des_x:
                self.bar_canvas.move(self.bars_recs[i1][1], -1, 0)
                self.bar_canvas.update()
                self.bars_recs[i1][0].x -= 1
                self.bars_recs[i1][0].x2 -= 1

                self.bar_canvas.move(self.bars_recs[i2][1], 1, 0)
                self.bar_canvas.update()
                self.bars_recs[i2][0].x += 1
                self.bars_recs[i2][0].x2 += 1

            self.bar_canvas.update()

        self.bars_recs[i1], self.bars_recs[i2] = self.bars_recs[i2], self.bars_recs[i1]

    def Sorting_GUI(self):
        x1 = 0
        y1 = 2
        gap = 2
        rec_width = 1

        amount_of_bars = self.width // (rec_width + gap)

        self.ranints = [x for x in range(1, amount_of_bars + 1)]
        random.shuffle(self.ranints)

        for i in range(amount_of_bars):
            height = self.ranints[i]
            self.bars_recs.append(
                [
                    Rectangle(x1, y1, rec_width, height),
                    self.bar_canvas.create_rectangle(
                        x1,
                        y1,
                        rec_width + x1,
                        height,
                        outline="black",
                        activefill="black",
                    ),
                ]
            )
            x1 += rec_width + gap

        self.quick_sort(self.bars_recs, 0, len(self.bars_recs) - 1)
        # self.selection_sort(self.bars_recs)

        self.sorting_completed()

        # OLD VERSIONS
        # self.bubble_sort(self.bars)
        # self.insertion_sort(self.bars)
        # self.heap_sort(self.bars)
        # self.merge_sort(self.bars) NEEDS FIXING
        # self.replace_bar(0, fill="blue", height=50)

    # _____________SORTING ALGORITHMS____________________________
    # SELECTION SORT                        ---------------
    def selection_sort(self, arr):  # works, sorts bars
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx][0].height > arr[j][0].height:
                    self.chosen_bar(min_idx, "0", color="red")
                    self.chosen_bar(j, "0", color="red")
                    min_idx = j

                self.delete_chosen("0")

            self.switch_bars(min_idx, i)

    # BUBBLE SORT                            ---------------
    def bubble_sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j].height > arr[j + 1].height:
                    self.switch_bars(j, j + 1)

    # INSERTION SORT                        ---------------
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i].height
            j = i - 1

            while j >= 0 and key < arr[j].height:
                self.switch_bars(j + 1, j)
                j -= 1

            arr[j + 1].height = key

    # HEAP SORT                             ---------------
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest].height < arr[l].height:
            largest = l

        if r < n and arr[largest].height < arr[r].height:
            largest = r

        if largest != i:
            self.switch_bars(i, largest)
            # arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            self.switch_bars(i, 0)
            # arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    # QUICK SORT                            ---------------
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high][0].height
        self.chosen_bar(high, "pivot")

        for j in range(low, high):
            if arr[j][0].height <= pivot:
                i = i + 1

                self.chosen_bar(j, "0", color="red")
                self.chosen_bar(i, "0", color="red")
                self.switch_bars(i, j)

            self.delete_chosen("0")

        self.chosen_bar(i + 1, "0", color="red")
        self.chosen_bar(high, "0", color="red")
        self.switch_bars(i + 1, high)  # will switch bars
        self.delete_chosen("0")

        self.delete_chosen("pivot")
        return i + 1

    def quick_sort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    # MERGE SORT                            ---------------
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i].height < R[j].height:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    # BUCKET SORT                           ---------------
    def bucketSort(self, arr):
        bucket = []

        # Create empty buckets
        for i in range(len(arr)):
            bucket.append([])

        # Insert elements into their respective buckets
        for j in arr:
            index_b = int(10 * j)
            bucket[index_b].append(j)

        # Sort the elements of each bucket
        for i in range(len(arr)):
            bucket[i] = sorted(bucket[i])

        # Get the sorted elements
        k = 0
        for i in range(len(arr)):
            for j in range(len(bucket[i])):
                arr[k] = bucket[i][j]
                k += 1
        return arr

    # RADIX SORT                            ---------------


if __name__ == "__main__":
    SortingAlgorithm()
