import numpy as np
import scipy
import scipy.linalg
import cv2

def get_system(x,y,k,gamma=100):
    x = x/gamma
    y = y/gamma
    A = np.array([x**i for i in range(k+1)]).T
    return scipy.linalg.solve(A.T@A,A.T@y) 

def spline(coes,x):
    return sum([coes[i]*(x**i) for i in range(len(coes))])

def make_splined_image(x,y,dos,width,gamma,img,spl_path='splined_image.jpg'):
    coes=get_system(x,y,dos)

    x_plot=np.linspace(1,width,width)
    y_plot=[]
    for xi in x_plot:
        y_plot.append(spline(coes,xi/gamma)*gamma)

    draw_points = (np.asarray([x_plot, y_plot]).T).astype(np.int32)
    cv2.polylines(img, [draw_points], False, (0,0,255))  # args: image, points, closed, color

    cv2.imwrite(spl_path, img)
