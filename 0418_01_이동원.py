'''
    [문제분석]
    초미세먼지 농도에 따른 문자메시지 발송
    좋음: 15이하
    보통: 15초과 36미만
    나쁨 : 36이상
    
    [알고리즘]
     1. 초미세먼지 농도를 측정한다.(입력받는다.)
     2. 만약 초미세먼지 농도가 15이하이면
      2-1. 좋음
     3.아니고 만약 초미세먼지 농도가 16~35이면
      3-1. 보통
     4.나머지는
      4-1. 나쁨
'''

nongdo = int(input("초미세먼지 농도를 입력하시오 : "))

if nongdo >= 0 and nongdo <=15 :
    print("오늘 초미세먼지 농도는 '좋음'입니다.")

elif nongdo >= 16 and nongdo <= 35 :
    print("오늘 초미세먼지 농도는 '보통'입니다.")
    
else :
    print("오늘 초미세먼지 농도는 '나쁨'입니다.")
    '''
    if mise < 15 :
    print("좋음")
if 15 <= mise <= 35 :  # mise >= 15 and mise <= 35
    print("보통")
if mise > 35 : 
    print("나쁨")
    
if mise < 15 :
    print("좋음")
elif 15 <= mise <= 35 :
    print("보통")
else :
    print("나쁨")
    

if mise < 15 :
    print("좋음")
elif mise <= 35 :
    print("보통")
else :
    print("나쁨")

if mise < 15 :
    print("좋음")
elif mise > 35 :
    print("나쁨")
else :
    print("보통")   
    '''