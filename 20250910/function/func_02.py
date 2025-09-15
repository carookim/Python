# 매개변수 O, 반환값 O
# 매개변수 O, 반환값 X
# 매개변수 X, 반환값 O
# 매개변수 X, 반환값 X

# 만들고 사용해보기

# 매개변수 O, 반환값 O
# 평균값을 구하는 함수, average
def average(a,b,c,d): # 매개변수의 갯수값은 고정되어있어야 되는지? ^ 가변 매개변수
    '''
    4개의 매개변수 a,b,c,d를 받아
    평균을 구하는 함수
    '''
    result = (a + b + c + d) // 4
    return result

# 매개변수 O, 반환값 X
def say_niceday_date(date):
    '''
    "입력한날짜 (예시) 910)niceday" 를 출력합니다.
    '''
    print(f'{date} niceday')

# 매개변수 X, 반환값 O
def get_10sum10():
    '''
    10 + 10의 결과값을 반환합니다.
    '''
    return 10+10

# 매개변수 X, 반환값 X
def say_niceday():
    '''
    "niceday" 를 출력합니다.
    '''
    print("niceday")

# 함수를 부를려면 함수뒤에 꼭 ()가 있도록 기재하기

# 매개변수 O, 반환값 O
average(1,2,3,4)
print(average(1,2,3,4))
print()

# 매개변수 O, 반환값 X ^
say_niceday_date(910)
print(say_niceday_date(910))
print()

# 매개변수 X, 반환값 O
get_10sum10()
print(get_10sum10())
print()

# 매개변수 X, 반환값 X ^
say_niceday()
print(say_niceday())

# niceday
# niceday
# None

# niceday <- say_niceday()에서 niceday 출력
# niceday <- print(say_niceday())의 say_niceday()에서 niceday 출력
# niceday <- print(say_niceday())의 print()에서 None 출력