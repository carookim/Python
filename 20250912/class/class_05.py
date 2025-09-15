# 학생
# 이름, 학생정보 출력
# 변수 : 이름
# 함수 : 학생정보를 출력

students = [] # 학생 이름 저장, 딕셔너리 형태
class StudentMng():
    def __init__(self):
        self.name = ''
        self.age = 0

    def info_student(self):
        print(f'이름 : {self.name} 나이 : {self.age}')

# def info_student(self):
#     print(f'이름 : {self.name} 나이 : {self.age}')

s1 = StudentMng()
s1.name = '홍길동'
s1.age = 25
students.append(s1)

s2 = StudentMng()
s2.name = '강태공'
s2.age = 35
students.append(s2)

# info_student(students[0])
# info_student(students[1])

students[0].info_student()
students[1].info_student()

# # 학생정보 입력
# # student 딕셔너리에 요소 추가
# def create_student(name,age):
#     return {'name' : name, 'age' : age}

# # 모든 학생 출력
# for s in students: # students 길이 만큼 반복
#     info_student(s)