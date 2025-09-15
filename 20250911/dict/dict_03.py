# enumerate(), zip(), .items(), .keys(), .values() # 고급기능 이지만 편리, 하지만 난이도가 있을수도 있다. 집중하기
# map(), 정렬 -> 람다함수를 적용
# 함수의 파라미터 - 키워드 파라미터, 가변 키워드 파라미터

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
my_bag["물통"] = "하얀색"
print(my_bag)

# 공책을 다써서 버려주세요
del my_bag["공책"]
print(my_bag)

# 순환문과 연결
for i in my_bag:
    print(f'key = {i}, value = {my_bag(i)}')
    # 출력하면 키값이 나온다.
    # for문 내부에서도 딕셔너리의 키값을 반환하고 있다는 점을 알 수 있다.