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
        return f"H::{self.height} x::{self.x} y::{self.y} x2::{self.x2}"


class SortingAlgorithm:
    def __init__(self):
        self.width = 900
        self.height = 570
        self.window = Tk()
        self.window.title("Sorting Algorithms")
        self.window.geometry(f"{self.width}x{self.height}")  # WxH
        self.window.resizable(False, False)
        self.window.config(bg="#ffffff")
        self.window.iconphoto(False, PhotoImage(file="images/icon.png"))

        self.chosen_ones = []

        self.top_canvas = Canvas(self.window, width=self.width, height=50)
        self.bar_canvas = Canvas(self.window, width=self.width, height=500, bg="white")
        self.top_canvas.pack(side=TOP)
        self.bar_canvas.pack(side=BOTTOM)
        self.Sorting_GUI()

        self.window.mainloop()

    def sorting_completed(self):
        self.completion_bars = []
        for index in range(len(self.bars_recs)):
            self.bar_canvas.delete(self.bars_recs[index][1])
            self.bar_canvas.update()
            self.completion_bars.append(
                self.bar_canvas.create_rectangle(
                    self.bars_recs[index][0].x,
                    self.bars_recs[index][0].y,
                    self.bars_recs[index][0].x2,
                    self.bars_recs[index][0].height,
                    fill=self.bars_recs[index][0].completed_color,
                    outline=self.bars_recs[index][0].completed_color,
                    activefill="black",
                )
            )
            self.bar_canvas.update()

    def reset(self):
        self.chosen_ones = []
        for i in self.completion_bars:
            self.bar_canvas.delete(i)

    def select_bar(self, index, tag, color="blue"):
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

    def replace_bar(self, old_bar, new_bar):
        index = self.bars_recs.index(old_bar)
        print("GGG", self.bars_recs[index])
        self.bar_canvas.delete(self.bars_recs[index][1])
        self.bars_recs[index] = new_bar
        print("AAA", self.bars_recs[index])
        self.bar_canvas.create_rectangle(
            self.bars_recs[index][0].x,
            self.bars_recs[index][0].y,
            self.bars_recs[index][0].x2,
            self.bars_recs[index][0].height,
            outline=self.bars_recs[index][0].outline,
            activefill="black",
        )
        self.bar_canvas.update()

    def switch_bars(self, i1, i2, speed=0):
        og_x = self.bars_recs[i1][0].x
        des_x = self.bars_recs[i2][0].x

        while self.bars_recs[i1][0].x != des_x:
            time.sleep(speed)
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

    def randomize(self, gap=1, width=10, min_height=1):
        self.bars_recs = []
        x1 = 0
        y1 = 2
        gap = gap
        rec_width = width

        amount_of_bars = self.width // (rec_width + gap)

        self.ranints = [x for x in range(min_height, amount_of_bars + min_height)]
        random.shuffle(self.ranints)

        for i in range(amount_of_bars):
            self.bars_recs.append(
                [
                    Rectangle(x1, y1, rec_width, self.ranints[i]),
                    self.bar_canvas.create_rectangle(
                        x1,
                        y1,
                        rec_width + x1,
                        self.ranints[i],
                        outline="black",
                        activefill="black",
                    ),
                ]
            )
            x1 += rec_width + gap

    def Sorting_GUI(self):
        self.randomize(gap=1, width=1)

        # self.selection_sort(self.bars_recs)
        # self.quick_sort(self.bars_recs, 0, len(self.bars_recs) - 1)
        # self.bubble_sort(self.bars_recs)
        # self.insertion_sort(self.bars_recs)
        # self.heap_sort(self.bars_recs)
        start = time.time()
        self.merge_sort(self.bars_recs)
        end = time.time()
        self.sorting_completed()
        print(end - start)

        self.reset()
        self.randomize(gap=1, width=1)

        start = time.time()
        self.quick_sort(self.bars_recs, 0, len(self.bars_recs) - 1)
        end = time.time()
        self.sorting_completed()
        print(end - start)

        self.reset()
        self.randomize(gap=1, width=1)

        start = time.time()
        self.selection_sort(self.bars_recs)
        end = time.time()
        self.sorting_completed()
        print(end - start)

        # OLD VERSIONS
        # self.merge_sort(self.bars) NEEDS FIXING
        # self.replace_bar(0, fill="blue", height=50)

    # _____________SORTING ALGORITHMS____________________________
    # SELECTION SORT                        ---------------
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j][0].height < arr[min_idx][0].height:
                    min_idx = j

            self.select_bar(min_idx, "min", "red")
            self.select_bar(i, "i")
            self.switch_bars(min_idx, i)  # switch spots
            self.delete_chosen("i")
            self.delete_chosen("min")

    # BUBBLE SORT                           ---------------
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j][0].height > arr[j + 1][0].height:
                    self.select_bar(j, "j")
                    self.select_bar(j + 1, "j1", "red")
                    self.switch_bars(j, j + 1)
                    self.delete_chosen("j")
                    self.delete_chosen("j1")

    # INSERTION SORT                        ---------------
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i][0].height
            j = i - 1

            while j >= 0 and key < arr[j][0].height:
                self.select_bar(j + 1, "j1")
                self.select_bar(j, "j", "red")
                self.switch_bars(j + 1, j, 0.0025)
                self.delete_chosen("j1")
                self.delete_chosen("j")
                j -= 1

            arr[j + 1][0].height = key

    # HEAP SORT                             ---------------
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest][0].height < arr[l][0].height:
            largest = l

        if r < n and arr[largest][0].height < arr[r][0].height:
            largest = r

        if largest != i:

            self.select_bar(i, "i")
            self.select_bar(largest, "lar", "red")
            self.switch_bars(i, largest)
            self.delete_chosen("i")
            self.delete_chosen("lar")

            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            self.select_bar(i, "i")
            self.select_bar(0, "0", "red")
            self.switch_bars(i, 0)
            self.delete_chosen("i")
            self.delete_chosen("0")

            self.heapify(arr, i, 0)

    # QUICK SORT                            ---------------
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high][0].height
        self.select_bar(high, "pivot")

        for j in range(low, high):
            if arr[j][0].height <= pivot:
                i = i + 1

                self.select_bar(j, "0", color="red")
                self.select_bar(i, "0", color="red")
                self.switch_bars(i, j)

            self.delete_chosen("0")

        self.select_bar(i + 1, "0", color="red")
        self.select_bar(high, "0", color="red")
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
                if L[i][0].height < R[j][0].height:
                    self.select_bar(self.bars_recs.index(arr[k]), "k")
                    self.select_bar(self.bars_recs.index(L[i]), "L", "red")
                    self.switch_bars(
                        self.bars_recs.index(arr[k]), self.bars_recs.index(L[i])
                    )

                    arr[k] = L[i]

                    self.delete_chosen("k")
                    self.delete_chosen("L")
                    i += 1
                else:
                    self.select_bar(self.bars_recs.index(arr[k]), "k")
                    self.select_bar(self.bars_recs.index(R[j]), "R", "red")
                    self.switch_bars(
                        self.bars_recs.index(arr[k]), self.bars_recs.index(R[j])
                    )

                    arr[k] = R[j]

                    self.delete_chosen("k")
                    self.delete_chosen("R")
                    j += 1
                k += 1

            while i < len(L):
                self.select_bar(self.bars_recs.index(arr[k]), "k")
                self.select_bar(self.bars_recs.index(L[i]), "L", "red")
                self.switch_bars(
                    self.bars_recs.index(arr[k]), self.bars_recs.index(L[i])
                )

                arr[k] = L[i]

                self.delete_chosen("k")
                self.delete_chosen("L")
                i += 1
                k += 1

            while j < len(R):
                self.select_bar(self.bars_recs.index(arr[k]), "k")
                self.select_bar(self.bars_recs.index(R[j]), "R", "red")
                self.switch_bars(
                    self.bars_recs.index(arr[k]), self.bars_recs.index(R[j])
                )

                arr[k] = R[j]

                self.delete_chosen("k")
                self.delete_chosen("R")
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
