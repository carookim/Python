class People():
    def make_instance(self):
        self.name = None
        self.age = None
        self.addr = None

h1 = People()
h1.make_instance()
print(h1.addr)
# 왜 출력이 되지않는지, 함수가 실행이 되지않아서? ^ 클래스 내부에 함수를 정의 한것뿐, 함수를 호출한게 아니기 때문이다.
h2 = People()
print(h2.addr)

# __어쩌구__ 의 경우 자동호출이 되고있던 함수구나