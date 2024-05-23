'''
작성일 : 2024년 5월 23일
작성자 : 202495012 이동원
설명 : 학생들의 점수의 평균을 출력하시오

        
        [알고리즘]
        1.학생의 이름과 성적을 불러올 파일객체를 만든다
        2.반복하면서 읽어오기
         2-1.점수에 대해 평균을 계산한다
            (합계계산을 하고 /3을 하여 출력한다)
            => 홍길동의 평균 성적 : 00점
         with open()사용하기
         
         읽기모드 -> r
         파일 읽기 = readline() => while True사용
'''


with open('student.txt', 'r') as f :
    while True :
        student = f.readline()
        
        
        
        if student == '' :
            break
        
        #빈칸을 기준으로 빈 리스트를 생성
        studentlist = student.split()
        
        #첫번째 항목을 name변수에 저장
        name = studentlist[0]
        
        # 1번지부터 3번지까지 합계 계산
        sum = 0
        for i in range(1,4) :
            sum += int(studentlist[i])
            
        average = sum / 3
        print(f"{name}학생의 평균성적 : {average:2f}")