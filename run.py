import random
import Sorting_Algorithms as sorts
import time
from tkinter import *


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x + width
        self.color = "#00b200"  # "ffffff" "0f4a16" "00b200"

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

    def switch_bars(self, i1, i2):

        og_x = self.bars[i1].x
        des_x = self.bars[i2].x

        while self.bars[i1].x != des_x:
            rate = 3
            time.sleep(1 / (10 ** 500))

            if self.bars[i1].x < des_x:  # moves bar to right
                self.bar_canvas.move(self.recs[i1], rate, 0)  # moves i1 bar to i2
                self.bars[i1].x += rate
                self.bars[i1].x2 += rate

                self.bar_canvas.move(self.recs[i2], -rate, 0)  # moves i2 to og_x
                self.bars[i2].x -= rate
                self.bars[i2].x2 -= rate

            else:
                self.bar_canvas.move(self.recs[i1], -rate, 0)
                self.bars[i1].x -= rate
                self.bars[i1].x2 -= rate

                self.bar_canvas.move(self.recs[i2], rate, 0)
                self.bars[i2].x += rate
                self.bars[i2].x2 += rate

            self.bar_canvas.update()

        self.recs[i1], self.recs[i2], self.bars[i1], self.bars[i2] = (
            self.recs[i2],
            self.recs[i1],
            self.bars[i2],
            self.bars[i1],
        )

    def Sorting_GUI(self):

        self.recs = []

        def bars_fill(amount=5, fill_all=False):
            x1 = 0
            y1 = 2
            gap = 2
            rec_width = 1

            if fill_all:
                amount_of_bars = self.width // (rec_width + gap)
            else:
                amount_of_bars = amount

            self.ranints = [x for x in range(1, amount_of_bars + 1)]
            random.shuffle(self.ranints)

            for i in range(amount_of_bars):
                self.bars.append(Rectangle(x1, y1, rec_width, self.ranints[i]))
                x1 += rec_width + gap

        def fill_canvas(amount_of_bars):
            for i in range(amount_of_bars):
                self.recs.append(
                    self.bar_canvas.create_rectangle(
                        self.bars[i].x,
                        self.bars[i].y,
                        self.bars[i].x2,
                        self.bars[i].height,
                        fill=self.bars[i].color,
                        outline=self.bars[i].color,
                        activefill="black",
                    )
                )

        bars_fill(100, True)
        fill_canvas(len(self.bars))

        # self.selection_sort()
        self.quickSort(self.bars, 0, len(self.bars) - 1)

    # _____________SORTING ALGORITHMS_____________
    # SELECTION SORT
    def selection_sort(self):  # works, sorts bars
        for i in range(len(self.bars)):
            min_idx = i
            for j in range(i + 1, len(self.bars)):
                if self.bars[min_idx].height > self.bars[j].height:
                    min_idx = j

            self.switch_bars(min_idx, i)

    # QUICK SORT
    def partition(self, arr, low, high):
        i = low - 1
        pivot = self.bars[high].height

        for j in range(low, high):
            if self.bars[j].height <= pivot:

                i = i + 1
                self.switch_bars(i, j)

        self.switch_bars(i + 1, high)
        return i + 1

    def quickSort(self, arr, low, high):
        if len(self.bars) == 1:
            return self.bars
        if low < high:
            pi = self.partition(self.bars, low, high)

            self.quickSort(self.bars, low, pi - 1)
            self.quickSort(self.bars, pi + 1, high)


if __name__ == "__main__":
    SortingAlgorithm()
