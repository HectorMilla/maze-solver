
from tkinter import TK, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = TK()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    root = TK()
    root.title = "Maze Solver"
    
    canvas = Canvas()
    canvas.pack()
    running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    

    def close(self):
        self.running = False
    

def main():

    win = Window(800,800)

    win.wait_for_close()





if __name__ == "main":
    main()