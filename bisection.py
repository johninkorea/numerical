# 이 코드는 bisection method를 사용해서 방정식의 해를 구해줍니다.

import numpy as np

def f(x): # 근을 구하고자 하는 함수
    y=x**3
    return y

def bisection (fun, s, f): # 이분법 정의
    n=0
    if (fun(s)*fun(f))>0:  # 근을 구할수 없을때
        print("이분법을 사용할 수 없음.")
    else:
        while 1:
            n+=1
            m=(s+f)/2
            err1=np.abs((s+f)/2-f) #x축으로의 오차
            err2=np.abs(fun(m)) #y축으로의 오차
            if (err1<1e-10) or (err2<1e-10): # x축으로의 오차만 활용
                break # 오차 법이 안에서 종료
            elif (np.sign(fun(s))*np.sign(fun(m)))<0:f=m # 근이 오른쪽에있을때
            elif (np.sign(fun(m))*np.sign(fun(f)))<0:s=m # 근이 왼쪽에있을때
    return round(m, 9)


a,b=-1,1 # 초깃값
re=bisection(f, a, b)
print(re)