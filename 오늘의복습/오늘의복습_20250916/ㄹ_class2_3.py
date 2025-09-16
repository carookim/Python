# 파일 위치 : class2_05.py
# !

# 4] 추상메서드, 추상화

# 추상메서드 : abstractmethod

from abc import ABC, abstractmethod # 추상 클래스 생성 및 추상 클래스 안에서 자식이 반드시 구현해야 하는 메소드를 표시, abstractmethod
class Parents(ABC):
    def make_money(self):
        raise NotImplementedError
    @abstractmethod # 부모클래스에 이 항목이 있다면, 아래 정의되어진 함수가 자식함수에 구현되게 강제하는 명령어이다.
                    # 그러지 않으면 코드가 에러가 나게 끔 작동이 되어서, 작성하지않으면 해당 클래스 인스턴스를 기점으로 코드가 죽는다.
    def save_money(self):
        print('저축')

class Child(Parents):
    def make_money(self):
        print('장사')

c = Child() # 부모의 추상메서드를 상속받으면, 클래스에서 반드시 해당 함수를 재정의 하지 않으면 객체 생성불가 : save_money 함수 형성 필수
c.make_money() # 장사가 출력된다. 다형성 # 자식클래스에서 재정의안하면 예외발생하도록 설계되어있다.

# 추상화  
# : 공통적인 기능이나 개념만 뽑아내어(추상화) 상위 클래스에 정의하고, 세부 구현은 하위 클래스가 맡도록 하는 개념 
# from abc import ABC, abstractmethod

# 추상 메서드  
# : 부모 클래스에서 메서드의 '이름과 규칙'만 정의하고, 실제 구현은 자식 클래스가 반드시 하도록 강제하는 메서드
# @abstractmethod
# def save_money(self):
#     print('저축')

# 다형성  
# : 같은 메서드 이름을 사용하지만, 객체의 종류(클래스)에 따라 실행되는 동작이 달라지는 성질

# 추상 메서드 → “이건 꼭 만들어야 한다”라는 틀
# 추상화 → “공통점만 위로 모으는 과정”
# 다형성 → “동일한 이름, 다른 동작”

# ! class2_03.py를 위내용 적용해서 작성해보기.