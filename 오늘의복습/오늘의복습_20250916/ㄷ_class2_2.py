# 파일 위치 : class2_02.py, class2_03.py, class2_04.py

# ! class2_04.py 둘러보기
# ! 상속개념을 활용한 다양한 예제 풀어보기

# 3] 상속개념을 활용한 예제


# 1) 상속개념을 활용한 예제 : Exception 사용
# 정수값이고 주어진 범위를 벗어나면 발행하는 Exception
class OutOfRangeError(Exception): # Exception 클래스를 부모 함수로 둔다.
    def __init__(self,strname):
        super().__init__(strname) # 부모클래스 생성자를 호출하고 자식 객체(self)에 부모 속성들을 초기화
                                  # 그래서 자식 클래스의 객체 생성 생성자에서 부모클래스 생성자를 부르고 초기화한다.
                                  
    def show_info(self): # OutOfRangeError 클래스 안에 정의된 메서드(method)
                         # 이 메서드를 호출하면, 문자열 "사용자가 정의한 예외입니다."를 반환함
        return '사용자가 정의한 예외입니다.'

try: # 오류가 발생할 가능성이 있는 코드 블록을 묶는 키워드
    number = 100
    if not 0 <= number <10:
        raise OutOfRangeError('0과 10사이를 벗어났습니다.')
    int('asdfasdf')
except OutOfRangeError as e: # try 블록에서 발생한 특정 오류를 처리하는 블록 / as 발생한 예외 객체를 변수로 받기 위해 사용
    print(e)
except ValueError as e: # try 블록에서 발생한 특정 오류를 처리하는 블록 / as 발생한 예외 객체를 변수로 받기 위해 사용
    print(e)

# 2) 상속개념을 활용한 예제 : 클래스 상속, 부모 클래스 객체생성자 호출 및 초기화, 프라이빗 변수, 데코레이션, raise, isinstance( , )

# 이전 헷갈린 부분 :
# isinstance( , )
# 클래스 인스턴스에서 클래스 메서드 호출 하는 방법

# 2)-1 클래스 정의하기
# 직원 Employee - 아이디, 이름 기본급
class Employee:
    def __init__(self,id,name,base_salary):
        self.name = name
        self.id = id
        self.base_salary = base_salary
    def __str__(self):
        return f'id : {self.id}, 이름 : {self.name}, 기본급여 : {self.base_salary}'
# 정규직 FullTimeEmployee - 보너스
class FullTimeEmployee(Employee):
    def __init__(self,id,name,base_salary,bonus_salary):
        super().__init__(id,name,base_salary)
        self.bonus_salary = bonus_salary
    def __str__(self):
        return f'id : {self.id}, 이름 : {self.name}, 기본급여 : {self.base_salary}, 보너스 : {self.bonus_salary}'
# 계약직 PartTimeEmployee - 시간당 급여, 기본급 없음
class PartTimeEmployee(Employee):
    def __init__(self,id,name,our_wage,hours):
        super().__init__(id,name,0)
        self.hour_wage = our_wage
        self.hours = hours
    def __str__(self):
        return f'id : {self.id}, 이름 : {self.name}, \
            시간당급여 : {self.hour_wage}, 일한시간 : {self.hours}'
# 인턴 Intern - 고정수당
class Intern(Employee):
    def __init__(self,id,name,fixed_wage):
        super().__init__(id,name,0)
        self.fixed_wage = fixed_wage
    def __str__(self):
        return f'id : {self.id}, 이름 : {self.name}, \
            고정급여 : {self.hour_wage}'

# 2)-2
# 정규직 직원, 계약직, 인턴을 모두 리스트에 섞어서 객체를 저장
# emp =  [
#     FullTimeEmployee(),
#     ...
#     ...
#     ...
#     ...
#     ...
#     ..
# ]

# 2)-3
# emp에 들어있는 직원이 각각 어떤 클래스인지 순환을 이용해서 판단, 각 클래스의 int,pte 메소드 호출

# 2)-4
# 다형성과 메소드 오버라이딩으로 단순화하기.