'''
    작성일 : 2024년 5월 10일
    작성자 : 컴공 202495012 이동원
    설명 : 사용자로부터 과일을 입력받아 리스트를 생성하시오.

            좋아하는 과일 5개를 입력받아 리스트에 저장
            좋아하는 과일 이름을 하나 입력하여 저장된 리스트에 있는지 없는지 판단한다
            
            리스트에 추가 => append()메소드
            찾기(포함) => in 연산자
            
            
        [알고리즘]
        1. 사용자가 입력한 과일을 저장할 리스트가 필요함 => 빈 리스트를 생성
        2. 5번 반복하면서
         2-1. 과일을 입력받아 변수에 저장
          2-2. 과일 변수에 저장된 과일을 리스트에 추가한다 => append()메소드 사용
        3. 리스트에 저장된 과일을 출력
        4. 과일 이름을 1개 입력받는다
        5. 만약 그 과일이 리스트에 있으면
         5-1. 그 과일은 당신이 좋아하는 과일입니다 출력
        6. 나머지는 
         6-1. 그 과일은 당신이 좋아하지않는 과일입니다 출력

'''

fruits = []
for i in range(5) :
    fruits_name = input(str(i+1) + ".좋아하는 과일 이름을 입력하시오 : ")
    fruits.append(fruits_name)
    
print(fruits)

print()

favorite_fruit = input("좋아하는 과일은? : ")

# 사용자가 입력한 과일이 리스트에 있는지 판단
# 만약에 입력한 과일이 과일 리스트에 있다면
if favorite_fruit in fruits :
    print(f"{favorite_fruit}는 당신이 좋아하는 과일이 맞습니다")
    
else :
    print(f"{favorite_fruit}는 당신이 좋아하는 과일이 아닙니다")