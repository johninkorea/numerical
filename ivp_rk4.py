import numpy as np
import matplotlib.pyplot as plt

def f(t_n, y): # 미분방정식 정의
    return -y

def M4(t_n, y_n, h): #RK4
    k1=h*f(t_n, y_n)
    k2=h*f(t_n+.5*h, y_n+.5*k1)
    k3=h*f(t_n+.5*h, y_n+.5*k2)
    k4=h*f(t_n+h, y_n + k3)
    y_np1=y_n+(k1+2*k2+2*k3+k4)/6
    return y_np1

y_0, x_start, x_finsh=1, 0, 10 # 초기조건
n=1e2 # 분활 회수
x=np.linspace(x_start, x_finsh, int(n)) # 정의역 정의
h=(x_finsh-x_start)/(n-1) # 정의역 분활 간격

z=1
y_list=[y_0]
y=y_0
while z<len(x):
    y=M4(x[z], y, h)
    y_list.append(y)
    z+=1

plt.plot(x,y_list)
plt.show()
