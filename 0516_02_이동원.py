'''
    작성일 : 2024년 5월 16일
    작성자 : 컴공 202495012 이동원
    설명 : 다음과 같은 튜플을 생성하고, 
            각 요소(숫자)의 튜플에 몇개의 있는지 출력하시오.
            len(), count(), 0번지부터
            
            개수를 칮은 숫자는 리스트에 따로 저장
            이미 찾은 숫자는 또 개수를 찾을 필요가 없다
'''
num = (1,2,3,4,1,2,3,4,1,2,3,4)
print("생성된 튜플 : ", num)

num_list = []

for i in range(len(num)) :
    print(num[i] ,"의 개수", num.count(num[i]))
    # 중복된 숫자의 개수가 다 출력된다
    
print()
print('중복제거하고 개수 찾기')

for i in range(len(num)) :
    if num[i] in num_list :        #숫자가 리스트에 있으면
        continue                #돌아가시오. 반복의 처음으로
        
    else :
        print(num[i] ,"의 개수", num.count(num[i]))
        num_list.append(num[i])
        
print()
print("없으면")
num_list = [] #다시 초기화
for i in range(len(num)) :
    if num[i] not in num_list :
        print(num[i] ,"의 개수", num.count(num[i]))
        num_list.append(num[i])
        

        





