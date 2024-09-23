from tkinter import Tk, BOTH, Canvas
from window import Window
from draw import Point, Line, Cell


class Maze():
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

    def _create_cells(self):
        self._cells = []

        for i in range(0,self.num_cols):
            self._cells[i] = []
            for j in self.num_rows:
                self._cells[i].append(Cell(self.win))
            self._draw_cells(self.cells[i],j)
        
    def _draw_cells(self,i,j):
        
        for cell in range(0,i):
            top_lef_point = Point(self.x1 + cell, self.y1 + j)
            bottom_right_point = Point(self.x1 + (cell + self.cell_size_x), self.y1 +(cell + self.cell_size_y))
            cell.draw(top_lef_point,bottom_right_point)
            self._animate()
    
    def _animate(self):
        
    

