import numpy as np


def f(x):
    y=np.sin(x)
    return y

def newton(f, df, x1): # 뉴턴법 정의
    n=0
    x2=x1
    while 1:
        n+=1
        x1=x1-(f(x1)/df(x1)) # 뉴턴법 점화식
        if abs(x2-x1)<1e-10: # 오차 범의 안에서 종료(x축)
            break 
        x2=x1 
    return round(x1,9), n