import pygame as pg
import numpy as np
import cv2
import argparse
from math import *
from point import *
from points import *
from spline import *

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", nargs=1, type=str, help="run spline fit on image")
parser.add_argument("-d", "--degree", nargs=1, type=int, help="degree of polynomial to fit")
args = parser.parse_args()

# parameters
img_path = "topface.jpg"
degree_of_spline = 4
gamma = 100

# set parameters from cmdlineargs
if args.image:
    img_path = args.image[0]
if args.degree:
    degree_of_spline = args.degree[0]

img = cv2.imread(img_path)
height, width, channels = img.shape 
print('Image Shape: [{}, {}]'.format(width,height))

# initalize pygame
pg.init()

# define canvas
screen = pg.display.set_mode((width, height))
background = pg.image.load(img_path)
pg.display.set_caption('Spline Image Fitting')

# initialize variables
spl_path = "splined_image.jpg"
pts = Points()
x = np.empty(0)
y = np.empty(0)
p_arr = []
LEFT = 1
RIGHT = 3
#************************************************ Main Program
running = True
while running:
    screen.blit(background, (0,0))
    mx, my = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            running = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
            pts.add_point(Point(mx, my))

        if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE and len(pts.get_nparray()) > 0:
            pts.pop_last()

        if event.type == pg.KEYDOWN and event.key == pg.K_DELETE:
            pts.clear()

        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            pts.print_points()
            if len(p_arr)>2:
                x = p_arr[:,0]
                y = p_arr[:,1]
                make_splined_image(x,y,degree_of_spline,width,gamma,img,spl_path)
                background=pg.image.load(spl_path)

    p_arr = pts.get_nparray()
    pts.draw_points(screen)   
    pg.display.flip()

