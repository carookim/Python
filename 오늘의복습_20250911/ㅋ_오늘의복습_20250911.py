# 파일 위치 : dict_03.py

# 9] 딕셔너리 기본기 예제(1)

my_bag = {"필통" : "파란색", "공책" : "수학공책", "지갑" : "분홍색"}

# 출력
print(my_bag)

# 가방에서 필통을 꺼내서 출력
print(my_bag["필통"])

# 가방에서 공책을 꺼내서 출력
print(my_bag["공책"])

# 지갑이 오래되서 "가죽지갑" 변경
my_bag["지갑"] = "가죽지갑"
print(my_bag)

# 물통을 추가 하얀색
my_bag["물통"] = "하얀색" # 딕셔너리에서 키: 값을 추가하는 방법 result[키] = 값
print(my_bag)            # 왼쪽값 키가 key, 오른쪽값 값이 value가 되어 딕셔너리가 된다.

# 공책을 다써서 버려주세요
del my_bag["공책"]
print(my_bag)

# 순환문과 연결
for i in my_bag:
    print(f'key = {i}, value = {my_bag(i)}') # 출력하면 키값이 나온다.