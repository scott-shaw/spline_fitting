import pygame as pg
import numpy as np

class Point(object):

    def __init__(self, x, y, color=(0,255,0), radius=3):
        self.x = round(x)
        self.y = round(y)
        self.color = color
        self.rad = radius

    def draw_point(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.rad)

    def print_point(self):
        print(np.array([self.x, self.y]))

    def get_nparray(self):
        return np.array([self.x, self.y])

