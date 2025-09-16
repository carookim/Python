# property getter setter

# 파이썬 클래스에서 getter setter 사용법
import random
class Person:
    def __init__(self, name, age):
        self.name = name  # private 변수로 설정
        self.age = age    # private 변수로 설정
    def get_age(self):
        return self.age

p1 = Person('홍길동', 20)
print(p1.get_age())

# -----

import random
class Person:
    def __init__(self, name, age):
        self.name = name  # private 변수로 설정
        self._age = age    # private 변수로 설정
    @property # 메서드를 변수처럼 접근 가능하게 만드는 것
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value

p1 = Person('홍길동', 20)
print(p1.age) # 클래스 메소드 호출이지만 변수처럼 접근가능
p1.age = 30
print(p1.age)
del p1.age # del 변수명
print(p1.name)
del p1.name
print(p1.name)

# 함수를 변수처럼 사용하기 위해서 사용

# 사용하지않을 경우 : 값을 넣을 때마다 예외 처리 코드 작성해야 함

# Getter (값 읽기)
# private 변수 값을 읽기 위해 만든 메서드

# Setter (값 설정/수정)
# private 변수 값을 안전하게 수정하도록 만든 메서드

# private 변수,
# @property, @score.setter, @score.deleter
# 이 private 변수를 안전하게 다루기 위한 인터페이스
# private 변수 구현 @ property를 통해 접근하는 데에 제한을 둔다.

# private 변수에서 실제 보호는 강제로 하는 게 아니라
# “getter/ setter 경로를 통해서만 값이 바뀌도록 설계"하는 것



# --- 강사님 예제 ---

# 파이썬 클래스에서 getter setter 사용법

import random
class Person:
    def __init__(self, name, age):
        self._name = name  # private 변수로 설정
        self._age = age    # private 변수로 설정
    # 데코레이터를 이용한 setter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

        self.name = name
        self._age = age
    @property
    def age(self):
        return self._age

    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        self._age = age
p = Person("홍길동", 25)
print(p.name)
print(p.age)    
p.name = "김철수"
p.age = 30
    def age(self, value):
       self._age = value

p1 = Person("홍길동", 20)
print(p1.age)
p1.age = 30
print(p1.age)
print(p1.name)
del p1.name
print(p1.name) #  'Person' object has no attribute 'name'