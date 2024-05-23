'''
작성일 : 2024년 5월 23일
작성자 : 202495012 이동원
설명 : 학생정보가 입력된 파일의 내용을 출력하시오

        
        [알고리즘]
        1.학생의 이름과 성적을 불러올 파일객체를 만든다
        2.반복하면서 읽어오기
         2-1.출력하기
         
         with open()사용하기
         
         읽기모드 -> r
         파일 읽기 = readline() => while True사용
'''

with open('student.txt', 'r') as f :
    while True :
        line = f.readline()
        print(line)
        
        
        if line == '' :
            break