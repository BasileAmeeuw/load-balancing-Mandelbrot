from PIL import Image
import numpy as np
import requests
import matplotlib.pyplot as plt

import requests as req

resp = req.get("http://localhost:8080/mandelbrot?real=1.000001&imag=1&max_steps=1000")

result=resp.text.split(', ')
# print(result[0])
# print(result[1])

(i,j)=(0,0)
def xrange(x):
    return iter(range(x))

cgX_s=0,2867683-1.2
cgX_e=0,2867683+1.2

def mandelbrot(real_limit=(cgX_s,cgX_e),real_length=1000,imag_limit=(-0.9,0.9),imag_length=1000,treshold=1000):
    realAxis = np.linspace(real_limit[0],real_limit[1], real_length)
    imaginaryAxis = np.linspace(imag_limit[0], imag_limit[1], imag_length)
    realAxisLen = len(realAxis)
    imaginaryAxisLen = len(imaginaryAxis)
    atlas = np.empty((real_length, imag_length))
    i=0
    for ix in xrange(realAxisLen):
        for iy in xrange(imaginaryAxisLen):
            i+=1
            cx = realAxis[ix]
            cy = imaginaryAxis[iy]
            # c = complex(cx, cy)
            getReq="http://localhost:8080/mandelbrot?real="+str(cx)+"&imag="+str(cy)+"&max_steps="+str(treshold)
            resp=req.get(getReq)
            result=resp.text.split(', ')
            if result[0]!="2":
                print(result[0])
                print(result[1])
                print(i)
            atlas[ix, iy] = result[0]
            pass
        pass

    plt.imshow(atlas.T, interpolation="nearest")
    plt.show()

mandelbrot(real_limit=(-1.5,-0.5),real_length=10000,imag_length=10000,imag_limit=(-1,0),treshold=120)
# while (i,j)<(1,1):
#     print("ok")
#     i+=0.5
#     j+=0.5
#     print((i,j))



# w, h = 512, 512
# data = np.ones((h, w, 3), dtype=np.uint8)*200
# data[256, 256] = [25, 38, 56]
# img = Image.fromarray(data, 'RGB')
# img.save('my.png')
# img.show()