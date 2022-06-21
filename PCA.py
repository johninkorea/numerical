import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)


# data 만들기
N=int(1e1)
x=np.linspace(0,5,N)
y=x+np.random.randn(N)*.3
data=np.array([x,y]).T



def PCA(data,dim): # 인풋 데이터와 최종 차원을 input으로 입력
    M=np.mean(data, axis=0) # 평균
    C=np.copy(data-M) # 중심을 원점으로
    V=np.cov(C.T) # cov 행열 연산

    # eigen 값들 찾기
    eval,evec=np.linalg.eig(V)
    evec=evec.T #   보기 편하게 전치했음

    asd=eval.argsort()[::-1] # eigen value(분산)가 큰 순으로 정리
    eval,evec=eval[asd],evec[asd]

    z,re=0,[]
    while z<dim: # 정해진 차원만큼 포인트를 eigen vector로 projection한 변위 계산
        v=np.copy(evec[z])
        asd=np.dot(v,C.T)/np.dot(v,v)
        re.append(asd)
        z+=1
    re=np.array(re).T
    return re, evec[:dim],C # 그림 드릴 경우를 위해서 eigen vector도 출력



re=PCA(data,1)
print(re[1])
print(re[0])

# 그림 그리기
qwe,=re[1]
C=re[2]
r=qwe[1]/qwe[0] # 기울기
x=np.linspace(np.min(C[:,0]),np.max(C[:,0]),100) # 정의역
y1=r*x

z=0
project=np.ones_like(C) # 변위에 벡터를 곱해 포인트를 잡는 반복문
while z<len(project):
    project[z]=re[0][z]*re[1]
    z+=1

plt.plot(x,y1)
plt.scatter(C[:,0],C[:,1],s=10,c="b")
plt.scatter(project[:,0],project[:,1],c="r",marker="x",s=20)
plt.axis('square')
plt.show()