# 직원 Employee - 아이디, 이름 기본급
class Employee:
    def __init__(self,id,name,base_salary):
        self.id = id
        self.name = name
        self.base_salary = base_salary
    def __str__(self):
        return f'{self.name} : {self.id}, {self.base_salary}'
# 정규직 FullTimeEmployee - 보너스
class FullTimeEmployee:
    def __init__(self,bonus):
        self.bonus = bonus
# 계약직 PartTimeEmployee - 시간당 급여
class PartTimeEmployee:
    def __init__(self):
# 인턴 Intern - 고정수당