'''
    작성일 : 2024년 5월 10일
    작성자 : 컴공 202495012 이동원
    설명 : 튜플 => 한 번 저장되면 그 값을 고칠 수 없는 자료형
'''

colors1 = ('red', 'blue', 'orange', 'green')

print("colors1 = ", colors1)

#인덱싱과 슬라이싱은 문자열이나 리스트오 동일하게 동작한다

print("색상중 2,3,4번째의 색은 : ", colors1[1:4])
print("색상 거꾸로 출력 : ", colors1[::-1])

# +,-연산자 사용이 가능함
colors = colors1 + colors1
print("colors = ", colors)
print("colors * 10 = ", colors * 10)

# colors1에 'black'추가
# 튜플은 추가, 삭제 안됨 => 오류발생
#colors1.append('black')
#print(colors)


print()
print()
print()
print()



colors2 = ('red', 'blue', 'orange', 'green', 'pink', 'white', 'white')
print(colors2.count('white'))
print(colors2.index('green'))
#print(colors2.find('green'))  # 튜플은 find를 사용이 불가능함

#튜플은 생성후에 변경될 수 없는 자료형이여서
#사용되는 메소드가 2개이다. count, index
















