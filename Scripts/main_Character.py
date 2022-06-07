# from cmath import rect
# from curses.textpad import rectangle
# from curses.textpad import rectangle
from cmath import rect
import re
import pygame


class mainChar:
    def __init__ (self,rectangle,scale=None):
        self.rectangle = rectangle
        if scale:
            self.scale = scale
    # def __init__(self,rectangle,scale):
    #     self.rectangle = rectangle
        
    def setVelocity(self,vel):
        self.vel = vel
    def move_up(self):
        self.rectangle.y -= self.vel
    def move_down(self):
        self.rectangle.y += self.vel
    def move_right(self):
        self.rectangle.x += self.vel
    def move_left(self):
        self.rectangle.x  -= self.vel
    def getRectangle(self):
        return self.rectangle
    def getVector(self):
        return ((self.rectangle.x, self.rectangle.y))
    def getX(self):
        return self.rectangle.x
    def getY(self):
        return self.rectangle.y
    def setVector(self,x,y):
        self.rectangle.x = x
        self.rectangle.y = y
    def getScale(self):
        return self.scale
    
