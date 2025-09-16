# 파일 위치 : class2_02.py
# ! 상속개념을 활용한 다양한 예제 풀어보기

# 3] 상속개념을 활용한 예제


# 1) 상속개념을 활용한 예제 : Exception 사용
# 정수값이고 주어진 범위를 벗어나면 발행하는 Exception
class OutOfRangeError(Exception): # Exception 클래스를 부모 함수로 둔다.
    def __init__(self,strname):
        super().__init__(strname) # 부모클래스 생성자를 호출하고 자식 객체(self)에 부모 속성들을 초기화
                                  # 그래서 자식 클래스의 객체 생성 생성자에서 부모클래스 생성자를 부르고 초기화한다.
                                  
    def show_info(self): # OutOfRangeError 클래스 안에 정의된 메서드(method)
                         # 이 메서드를 호출하면, 문자열 "사용자가 정의한 예외입니다."를 반환함
        return '사용자가 정의한 예외입니다.'

try: # 오류가 발생할 가능성이 있는 코드 블록을 묶는 키워드
    number = 100
    if not 0 <= number <10:
        raise OutOfRangeError('0과 10사이를 벗어났습니다.')
    int('asdfasdf')
except OutOfRangeError as e: # try 블록에서 발생한 특정 오류를 처리하는 블록 / as 발생한 예외 객체를 변수로 받기 위해 사용
    print(e)
except ValueError as e: # try 블록에서 발생한 특정 오류를 처리하는 블록 / as 발생한 예외 객체를 변수로 받기 위해 사용
    print(e)

# 2) 상속개념을 활용한 예제 :