# 함수
# 함수명 add
# 파라미터는 2개 op1, op2
# 결과를 반환한다.

# 생성
def add(op1,op2):
    # return op1 + op2
    result = op1 + op2
    return result
# 안에 함수를 리턴한다고 하며 어떻게 되나?

# 사용
print(add(10,20)) # 출력
two_number_hab = add(10,30) # 변수 생성
numbers = [add(10,20),add(10,20),add(10,20)]

# 매개변수 받아서 출력하는 함수
# 함수명 : show_numbers
# 매개변수명 : data
def show_numbers(data):
    return f'numbers = {data}'

print(show_numbers(add(10,2)))