# len()함수 구현하기
def len_return(sen):
    if type(sen) == str:
        return len(sen)
    else:
        return len(str(sen))

print(len_return('안녕하세요'))

print(len_return(13))
print()
# len()함수는 return값이 있는지? ^ 네, len() 함수에는 반드시 리턴값이 있습니다.

# 그럼 그걸 반영해서 리턴명령어 간소화하기?
# len()함수 구현하기
def len_return2(sen):
    if type(sen) == str:
        print(len(sen))
    else:
        print(len(str(sen)))

len_return2('안녕하세요')

len_return2(13)
print()
# VS Code의 **인터프리터(터미널이 아닌 Interactive/REPL 모드)**에서는,
# 마지막 표현식의 결과값을 자동으로 화면에 표시해 줍니다.
# 그걸 반영해서 출력 명령어 넣기.

# len()함수 구현하기
def len_return3(sen):
    if type(sen) == str:
        print(len(sen))
    else:
        print(len(str(sen)))

len_return3('안녕하세요')

len_return3(13)

# 간단한 함수, 람다
# 함수 내의 로직인 한줄로 표현 가능한 함수들
def my_add(a,b):
    return a+b

# 람다 함수 - 한줄로 표현한 함수 lambda 키워드 사용
# 간단한 함수를 즉석에서 만들때 유용

# lambda 파라미터:내용
test = lambda a,b: a+b
# 가변 매개변수인경우 람다에 사용하려면 어떻게 해야되는지 ^
a,b = 10,20 # ^
print(f'a + b = {my_add(a,b)}')
print(f'a + b = {test(a,b)}')
# 무조건 값을 리턴하는 함수, return 키워드 사용 안함