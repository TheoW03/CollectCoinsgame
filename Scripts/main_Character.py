# from cmath import rect
# from curses.textpad import rectangle
import pygame


class mainChar:
    def __init__ (self,rectangle):
        self.rectangle = rectangle
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
    
