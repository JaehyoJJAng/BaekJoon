from typing import List
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

param = input().split()

def Add(param:List[str])-> None:
    A,B = map(int,param)
    print(A + B)

def Minus(param:List[str])-> None:
    A,B = map(int,param)
    print(A - B)

def Multi(param:List[str])-> None:
    A,B = map(int,param)
    print(A * B)

def division(param:List[str])-> None:
    A,B = map(int,param)
    print(A // B)
    
def Remainder(param:List[str])-> None:
    A,B = map(int,param)
    print(A % B)

Add(param=param)
Minus(param=param)
Multi(param=param)
division(param=param)
Remainder(param=param)

# 위 방법도 통과는 하나 처리 시간이 너무 오래걸림 , 평균 150ms
# seperate 옵션 응용
A,B = map(int,input().split())
print(A+B ,  A-B , A * B , A // B , A % B , sep='\n')