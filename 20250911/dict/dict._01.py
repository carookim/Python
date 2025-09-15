# 집합을 이루는 요소 : 수지,문자, 문자열, 리스트, 셋, 튜플

[1,1.5,'안녕',[1,2,3], {3,4,6},(10,20,30)]

# key 와 value 쌍으로 구성되있다.

# dict
# 키와 값의 쌍으로 구성되있다. {key : value, key :value} ^ ()나 []로 도 dict 가능한지
# 키에 있는 건 value 값으로 사용될 수 없다
# 순서가 없다
# 키는 중복안된다
# 키는 변하지 않는 자료형만 가능(문자열, 숫자, 튜플)
# CRUD 가능
# 각 요소에 접근할때는 키 값으로 접근한다 (인덱스가 없다)

# 생성하기
student = {
    "name" : "홍길동",
    "age" : 20,
    "major" : "컴퓨터"
}

# 읽기
print(student['name'])

# 업데이트 하기
student["name"] = '이순신'
print(f'studnet = {student}')

# 삭제하기
del student["name"]
print(f'studnet = {student}')

# 추가하기
student['add'] = '서울시 강남구'
print(f'studnet = {student}')
# 업데이트와 추가하는 방법이 동일하다. 입력되는 값이 없는 값이라면 추가되고, 있는 거라면 업데이트 된다.