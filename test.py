# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from tkinter import *
import time


class alien(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.alien1 = self.canvas.create_oval(
            20, 260, 120, 360, outline="white", fill="blue"
        )
        self.alien2 = self.canvas.create_oval(2, 2, 40, 40, outline="white", fill="red")
        self.canvas.pack()
        self.animation()
        self.root.mainloop()

    def animation(self):
        track = 0
        while True:
            x = 5
            y = 0
            if track == 0:
                for _ in range(50):
                    time.sleep(0.025)
                    self.canvas.move(self.alien1, x, y)
                    self.canvas.move(self.alien2, x, y)
                    self.canvas.update()
                track = 1

            else:
                for _ in range(50):
                    time.sleep(0.025)
                    self.canvas.move(self.alien1, -x, y)
                    self.canvas.move(self.alien2, -x, y)
                    self.canvas.update()
                track = 0


alien()