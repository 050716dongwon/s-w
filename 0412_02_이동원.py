'''
     작성일 : 2024년 4월 12일
     작성자 컴퓨터공학과 202495012 이동원
     설명 : 반복문 for와 range()함수의 사용법
'''

#range()함수는 범위에서 순차적인 값을 제공한다

#자기이름 10개 출력하기
# 0~9까지 1씩 증가하는 값을 i변수에 저장하여 반복하시오.
for i in range(10) :
    print(f"{i}.이동원")


for i in range(1, 11) :
    print(f"{i}.이동원")


# 아래 그림과 같이 출력되도록 코드를 작성하시오.
'''
♥
♥♥
♥♥♥
♥♥♥♥
♥♥♥♥♥

'''

for i in range(1,6) :
    print("♥ " * i)
    
print("-------------------")
for i in range(5) :
    print("♥ " * (i + 1))

        
