# import random
# result = random.randit(1,5)

# 함수정의 def 키워드 사용
# 매개변수(Parameter) : 함수가 전달 받는 값
# 인자(Argument) : 함수를 호출할때 전달하는 값
# 반환값(Return Value) : 함수가 작업을 마치고 호출한 곳으로 돌려주는 값
    # return 키워드를 사용

# 함수의 구성요소 4. 매개변수와 반환값이 있는 함수
def myCalc(num1, num2): # 값을 두개를 받기로 설계
    result = num1 + num2
    return result # return, 반환값이 없게 하면 어떻게 되는 거지?
                  # 임의로 print()값으로 결과값을 출력하게 하는 방법으로 하는 건? ^

myCalc(1,2)

# 1.매개변수와 반환값이 없는 함수
# 사방이 닫힌 네모 모양 박스
def say_hello():
    '''
    "안녕하세요" 를 출력합니다.
    '''
    print("안녕하세요...")

# 2.매개변수가 있고 반환값이 없는 함수
def say_hello_name(name): # name에 들어가는 값을 무조건 문자열로만 고정하는 법? ^ ''를 해야 문자열이 인식이 된다.
    print(f'{name}님 안녕하세요.')

# 3.매개변수가 없고 반환값이 있는 함수
import datetime
def get_current_time():
    return datetime.datetime.now()

#---------------------------------
# 위에서 만든 4개의 함수 사용해보기.
# 1.
print(say_hello)

# 2.
print(say_hello_name('김지은'))

# 3.
now_time = get_current_time()
print(now_time)

# 4.
# myCalc(1)
# TypeError: myCalc() missing 1 required positional argument: 'num2'
print(f"3 + 5 = {myCalc(3, 5)}")