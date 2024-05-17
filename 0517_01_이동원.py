'''
    작성일 : 2024년 5월 17일
    작성자 : 컴공 202495012 이동원
    설명 : 키와 값을 가지는 딕셔너리
    
    문자열 = " "  튜플 = ()     리스트 = [] => 순서가 없다
    세트 = {}       딕셔너리 = {key : value}    => 순서가 없다
'''
#빈 딕셔너리 생성
phone_book1 = {}    # 빈 세트와 동일

#딕셔너리에 값 저장 -> 1) key, value => [key] = value
phone_book1['이동원'] = '010-3054-7116'
print(phone_book1)

#빅셔너리에 갑 저장 -> 2) {key, vlaue}
phone_book2 = {'이동원' : '010-3054-7116', '홍길동' : '010-1111-1111'}
print(phone_book2)

#빈 딕셔너리 생성
phone_book3 = {}

# 5명의 이름과 전화번호 저장
phone_book3['이동원'] = '010-1111-1111'
phone_book3['개동원'] = '010-1111-1111'
phone_book3['개개동원'] = '010-1111-1111'
phone_book3['홍길동'] = '010-1111-1111'
phone_book3['개길동'] = '010-1111-1111'

print(phone_book3)
print("phone_book3의 모든 key를 출력", phone_book3.keys())
print("phone_book3의 모든 value를 출력", phone_book3.values())
print("phone_book3의 모든 keydhk vlaue를 출력", phone_book3.items())


print("모든 전화번호부의 모든 내용을 출력")
for name, phone_num in phone_book3.items() :
    print(name, ":", phone_num)
    
print()

print('전화번호의 key로 접근하여 출력')
for key in phone_book3.keys() :
    print(key, ':', phone_book3[key])       #해당 키의 value를 찾아준다
    
print()

person_dict = {'name' : '이동원', 'age' : 20, 'class' : '1학년'}

#딕셔너리로 'name'키로 값을 조회해 출력
print("name :", person_dict['name'])


#딕셔너리 'age'키로 값을 출력
print("age :", person_dict['age'],'세')

print()

#딕셔너리의 키를 기준으로 정렬 = phone_book3
print("phon_book3 정렬")
print(sorted(phone_book3))

print("키를 기준으로 전체 정렬")
sorted_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])   #key기준
print(phone_book3)

print("값를 기준으로 전체 정렬")
sorted_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])   #value기준
print(phone_book3)

print()

print("항목삭제")
del phone_book3['이동원']
print(phone_book3)

print("전체 삭제")
phone_book3.clear()
print(phone_book3)

dict1 = {1:'one', 2 : 'two', 3 : 'three'}
print("사전1 : ", dict1)

print("사전의 모든 키")
for num in dict1.keys() :
    print(num, end=' ')

print()
print("사전의 모든 값을 출력")

for alpanum in dict1.values() :
    print(alpanum, end=' ')

print()

# 1은 영어로 one
# 2는 영어로 two
# 3은 영어로 three

for num1, alpanum in dict1.items() :
    print(num1,'는 영어로',alpanum)



