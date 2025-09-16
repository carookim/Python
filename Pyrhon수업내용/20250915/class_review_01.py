# 기본 클래스 생성 
class review:
    # 클래스변수 생성 : 모든 인스턴스가 공유하는 변수
    count = 0
    # 생성자 메소드 : 객체 생성시 자동으로 호출되는 메소드, 콜백함수 / 이벤트 함수라고도 부른다.
    def __init__(self):
        self.name = '' # 인스턴스 변수 : 자기가 고유하게 지니고 있는 변수

# 인스턴스 생성 = 객체 생성
r1 = review() #  =  def __init__(self):
              #         self.name = '' ^
r2 = review()
# print(r1)

# 인스턴스 변수 변경
r1.name = '첫번째 리뷰'
print(f'r1 인스턴스 변수 : {r1.name} / r2 인스턴스 변수 : {r2.name}')
print(f'review 클래스 변수 : {review.count}')
# 클래스 변수를 접근할때는
# (1) 클래스이름.변수명 (권장)**
# (2) 인스턴스이름.변수명 **

# 그러면 없는 클래스변수에 접근할려고하면 어떻게 될까?
# 클래스이름에서 접근하는 경우 : AttributeError 발생
# 인스턴스이름에서 접근하는 경우 : 본인에게도 없다면, AttributeError 발생

# ** 인스턴스이름.변수명 = 값
# -> 인스턴스 변수로 새로 생성이 되고, 클래스 변수와는 별개로 존재하게 된다.
# 인스턴스에 이미 존재하는 변수가 있다면 인스턴스.변수명 으로 클래스 변수에 접근할 수 없을 수 있다.
# 그래서 클래스명.변수명 으로 접근하는 것을 권장한다.


##
# 기본 클래스 생성 
class review:
    # 클래스변수 생성 :
    count = 0
    # 생성자 메소드 :
    def __init__(self):
        self.name = '' # 인스턴스 변수 :

# 인스턴스 생성 = 객체 생성
r1 = review(100)
# TypeError: review.__init__() takes 1 positional argument but 2 were given

# 수정
class review:
    count = 0
    def __init__(self, num = 0):
        self.name = ''
r1 = review(100)
r2 = review() # 이제 여기서 오류남
