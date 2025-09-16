class Parents:
    def make_money(self):
        raise NotImplementedError
    @abstractmethod
    def save_monet(self):
        print('저축')

class Child(Parents):
    def make_money(self):
        print('장사')

c = Child()
c.make_money() # 장사가 출력, 다형성