array = [273, 32, "안녕하세요", True, False]
age = 25
array.append(age)
print(array)
# age가 출력이 될때 25로 출력이 된다.
# age는 변수명이고 그 age가 담은 값을 출력하고 있다.

array_2 = [100, array]
print(array_2)
# 리스트안에 리스트를 담으면, 리스트안에 리스트가 존재하게 된다.

# array 에서 안녕하세요를 출력하는 방법
print(array[2])

# array_2 에서 안녕하세요를 출력하는 방법
print(array_2[1][2])
# array_2[1] == array

# array_2 에서 안녕하세요의 요를 출력하는 방법
print(array_2[1][2][4])

# 문자열의 경우는 리스트 처럼 인덱스 접근이 가능하다.
# 하지만 문자열 자체를 변경할수는 없다. 새로 문자열을 생성하는 거에 가깝다.
# 문자열을 "수정"하는 것처럼 보이는 모든 작업은 사실 기존 문자열의 일부를 가져오거나
# 다른 문자열과 합쳐서 완전히 새로운 문자열을 생성하고, 보통 그 결과를 같은 변수 이름에 다시 저장하는 것입니다.

temp = [
    [1,2],  # temp[0] -- row 행
    [10,20], # temp[1] temp[1][1] == 20
    [30,40] # temp[2] temp[2][0] == 30
]   # column 열

list_a = [273, 32, 103, "문자열", [1,2,3], True, False]
print(list_a[0])
print(list_a[3][0])
print(list_a[4][0])