# 파일 위치 : class2_01.py

# 2] 상속

# 상속의 정의
# 상속은 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받습니다.
# 상속을 통해 코드의 재사용성을 높이고, 클래스간의 계층적인 관계를 표현할 수 있습니다.

# 상속의 기본 문법
# class 부모클래스:
#     def 부모메서드(self):
#         print("부모 메서드 호출")

# class 자식클래스(부모클래스):
#     def 자식메서드(self):
#         print("자식 메서드 호출")

# 클래스 상속하는 법
# 클래스()에서 괄호안에 상속받을 클래스명을 입력하면된다.

# 부모 클래스
class Parents():
    def __init__(self,name):
        self.p_name = name
        print('부모 생성자')
    def parents_method(self):
        print('부모클래스 메서드')

class Child(Parents):
    def __init__(self,name):
        Parents.__init__(self, name) # ^ 부모 클래스 생성자를 자식 클래스에서 호출하는 이유는
        print('자식 생성자')         # 자식 객체(self)에 부모 속성들을 초기화하기 위해서이다.
    def child_method():
        print('자식클래스 메서드')

# Child 클래스 객체 c
c = Child()
# c. 으로 작성해보면 클래스 정의에서 만든 메서드말고도, 자동으로 부여되있는 __함수__가 있다.
# 그중에는 Parents내에 있는 메서드도 있는데, 이는 Child 상속 받아서 사용이 가능한거다.