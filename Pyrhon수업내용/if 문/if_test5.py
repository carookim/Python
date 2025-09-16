# 논리 연산자 사용
# 나이가 18이상(성인) 이면서 주민번호를 가진사람은 "입장가능" "입장불가"
has_id = True
# has_id == True 라고 하지않는 이유?
# has_id 라는 변수 자체가 주민번호를 가진건지 아닌지 여부가 들어가 있어서
age = int(input('나이를 입력하세요: '))
print(type(age))

if has_id and age >= 18:
    print('입장가능')
else:
    print('입장불가능')
print('종료')

# 트라이 구문 ^
# 에러, 오류가 발생한 시점에서 프로그램은 죽은 거라고 부른다.