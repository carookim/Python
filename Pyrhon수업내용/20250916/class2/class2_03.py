# 사용 된것 :
# 클래스 상속, 부모 클래스 객체생성자 호출 및 초기화, 프라이빗 변수, 데코레이션, raise, isinstance( , )

# 직원 Employee - 아이디, 이름 기본급
class Employee:
    def __init__(self,id,name,base_salary):
        self.id = id
        self.name = name
        self._base_salary = base_salary # private의 의미로 사용
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self,money):
        if money > 0:
            self._base_salary = money
        else :
            raise ValueError('금액은 양수입니다. 마이너스 불가')
    def __str__(self): # 출력 했을 때 무엇이나오게 할지 ^ 이 클래스에 포함된?
        return f'{self.name} : {self.id}, {self.base_salary}'
    def show_class(self):
        print('직원 클래스')
    
# 정규직 FullTimeEmployee - 보너스
class FullTimeEmployee(Employee):
    def __init__(self,id,name,base_salary,bonus): # ^
        super().__init__(id,name,base_salary)
        self.bonus = bonus
        # bonus도 마이너스 입력 불가 ^
    def __str__(self): # 출력 했을 때 무엇이나오게 할지 클래스 마다 다르게 설정? ^
        return super().__str__() + f', {self.bonus}'
    def show_class(self):
        print('정규직 클래스')

# 계약직 PartTimeEmployee - 시간당 급여, 기본급 없음
class PartTimeEmployee(Employee):
    def __init__(self,id,name,hourly_rate,hours): # 여기에 base_salary 언급이 안됬는데 괜찮은건지?
        super().__init__(id,name,0) # base_salary는 사용하지 않아 0으로 설정
        self.hourly_rate = hourly_rate
        self.hours = hours
    def __str__(self):
        return f'{self.name} : {self.id}, {self.hourly_rate}, {self.hours}'
    def show_class(self):
        print('계약직 클래스')

# 인턴 Intern - 고정수당
class Intern(Employee):
    def __init__(self,id,name,fixed_salary):
        super().__init__(id,name,0) # base_salary는 사용하지 않아 0으로 설정
        self.fixed_salary = fixed_salary
    def  __str__(self):
        return f'{self.name} : {self.id}, {self.fixed_salary}'
    def show_class(self):
        print('인턴 클래스')
    
# 문제 풀이
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
emp_1 = Employee('abc1','이순신',40000)
emp_2 = FullTimeEmployee('abc2','김유신',40000,30000)
emp_3 = PartTimeEmployee('abc3','강감찬',10030,4)
emp_4 = Intern('abc4','세종대왕',3000000)

emp = [emp_1,emp_3,emp_4,emp_2] # 임의의 여러 직원이 들어가 있는 리스트

# emp에 들어있는 직원이 각각 어떤 클래스인지 순환을 이용해서 판단, 각 클래스의 int,pte 메소드 호출

# def print_emp_classification(emp_list):
#     for emp_value in emp_list:
#         if isinstance(emp_value,FullTimeEmployee):
#             emp_value.fte()
#         elif isinstance(emp_value,PartTimeEmployee):
#             emp_value.pte()
#         elif isinstance(emp_value,Intern):
#             emp_value.int()
#         else:
#             emp_value.emp()

# print_emp_classification(emp)

# 헷갈린 부분 :
# isinstance( , )
# 클래스 인스턴스에서 클래스 메서드 호출 하는 방법

# 다형성과 메소드 오버라이딩
# 다형성 : 같은 메시지를 보내도, 객체에 따라 다르게 동작하는 능력
# 만약 클래스 메서드의 emp(),fte(),pte(),int()를 show_class()로 동일하게 이름을 지으면? ^
for e in emp:
    e.show_class() # emp 리스트의 각각의 객체에 맞는 메소드를 호출