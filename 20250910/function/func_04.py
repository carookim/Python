# 가변 매개변수
    # 함수정의 할때, 매개변수의 개수를 지정하지 않습니다.
    # 함수내부에서는 리스트로 간주합니다.
    # 함수를 호출하는 쪽에서는 편안하게.. 1,2,3,4 or 1,2,3,4,5,1,4,5

def myFunc1(args):
    for i in args:
        pass

datas = [10,20,50,60]
myFunc1(datas)

# myFunc1(10,20,50,60)
# # 한개의 parameter 에 4개의 argument가 들어가서 에러가 난다.

# 여러가지 갯수가 변한는 변수를 넣기 위해서는 
# datas = [10,20,50,60]
# myFunc1(datas)
# 이런식으로나
# myFunc1([10,20,50,60]) 해야되는데,
# 입력한 argument들을 자동으로 리스트로 변경하게 하기위해선 parameter앞에 *를 붙이면 된다.
# 21번째 줄을 패킹이라고 한다. ^ 다른 건 뭐라고 부르는지

def myFunc1(*args): # packing
    for i in args:
        print(i)
myFunc1(10,20,50,60)
myFunc1([10,20,50,60])

def myFunc1(args):
    for i in args:
        print(i)
myFunc1([10,20,50,60])

# unpacking
a,b = [10, 20]
print(f'a = {a}')
print(f'b = {b}')

# 추가로 다른 언패킹 방법이 있는 것같다 ^