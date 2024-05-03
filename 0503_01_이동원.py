'''
    작성일 : 2024년 5월 3일
    작성자 : 202495012 이동원
    설명 : 시퀀스 자료형
'''

#문자열
name = '이동원' #문자열을 변수에 저장
city = ['서울시', 800, '부산시', 400] #리스트 생성

num = (100, 200, 300, 400)  #튜플 생성

'''
1.인덱싱 : 순차적인 자료구조에 인덱스(첨자)의 값을 
            가지고 접근할 수 있는 기능
            [i] => i번째의 값
'''

surname = name[0]   #name 무낮열에서 첫 번째 문자를 변수에 저장
print("name[0] : ", surname)

print("city[-2] : ", city[-2]) #리스트 city에서 마지막에서 두번째 요소 출력

#리스트의 마지막에서 네번째 요소의 값을 변경
city[-4] = '서울특별시'
print("city : ", city)
#print("city[5] : ", city[5])    # 리스트의 6번쨰 값을 출력 -> 오류 발생
                                # IndexError: list index out of range
                               
'''
2.슬라이싱 : 시퀀스 자료형에서 일부를 잘라내어 동일한 자료형으로
                반환하는 기능
                
[start : stop : step] => start에서 시작해서 stop이전까지 step간격으로 추출                
                
'''
#문자열의 1부터 2까지 잘라서 변수에 저장
giveName = name[1 : 3]
print("name[1:3]", giveName)    #성뺴고 이름만 출력된다

#리스트의 세번째 요소부터 끝까지 출력
print("city[2:] : ", city[2:])

#튜플의 두번쨰 요소부터 세번째요소까지 출력
print("num[1:3]", num[1:3])

#튜플의 처음부터 끝까지 2씩 증가하면서 슬라이싱
print("num[::2]", num[::2])
#인덱스 범위가 벗어났다. 하지만 가능한 값들만 자동 슬라이싱한다.
print("num[-10:10]", num[-10:10]) 

'''
3.연결 : +연산자를 이용하여 두 개의 자료를 연결한다
        새로운 시퀀스 자료형을 만든다
자료형 + 자료형
'''
text1 = 'I like'
text2 = text1 + 'Python Language'   #문자열 + 문자열
print("text1 + 문자열 : ", text2)
num1 = (1, 2, 3, 4, 5)
num2 = (6, 7, 8, 9)

num = num1 + num2       #튜플 + 튜플
print("num1 + num2 = ", num)

#city(리스트) + num1(튜플)
#result = city + num1 # 오류 발생. 서로다른 자료형은 합칠 수 없다.
#print(result)


'''
4.반복 : * 연산자 사용한다
            시퀀스 자료형을 원하는 만큼 반복시킬 수 있는 기능.
자료형 * 반복횟수
'''
#튜플생성
language = ('C', 'JAVA', 'PYTHON')
languages = language * 3
print(languages)

feel = 'happy' * 10
print('feel : ', feel)
country = ['대한민국'] * 10
print(country)

'''
5. 멤버 유무 검사 : 시퀀스 자료형에 특정 자료가 있는지 알려주는 기능
자료 in 자료형
'''
color = ['red', 'green', 'blue', 'yellow']
print("리스트에 'black'이 있나요?", 'black' in color)
print("리스트에 'red'이 있나요?", 'red' in color)

text3 = 'Python'
print("'t'가 문자열에 있나요?", 't' in text3)
print("'p'가 문자열에 있나요?", 'p' in text3)
print("'P'가 문자열에 있나요?", 'P' in text3)

# in 연산자는 for반복문에 효율적으로 사용
for i in text3 :    # text3 안에 있는 문자를 하나씩 i 변수에 넣어서  반복
    print(i)


'''
6.길이 정보 : 내장함수 len()을 사용한다
                시퀀스 자료형의 길이를 알아볼 수 있다 
len(자료형)
'''
#문자열 text2의 길이
print("text2의 길이 : ", len(text2)) # 21 => 띄어쓰기도 포함
#리스트의 길이
print("city의 길이 : ", len(city))
