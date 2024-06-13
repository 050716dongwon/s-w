'''
    학번을 입력받아 어느 학과 학생인지 알려주세요.
    학번은 학과 코드 영문자와 숫자로 구성되어 있습니다.

    예) C202095001
    [학과 코드]
    C : 컴퓨터공학과  A : 인공지능공학과   F : 식품영양학과

    입력받는 학과코드는 대소문자를 구분하지 않습니다.
    학과를 알려주는 부분은 함수로 작성하세요.

    [출력 결과]
        [학과 코드]
         C : 컴퓨터공학과 , A : 인공지능공학과, F : 식품영양학과
        학번을 입력하세요 : c202095001 
        c202095001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : A202045001
        A202045001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : s202036001
        해당 학과는 없습니다.
'''

def Dept(student_num) :
    if 'c' in student_num or 'C' in student_num :
        print(student_num, '학생은 컴퓨터 공학과 소속입니다')
        
    elif  'a' in student_num or 'A' in student_num :
        print(student_num, '학생은 인공지능 공학과 소속입니다')
        
    elif 'f' in student_num or 'F' in student_num :
        print(student_num, '학생은 식품영양학과 소속입니다')
    else :
        print("해당 학과는 없습니다.") 

student_num = input("학번을 입력하시오 : ")
Dept(student_num)

#시작하는 문자가 c면 
#startswitch(시작하는 문자)
#endswitch(끝나는 문자)
def tt(id_num) :
    if id_num.startswith("c") == True or id_num.startswith("C") == True :
        print("컴퓨터 공학부 소속입니다.")
    if id_num.startswith("F") == True or id_num.startswith("f") == True :
        print(" 식품영양학과 소속입니다.")
    if id_num.startswith("A") == True or id_num.startswith("a") == True :
        print("인공지능공학과 소속입니다.")


id_num = input("학번을 입력하시오 : ")
tt(id_num)
