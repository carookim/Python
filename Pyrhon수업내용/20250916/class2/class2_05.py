# 추상메서드 abstractmethod

from abc import ABC, abstractmethod # 추상 클래스 생성 및 추상 클래스 안에서 자식이 반드시 구현해야 하는 메소드를 표시 abstractmethod
class Parents(ABC):
    def make_money(self):
        raise NotImplementedError
    @abstractmethod # 부모클래스에 이 항목이 있다면 아래 정의되어진 함수가 자식함수에 구현되게 강제하는 명령어이다.
                    # 그러지 않으면 코드가 에러가 나게 끔 작동이 되어서, 작성하지않으면 해당 클래스 인스턴스를 기점으로 코드가 죽는다.
    def save_money(self):
        print('저축')

class Child(Parents):
    def make_money(self):
        print('장사')

    # def save_money(self):
    #     pass

c = Child() # 부모의 추상메서드를 상속받으면 클래스에서 반드시 재 정의 안하면 객체 생성불가
c.make_money() # 장사가 출력, 다형성 # 자식클래스에서 재 정의안하면 예외발생하도록 설계

# ! class2_03.py를 위내용 적용해서 작성해보기.