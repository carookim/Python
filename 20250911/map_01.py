# map 자료구조의 각 요소에 특정 함수를 적용
# map(함수, 반복 가능한 객체)

str_numbers = ['1','10','100'] 
print(str_numbers)
print(map(int,str_numbers)) # map 오브젝트 자체는 출력할수가 없다?? ^
print(list(map(int,str_numbers)))

# .split() ^0
# 문자열.split(구분자, 최대분할횟수)
# 구분자는 공백 , ; 등 구분자에 입력한걸 사용가능하다.

list_3 = [10,20,30]
# 각 원소에 2를 곱한다.
def test(list):
    # 대충 list를 받아 두값을 곱하는 함수
    a = list[0]
    b = list[1]
    return(a * b)

print(list(map(test(list),list_3))) # 이렇게 하면 함수를 만들고 그걸 불러와야된다.

print(list(map(lambda data:data*2, list_3)))