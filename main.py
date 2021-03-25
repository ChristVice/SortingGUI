import random
import time
import copy
from tkinter import *


class Rectangle:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x + width

    def redraw(self, color="#495057"):
        self.canvas.delete(self.rec)
        self.rec = self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x2,
            self.height,
            outline=color,
        )

    def draw(self):
        self.rec = self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x2,
            self.height,
            outline="#495057",
        )

    def highlight(self, color="red"):
        self.hlight = self.canvas.create_rectangle(
            self.x, self.y, self.x2, self.height, fill=color, outline=color
        )
        self.canvas.update()

    def unhighlight(self):
        self.canvas.delete(self.hlight)
        self.hlight = None

    def set_height(self, height):
        self.height = height

    def set_x(self, x):
        self.x = x
        self.x2 = self.x + self.width

    def __str__(self):
        return f"H::{self.height} x1::{self.x} x2::{self.x2} y::{self.y}"


class SortingAlgorithm:
    def __init__(self):
        self.window = Tk()

        self.width = 1080
        self.height = 600

        self.window.title("Sorting Algorithms")
        self.window.geometry(f"{self.width}x{self.height}")  # WxH
        self.window.resizable(False, False)
        self.window.config(bg="#ffffff")
        self.window.iconphoto(False, PhotoImage(file="images/icon.png"))

        self.chosen_ones = []

        self.top_canvas = Canvas(self.window, width=self.width, height=50)
        self.bar_canvas = Canvas(
            self.window, width=self.width, height=self.height - 20, bg="white"
        )
        self.top_canvas.pack(side=TOP)
        self.bar_canvas.pack(side=BOTTOM)
        self.Sorting_GUI()

        self.window.mainloop()

    def completed(self, completed_color="#00b200"):
        self.completion_bars = []
        for index in range(len(self.bars)):
            self.bar_canvas.delete(self.bars[index].rec)
            self.bar_canvas.update()
            self.completion_bars.append(
                self.bar_canvas.create_rectangle(
                    self.bars[index].x,
                    self.bars[index].y,
                    self.bars[index].x2,
                    self.bars[index].height,
                    fill=completed_color,
                    outline=completed_color,
                )
            )
            self.bar_canvas.update()

    def empty(self):
        self.bar_canvas.delete("all")
        self.chosen_ones = []
        self.completion_bars = []

    def select(self, index, tag, color="blue"):
        self.chosen_ones.append(
            [
                tag,
                self.bar_canvas.create_rectangle(
                    self.bars[index].x,
                    self.bars[index].y,
                    self.bars[index].x2,
                    self.bars[index].height,
                    fill=color,
                    outline=color,
                ),
            ]
        )

        self.bar_canvas.update()

    def unselect(self, tag):
        for arr in self.chosen_ones:
            if arr[0] == tag:
                self.bar_canvas.delete(arr[1])
                self.chosen_ones.remove(arr)

    def switch(self, i1, i2):
        og_x = self.bars[i1].x
        des_x = self.bars[i2].x

        self.bar_canvas.moveto(self.bars[i1].rec, str(des_x - 1), "1")
        self.bars[i1].set_x(des_x)

        self.bar_canvas.moveto(self.bars[i2].rec, str(og_x - 1), "1")
        self.bars[i2].set_x(og_x)

        self.bar_canvas.update()
        self.bars[i1], self.bars[i2] = self.bars[i2], self.bars[i1]

    def randomize(self, gap=1, width=10, min_height=1):
        self.bars = []
        x1 = 2
        y1 = 2
        gap = gap
        rec_width = width

        amount_of_bars = self.width // (rec_width + gap)
        self.ranints = [x for x in range(1, amount_of_bars + 1)]
        random.shuffle(self.ranints)

        for i in range(amount_of_bars):
            self.bars.append(
                Rectangle(self.bar_canvas, x1, y1, rec_width, self.ranints[i])
            )
            x1 += rec_width + gap
            self.bars[i].draw()

    def Sorting_GUI(self):
        gap = 1
        width = 1
        self.randomize(gap=gap, width=width)

        # """
        s = time.time()
        self.selection_sort(self.bars)
        e = time.time()
        print("select:\t", e - s)
        self.completed()

        self.empty()
        time.sleep(2)
        self.randomize(gap=gap, width=width)

        s = time.time()
        self.quick_sort(self.bars, 0, len(self.bars) - 1)
        e = time.time()
        print("quick:\t", e - s)
        self.completed()
        #
        self.empty()
        time.sleep(2)
        self.randomize(gap=gap, width=width)

        s = time.time()
        self.bubble_sort(self.bars)
        e = time.time()
        print("bubble:\t", e - s)
        self.completed()

        self.empty()
        time.sleep(2)
        self.randomize(gap=gap, width=width)

        s = time.time()
        self.insertion_sort(self.bars)
        e = time.time()
        print("insert:\t", e - s)
        self.completed()

        self.empty()
        time.sleep(2)
        self.randomize(gap=gap, width=width)

        s = time.time()
        self.heap_sort(self.bars)
        e = time.time()
        print("heap:\t", e - s)
        self.completed()

        self.empty()
        time.sleep(2)
        self.randomize(gap=gap, width=width)

        s = time.time()
        self.merge_sort(self.bars)
        e = time.time()
        print("merge:\t", e - s)
        self.completed()
        # """

    # self.selection_sort(self.bars)
    # self.quick_sort(self.bars, 0, len(self.bars) - 1)
    # self.bubble_sort(self.bars)
    # self.insertion_sort(self.bars)
    # self.heap_sort(self.bars)
    # self.merge_sort(self.bars)

    # *************** SORTING ALGORITHMS ***************
    # SELECTION SORT                        ---------------
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j].height < arr[min_idx].height:
                    min_idx = j

            self.select(min_idx, "min")
            self.select(i, "i", "red")
            self.switch(min_idx, i)
            # arr[min_idx], arr[i] = arr[i], arr[min_idx]
            self.unselect("min")
            self.unselect("i")

    # BUBBLE SORT                           ---------------
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j].height > arr[j + 1].height:
                    self.select(j, "j")
                    self.select(j + 1, "j1", "red")
                    self.switch(j, j + 1)
                    self.unselect("j")
                    self.unselect("j1")

    # INSERTION SORT                        ---------------
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i].height
            j = i - 1

            while j >= 0 and key < arr[j].height:
                self.select(j + 1, "j1")
                self.select(j, "j", "red")
                self.switch(j + 1, j)
                self.unselect("j1")
                self.unselect("j")

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
            self.select(i, "i")
            self.select(largest, "l", "red")
            self.switch(i, largest)
            self.unselect("i")
            self.unselect("l")

            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            self.select(i, "i")
            self.select(0, "0", "red")
            self.switch(i, 0)
            self.unselect("i")
            self.unselect("0")

            self.heapify(arr, i, 0)

    # QUICK SORT                            ---------------
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high].height
        self.select(high, "p")

        for j in range(low, high):
            if arr[j].height <= pivot:
                i = i + 1

                self.select(j, "j", color="red")
                self.select(i, "i", color="red")
                self.switch(i, j)
                # arr[i], arr[j] = arr[j], arr[i]
                self.unselect("j")
                self.unselect("i")

        self.select(i + 1, "i1", color="red")
        self.select(high, "h", color="red")
        self.switch(i + 1, high)  # will switch bars
        # arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.unselect("i1")
        self.unselect("h")
        self.unselect("p")

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

            L = [copy.copy(iL) for iL in L]
            R = [copy.copy(iR) for iR in R]
            while i < len(L) and j < len(R):
                if L[i].height < R[j].height:
                    self.select(self.bars.index(arr[k]), "k", "red")
                    arr[k].set_height(L[i].height)
                    # arr[k] = L[i]
                    arr[k].redraw()
                    self.unselect("k")

                    i += 1
                else:
                    self.select(self.bars.index(arr[k]), "k", "red")
                    arr[k].set_height(R[j].height)
                    # arr[k] = R[j]
                    arr[k].redraw()
                    self.unselect("k")

                    j += 1

                k += 1

            while i < len(L):
                self.select(self.bars.index(arr[k]), "k", "red")
                arr[k].set_height(L[i].height)
                # arr[k] = L[i]
                arr[k].redraw()
                self.unselect("k")

                i += 1
                k += 1

            while j < len(R):
                self.select(self.bars.index(arr[k]), "k", "red")
                arr[k].set_height(R[j].height)
                # arr[k] = R[j]
                arr[k].redraw()
                self.unselect("k")

                j += 1
                k += 1

    # BUCKET SORT                           ---------------
    def bucketSort(self, arr):
        bucket = []

        for i in range(len(arr)):
            bucket.append([])

        for j in arr:
            index_b = int(10 * j)
            bucket[index_b].append(j)

        for i in range(len(arr)):
            bucket[i] = sorted(bucket[i])

        k = 0
        for i in range(len(arr)):
            for j in range(len(bucket[i])):
                arr[k] = bucket[i][j]
                k += 1

        return arr

    # RADIX SORT                            ---------------
    def counting_sort(self, arr, exp1):
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
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def radix_sort(self, arr):
        max1 = max(arr.height)

        exp = 1
        while max1 / exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10


if __name__ == "__main__":
    SortingAlgorithm()
