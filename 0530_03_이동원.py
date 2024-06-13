'''
작성일 : 2024년 5월 30일
작성자 : 202495012 이동원
설명 : 정수를 입력받아 그 수가 소수인지 아닌지 판단하시오
        소수를 판단하는 부분을 함수로 작성하고, 결과는 따로 돌려줍니다


[문제분석]
소수는 약수가 1과 자기자신인 수가 소수이다



[알고리즘]
1. 함수
    2)메인으로부터 값을 1개를 입력받는다
    3)count = 0
    4) 2부터 입력수까지 반복한다
        4-1) 만약 입력수와 나누는 수가 같다면
        4-2) count를 1 올린다

'''

def junsu_num(num1) :
    count = 0
    for i in range(2, num1+1) :
        if num1 % i == 0 :
            count = count + 1
            if count == 1 :
                return num1

            
num1 = int(input("정수를 입력하시오. : "))

result = junsu_num(num1)            

print(f"{result}은 소수가 맞습니다")