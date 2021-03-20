import random
import time
from tkinter import *


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x + width
        self.color = "#00b200"
        self.outline = "#157145"

    def __str__(self):
        return f"h:{self.height}\t| x:{self.x} | y:{self.y} | x2:{self.x2}"

    def set_color(self, color):
        self.color = color

    def set_x2(self, x2):
        self.x2 = x2


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

        self.recs = []
        self.bars = []
        self.ranints = []

        self.top_canvas = Canvas(
            self.window, width=self.width, height=50
        )  # , bg="red")
        self.bar_canvas = Canvas(self.window, width=self.width, height=500, bg="white")
        self.top_canvas.pack(side=TOP)
        self.bar_canvas.pack(side=BOTTOM)
        self.Sorting_GUI()

        self.window.mainloop()

    def sorting_completed(self):
        for i in range(len(self.bars)):
            self.bar_canvas.create_rectangle(
                self.bars[i].x,
                self.bars[i].y,
                self.bars[i].x2,
                self.bars[i].height,
                fill=self.bars[i].color,
                outline=self.bars[i].color,
                activefill="black",
            )
            self.bar_canvas.update()

    def switch_bars(self, i1, i2):
        og_x = self.bars[i1].x
        des_x = self.bars[i2].x

        rate = 1
        while self.bars[i1].x != des_x or self.bars[i2].x != og_x:
            if self.bars[i1].x < des_x:  # moves bar to right
                self.bar_canvas.move(self.recs[i1], rate, 0)  # moves i1 bar to i2
                self.bar_canvas.update()
                self.bars[i1].x += rate
                self.bars[i1].x2 += rate

                self.bar_canvas.move(self.recs[i2], -rate, 0)  # moves i2 to og_x
                self.bar_canvas.update()
                self.bars[i2].x -= rate
                self.bars[i2].x2 -= rate

            elif self.bars[i1].x > des_x:
                self.bar_canvas.move(self.recs[i1], -rate, 0)
                self.bar_canvas.update()
                self.bars[i1].x -= rate
                self.bars[i1].x2 -= rate

                self.bar_canvas.move(self.recs[i2], rate, 0)
                self.bar_canvas.update()
                self.bars[i2].x += rate
                self.bars[i2].x2 += rate

        self.recs[i1], self.recs[i2], self.bars[i1], self.bars[i2] = (
            self.recs[i2],
            self.recs[i1],
            self.bars[i2],
            self.bars[i1],
        )

    def Sorting_GUI(self):
        x1 = 0
        y1 = 2
        gap = 2
        rec_width = 1

        amount_of_bars = self.width // (rec_width + gap)

        self.ranints = [x for x in range(1, amount_of_bars + 1)]
        random.shuffle(self.ranints)

        for i in range(amount_of_bars):
            self.bars.append(Rectangle(x1, y1, rec_width, self.ranints[i]))
            x1 += rec_width + gap

        for i in range(amount_of_bars):
            self.recs.append(
                self.bar_canvas.create_rectangle(
                    self.bars[i].x,
                    self.bars[i].y,
                    self.bars[i].x2,
                    self.bars[i].height,
                    outline=self.bars[i].outline,
                    activefill="black",
                )
            )

        # self.selection_sort(self.bars)
        self.quick_sort(self.bars, 0, len(self.bars) - 1)
        self.sorting_completed()

    # _____________SORTING ALGORITHMS_____________
    # SELECTION SORT                        ---------------
    def selection_sort(self, arr):  # works, sorts bars
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx].height > arr[j].height:
                    min_idx = j

            self.switch_bars(min_idx, i)

    # QUICK SORT                            ---------------
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high].height

        for j in range(low, high):
            if arr[j].height <= pivot:

                i = i + 1
                self.switch_bars(i, j)

        self.switch_bars(i + 1, high)
        return i + 1

    def quick_sort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    SortingAlgorithm()
