from tkinter import Tk, BOTH, Canvas
from draw import Point, Line


# create a window to draw widgets
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "maze solver"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__running = False
        self.__canvas.pack(fil=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
