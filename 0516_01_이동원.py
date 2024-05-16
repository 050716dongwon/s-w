'''
    작성일 : 2024년 5월 16일
    작성자 : 컴공 202495012 이동원
    설명 : 아래와 같이 두개의 튜플을 만들고,
            튜플로부터 하나의 리스트를 작성하는 프로그램을 만드시오.
'''

fruits = ('사과', '배', '파인애플', '포도')
price = (5000, 7000, 4500, 6000)

#저장할 빈 리스트를 생성
fp_list = []
#fp_tuple = ()
for i in range(len(fruits)) :       #튜플의 길이만큼 반복하면서
    fp_list.append(fruits[i])
    fp_list.append(price[i])
    #fp_tuple.append(fruits[i])
    #fp_tuple.append(price[i])
print("과일 목록 : ", fruits)
print("과일 가격 : ", price)
print("과일별 가격 리스트 : ", fp_list)




