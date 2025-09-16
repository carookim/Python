# 파일 위치 : class_9.py

# 3] isinstance() 함수

# isinstance() 함수
# - 객체가 어떤 클래스의 인스턴스인지 확인하는 함수
# - isinstance(객체,클래스) -> True/False 반환

# 사용하는 이유 :
# 1) 타입 확인 : 함수나 메소드가 특정 클래스의 인스턴스라고 기대할때, 이를 확인하는 기능
# 2) 다형성 처리 : -> 수업 내용상 skip

class Student:
    def study(self):
        return '공부하는 중입니다.'

class Teacher:
    def teach(self):
        return '가르치는 중입니다.'
    
# 리스트에 어떤 객체가 있는지 모르는 상황, 특정 인스턴스만 기대할 수 없다. -> 여러가지 타입이 섞여있을 수 있다.
peoples = [Student(), Teacher(), Student(), Teacher()]
peoples[0].teach() # AttributeError: 'Student' object has no attribute 'teach'
                   # 해당 객체의 클래스에 없는 메소드를 사용하려고 하여 생긴 오류

if isinstance(peoples[0], Teacher): # 어떤 클래스에 속하는지 확인 : Teacher
    print(peoples[0].teach()) # Teacher 클래스의 메소드 사용
elif isinstance(peoples[0], Student): # 어떤 클래스에 속하는지 확인 : Student
    print(peoples[0].study()) # Student 클래스의 메소드 사용