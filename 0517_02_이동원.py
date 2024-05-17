'''
    작성일 : 2024년 5월 17일
    작성자 : 컴공 202495012 이동원
    설명 : 5명의 학생 정보를 입력 받는다
            이름과 전화번호를 입력받는다
'''

#빈 딕셔너리를 생성
phone = {}

for i in range(5) :
    name = input(str(i+1) + "번째의 이름을 입력하시오. : ")
    phone_num = input(str(i+1)+"번째 학생의 전화번호를 입력하시오 : ")
    phone[name] = phone_num

print(phone)


#학생 정보 출력

for name, phone_num in phone.items() :
    print(name, ":", phone_num)
    

#학생 검색
#학생 이름을 검색하면 해당 학생의 전화번호를 출력하시오
#만약 학생이름이 없으면 입력한 학생의 전화번호가 없습니다

while True :
    name = input("찾고싶은 학생의 이름을 입력하세요. : ")
    if name == '0' :
        print("프로그램을 종료합니다")
        break
    else :
        if name not in phone.keys() :
            print("입력한 학생의 정보가 없습니다")
        
        else :
            print(name, ":", phone[name])
    
    
    
    
    
    
    
    
    
    
