# 다양한 매개변수
    # 기본 매개변수 default parameter
    # 만약에 필요한 매개변수를 사용자가 입력하지 않았을 경우, 임의로 들어갈 default 값을 부여하는 것
# 포지셔널 매개변수 ^

def myAdd(num1, num2 = 0):
    return num1 + num2

result = myAdd(10,20)
print(f'result = {result}')

result = myAdd(10)
print(f'result = {result}')

# def myAdd(num1, num2 = 0, num3): # 오류가 뜬다. 왜? ^
#     return num1 + num2 + num3    # num1하고 num3에 값을 넣어야되는데, 그렇게 할려고 하면 순서가 안맞는다.
#                                  # myAdd(1,2) <- 첫번째와 세번째에 넣고자함, 하지만 2는 두번째에 들어가게된다.
#                                  # 그래서 서순을 매개변수는 뒤에 기재해야된다! 

# 기본 매개변수는 뒤에서부터 해야한다.
def myAdd(num1, num2 , num3 = 0):
    return num1 + num2 + num3

def myAdd(num1, num2 = 0, num3 = 0):
    return num1 + num2 + num3

def myAdd(num1 = 0, num2 = 0, num3 = 0):
    return num1 + num2 + num3

result1 = myAdd()
result2 = myAdd(1)
result3 = myAdd(1, 2)
result4 = myAdd(1, 2, 3)
print(result1,result2,result3,result4)