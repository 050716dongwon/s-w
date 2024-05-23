'''
작성일 : 2024년 5월 23일
작성자 : 202495012 이동원
설명 : for문을 이용하여 읽어오기
'''
print("== for문을 이용하여 읽기 ==")
#with open을 이용하여 읽기기모드로 파일객체생성



with open("test2.txt", 'r') as f :
    for line in f :     #for문에 파일 객체를 지정하여 한 줄씩 반복하여 읽어온다
        print(line)
    
#with open을 사용하면 f.close()를 쓸 필요가 없다