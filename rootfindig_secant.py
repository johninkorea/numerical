# 이 코드는 newton method를 사용해서 방정식의 해를 구해줍니다.
import numpy as np

def f(x):
    y=x**3
    return y

def secant(f, x1,x2): # 할선법 정의
    n=0
    while True:
        n+=1
        x_n=x2-f(x2)* (x2-x1) / (f(x2)-f(x1))
        if x_n<-10 or x_n>3.5:
            x_n=100
            break
        x1=x2
        x2=x_n
        if np.abs(x1-x2)<1e-10: break
    return round(x_n,9)


re=secant(f, 100, 1)
print(re)