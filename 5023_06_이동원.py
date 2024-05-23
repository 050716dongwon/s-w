'''
작성일 : 2024년 5월 23일
작성자 : 202495012 이동원
설명 : readline()메소드 사용법
'''
print("== readline()메소드를 이용하여 읽기 ==")
#with open을 이용하여 읽기모드로 파일객체생성
with open("test2.txt", 'r') as f :
    #while문을 이용하여 무한 반복
    while True :        
        line = f.readline() #한 줄씩 읽어와서 변수에 저장
        print(line)
    
    
    
        if line == '' :
            break
    
    
#with open을 사용하면 f.close()를 쓸 필요가 없다