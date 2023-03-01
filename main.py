import os
import matplotlib.pyplot as plt
import numpy as np


def path_list(path):
    li = next(os.walk(path))[2]
    li2 = []
    for l in li:
        if not l.endswith('py'):
            li2.append(path + l)
    return li2


def create_sc(x,y,path):
    li2 = path_list(path)
    li3 = []
    for li in li2:
        li3.append(plt.imread(li))
    
    return li3


def con2(x, y, path='./'):
    li2 = create_sc(x,y,path)
    h = li2[0].shape[0]
    w = li2[0].shape[1]
    bu = [np.ones_like(li2[0])]
    img_out = np.empty((h * y, w * x, li2[0].shape[2]))
    if x*y > len(li2):
        num = x*y-len(li2)
        li2.extend(bu*num)
    cont = 0
    for i in np.arange(0, h * (y - 1) + h, h):
        for j in np.arange(0, w * (x - 1) + w, w):
            img_out[i:i + h, j:j + w, :] = li2[cont]
            cont += 1
    return img_out


if __name__ == "__main__":
    y = input('输入行:')
    x = input('输入列:')
    img = con2(int(x),int(y))
    plt.imsave("./out.png", img)
