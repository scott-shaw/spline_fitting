import numpy as np
import scipy
import scipy.linalg
import cv2

def least_squares(x,y,k,gamma=100):
    x = x/gamma
    y = y/gamma
    A = np.array([x**i for i in range(k+1)]).T
    return scipy.linalg.solve(A.T@A,A.T@y) 

def qr_factorization(x,y,k,gamma=100):
    x = x/gamma
    y = y/gamma
    A = np.array([x**i for i in range(k+1)]).T
    Q, R = scipy.linalg.qr(A)
    R_hat = R[0:k+1,0:k+1]
    d=(Q.T).dot(y)
    d=d[0:k+1]
    c=scipy.linalg.solve(R_hat,d)
    print('QR factorization: {}'.format(c))

def spline(coes,x):
    return sum([coes[i]*(x**i) for i in range(len(coes))])

def make_splined_image(x,y,dos,width,gamma,img,spl_path,path_type):
    coes=least_squares(x,y,dos,gamma)
    print('least squares: {}'.format(coes))
    qr_factorization(x,y,dos,gamma)

    x_plot=np.linspace(1,width,width)
    y_plot=[]
    for xi in x_plot:
        y_plot.append(spline(coes,xi/gamma)*gamma)

    draw_points = (np.asarray([x_plot, y_plot]).T).astype(np.int32)
    cv2.polylines(img, [draw_points], False, (0,0,255),5)  # args: image, points, closed, color

    cv2.imwrite(spl_path+str(dos)+path_type, img)
