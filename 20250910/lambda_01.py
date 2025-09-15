# 람다가 사용되지 않는 상황
def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def calc(func, a,b): # ^ calc(func, a,b)
    return func(a,b)

print(calc(add,1,2))
# 여기서 func는 타입처럼 함수를 부르는 키워드 같은 건지 ^
# func는 특별한 키워드가 아니라 그냥 매개변수 이름(변수명) 이에요.

print(calc( lambda a,b : a+b, 1,2 ))
# 람다 형식
# lamda 파라미터 : 내용, 아규먼트
# 수시로 필요할때마다 함수를 만들지 않아도 람다만 작성해서 만들수있다.
# 편의성을 위해 만들어진 람다 함수
# 람다는 필요할때 마다 만들어서 사용할 수있지만, 함수는 생성해두면 메모리를 차지하기때문에
# 람다기능을 사용하는 것

print(calc( lambda x,y : x*y, 10,20 ))

# 근데 왜 calc 함수를 사용해야되는 거지? ^ 고차 함수(Higher-Order Function) 개념 ^