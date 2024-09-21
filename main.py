from tkinter import Tk, BOTH, Canvas
from window import Window
from draw import Point, Line, Cell


def main():

    win = Window(800, 800)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(125, 125, 200, 200)
    c.draw_move(c1, True)
    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    win.wait_for_close()


if __name__ == "__main__":
    main()
