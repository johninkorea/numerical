import numpy as np

def FDD(list): # 유한 차분
    if len(list)==2: # 성분이 2개일때는 지정된 값으로 계산
        y1=dic[list[0]]-dic[list[1]]
        y2=list[0]-list[1]
        y=y1/y2
    else: # 성분이 3개 이상일때 재귀함수를 사용해서 성분이 2개일때까지 계산
        list1,list2=list[1:],list[:-1] # 재귀를 사용하기 위해 성분을 따로 저장
        y1=FDD(list1)-FDD(list2) # 분자
        y2=list[-1]-list[0] # 분모
        y=y1/y2
    return y

def asd(list, x): # 뉴턴 보간법 공식에서 다항식 부분
    list=np.array(list)
    y=x-list
    y=np.prod(y) # 모든 성분을 곱
    return y

def NFDD(list, x):
    z, s=1,dic[list[0]] # 초기값 설정
    while z<(len(list)):
        a=asd(list[:(z)], x) # 다항식 파트
        b=FDD(list[:(z+1)]) # 유한 차분 파트
        asdfass=a*b # 누적하며  항별로 덧셈
        s+=asdfass
        z+=1
    return s

# 3번으로 확인
# x_l=[-1, 1, 2, 3]
# y_l=[1, -3, -5, 1]
x_l=[0, 1.1, 2.3, 3.8, 4.5, 5.4, 5.9, 6.7, 8.4]
y_l=[1, 2, 0.5, 1.2, 1.6, 2.8, 4.7, 5.2, 4.5]

# 주어진 함수 값을 딕션어리로 저장 
# 유한 차분에서 성분이 2개일때 대응시키기 위해서
dic = dict(zip(x_l, y_l))

a=NFDD(x_l, 4.9)
print(f"f(4.9)={a}")


# 시각화
import matplotlib.pyplot as plt
x=np.linspace(0,9, 1000)
z=0
yl=[]
while z<len(x):
    y=NFDD(x_l, x[z])
    yl.append(y)
    z+=1
plt.plot(x,yl)
plt.scatter(x_l, y_l)
plt.scatter(4.9, a)
plt.show()


