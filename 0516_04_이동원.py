'''
    작성일 : 2024년 5월 16일
    작성자 : 컴공 202495012 이동원
    설명 : 로또 번호 만들기
   
    로또는 1에서 45까지의 6개의 번호입니다
    로또 번호를 생성하고 로또번호를 오름차순으로 정렬하시오
     
'''

import random

print("로또 번호 생성")

lotto = list()  #빈 리스트 생성

i = 0 #랜덤수 발생 횟수 저장
while True :
    lotto.append(random.randint(1,45))
    i += 1
    if len(lotto) == 6 :
        break
print("이번주 로또번호 : ", sorted(lotto))

print("세트로 생성")

lotto = set()   #빈 세트를 생성
i = 0
while True :
    lotto.add(random.randint(1,45))
    i += 1
    if len(lotto) == 6 :
        break
print("이번주 로또번호 : ", sorted(lotto))




