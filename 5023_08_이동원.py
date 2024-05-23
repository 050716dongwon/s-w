'''
작성일 : 2024년 5월 23일
작성자 : 202495012 이동원
설명 : readlines()메소드 사용법 - 반복문으로 출력하기
'''
print("== readlines()메소드를 이용하여 읽기 ==")


#with open을 이용하여 읽기모드로 파일객체생성
with open("test2.txt", 'r') as f :
    # 파일에 있는 모든 줄을 하나의 리스트로 만든다
    textlist = f.readlines()
    
    
    for line in textlist :
        print(line)
 
 
    
#with open을 사용하면 f.close()를 쓸 필요가 없다