import numpy as np
import matplotlib.pyplot as plt

def lagrange1 (list, x): # 여러항을 곱하는 함수 정의
    list=np.array([list])
    L=np.prod(x-list)
    return L

# make list of lagrange inerpolation basis function
def lagrage2(x_l, x): 
    L=[]
    z=0
    while z<len(x_l):
        x1=x_l[:]
        del x1[z]
        L1=lagrange1(x1, x)/lagrange1(x1, x_l[z])
        L.append(L1)
        z+=1
    return L

def lagrage(list, y_l, X): # define lagrange's furmula
    L1=np.array(lagrage2(list, X))
    re=y_l*L1
    re=np.sum(re)
    return re

# 주어진 좌표들
x_l=[0, 1.1, 2.3, 3.8, 4.5, 5.4, 5.9, 6.7, 8.4]
y_l=[1, 2, 0.5, 1.2, 1.6, 2.8, 4.7, 5.2, 4.5]

a=lagrage(x_l, y_l, 4.9)
print(f"f(4.9)={a}")



# 시각화
x=np.linspace(0,9, 1000)
z,yl=0,[]
while z<len(x):
    y=lagrage(x_l, y_l, x[z])
    yl.append(y)
    z+=1
plt.plot(x,yl)
plt.scatter(x_l, y_l)
plt.scatter(4.9, a)
plt.show()
