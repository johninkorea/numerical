# 이 코드는 newton method를 사용해서 방정식의 해를 구해줍니다.
import numpy as np

def f(x):
    y=x**2-1
    return y

def xnp1(x1,x2):
    if np.abs(f(x2)-f(x1))<1e-5:
        x3=100
    else:
        x3=x2-f(x2)* (x2-x1) / (f(x2)-f(x1))
    return x3

def falsem(f, list):
    sss=list[:]
    n=0
    while True:
        x3=xnp1(sss[0],sss[1])
        if x3==100:
            break
        if np.sign(f(x3))*np.sign(f(sss[1]))==0: break
        elif np.abs(sss[1]-x3)<1e-10: break

        if np.sign(f(sss[0]))*np.sign(f(sss[1]))<0:
            sss[1]=x3
        elif np.sign(f(sss[0]))*np.sign(f(sss[1]))>0:
            sss[0]=x3
        n+=1
    return round(x3,9)

list=[0, 3]
re=falsem(f, list)
print(re)