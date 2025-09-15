class People():
    def __init__(self): # __init__ ^ 객체가 생성될 때 자동으로 호출됨
                        # 객체의 속성(initial state)을 초기화하는 용도
        self.name = None
        self.age = None
        self.addr = None
        print('생성자 호출')

print('객체 생성 전')
h1 = People()
print('객체 생성 후')
print(h1.addr)

class Product():
    serial_num = 0 # 클래스 변수, 객체로 접근하지않는다. 접근해서도 안되는 듯하다. ^
    def __init__(self):
        Product.serial_num += 1
        self.serial_num = Product.serial_num # 클래스 내부에 있는 변수를 불러서 사용도 가능하구나 ^
        self.name = None
tv1 = Product()
tv2 = Product()
tv3 = Product()

print(tv1.serial_num, tv2.serial_num, tv3.serial_num)
# 실행이 될때마다 self.serial_num이 1씩 증가하는 걸 볼 수 있다.
# for 문 처럼 순환 되면서 뭔가 값이 상승하게도 가능하다.

# 클래스 변수
# 모든 객체가 공유
# Product.serial_num 이렇게 클래스로 직접 접근 가능
# 객체로 접근하면 사실상 “인스턴스 속성이 우선” 때문에 혼동이 있을 수 있음


if __name__ == '__main__':
    tv1 = Product()
    tv2 = Product()
    tv3 = Product()

# if __name__ == "__main__":는
# __name__라는 문자열이 "__main__"과 같은가?
# 이고
# __main__ 기재된 파일의
# 직접 실행 = “파이썬 파일을 직접 실행 버튼으로 실행하거나, python 파일명.py로 실행”하는 것