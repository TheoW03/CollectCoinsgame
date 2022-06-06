# from cmath import rect
# from curses.textpad import rectangle
import pygame


class mainChar:
    def __init__ (self,rectangle):
        self.rectangle = rectangle
    def move_up(self):
        self.rectangle.y += 1
    def move_down(self):
        self.rectangle.y -= 1
    def move_right(self):
        self.rectangle.x += 1
    def move_left(self):
        self.rectangle.x  -= 1
    def getRectangle(self):
        return self.rectangle
    def getVector(self):
        return ((self.rectangle.x, self.rectangle.y))
    def getX(self):
        return self.rectangle.x
    def getY(self):
        return self.rectangle.y
    
