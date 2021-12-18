# 이 코드는 newton method를 사용해서 방정식의 해를 구해줍니다.

def f(x): # 근을 구하고자 하는 함수
    y=x**3
    return y

def df(x): # 함수의 도함수
    y=3*x**2
    return y

def newton(f, df, x1): # 뉴턴법 정의
    x2=x1
    while 1:
        x1=x1-(f(x1)/df(x1)) # 뉴턴법 점화식
        if abs(x2-x1)<1e-10: # 오차 범의 안에서 종료(x축)
            break 
        x2=x1 
    return round(x1,9)

x1=3 # 초깃값
re=newton(f, df, x1)
print(re)