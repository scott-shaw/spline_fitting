import numpy as np

class Points(object):

    def __init__(self):
        self.points = []

    def add_point(self, point):
       self.points.append(point)

    def draw_points(self, screen):
       for p in self.points: p.draw_point(screen)

    def get_nparray(self):
       return np.array([p.get_nparray() for p in self.points])

    def print_points(self):
       print(self.get_nparray())

    def pop_last(self):
       self.points.pop(len(self.points)-1)

    def clear(self):
       self.points = []

