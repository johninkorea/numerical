import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre


f=lambda x: np.sqrt(1+x**3)
# 기준값
r,asd=quad(f,0,2)
print("모듈을사용한 기준값")
print(r)


## 사다리꼴
a,b=0,2
n=10
h=(b-a)/n
x=np.linspace(a,b,n+1)
fx=f(x)
s=(np.sum(fx)-.5*(fx[0]+fx[-1]))*h # 공식
print("\n사다리꼴 공식")
print(f"S(n={n})= {s} : err={np.abs(s-r)}")


## 심프슨
N=int((n-2)/2)
w=np.array([1]+ [4,2]*N+ [4,1])
s=(h/3)*np.sum(np.multiply(w, fx))
print("\n심프슨 공식")
print(f"S(n={n})= {s} : err={np.abs(s-r)}")


## 가우스
m=(2)/(b-a)
ff=lambda x: f((x+1)/m+a) # 새로운 함수 정의
n=1
print("\n가우스 수치적분")
while n<6:
    x,w=roots_legendre(n)
    s=np.sum(np.multiply(w,ff(x)))*(1/m)
    print(f"S(n={n})= {s} : err={np.abs(s-r)}")
    n+=1

