from tkinter import Tk, BOTH, Canvas
from window import Window
from draw import Point, Line


def main():

    win = Window(800, 800)
    point1, point2 = Point(10, 10), Point(200, 200)
    line = Line(point1, point2)
    win.draw(line, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()
