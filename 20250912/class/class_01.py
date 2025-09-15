class  StudentMng:
    name = '홍길동'

class  StudentMng():
    name = '홍길동'
# 함수를 표현하는 경우 소괄호가 무조건있어야되고, 변수에는 없어도 되는데 (예외사항이 있긴하지만)
# 클래스는 괄호 유무와 상관없이 그냥 작동이 된다.
# 클래스 괄호 안에 들어가는 항목은 뭐냐면,
# 부모 클래스를 넣는다.

# 클래스()의 괄호안에 여러개의 클래스를 기입하여 다중상속을 할수있지만, 그렇게 하니
# 충돌이 일어나는 경우가 생긴다.

# 클래스에서 ()의 용도는 괄호안 클래스를 부모클래스로 삼고 상속을 받게한다.

sl = StudentMng()
print(sl.name)

# 클래스 변수 VS 인스턴스 변수
class  StudentMng():
    name = '홍길동' # 클래스 변수

s1 = StudentMng()
s2 = StudentMng()
s3 = StudentMng()
print(s1.name,s2.name,s3.name)

s1.name = '강감찬' # 인스턴스 변수
print(s1.name,s2.name,s3.name)

StudentMng.name = '이순신' # 클래스 변수
print(s1.name,s2.name,s3.name)

# s1.name 자체가 변수가 된다?
# StudentMng.name = '이순신'을 통해 StudentMng내부의 name 의 값을 '이순신'이 된다.

# 클래스 변수와 인스턴스 변수가 있으면 인스턴스 변수가 이기는 구나 그 강도가 더 센거다.
# s2.name,s3.name 은 클래스가 없어서, StudentMng.name 에서 가져옴
# 하지만 s1.name은 s1.name = '강감찬'이라는 인스턴스가 그 하위항목에 있어서 그걸로 덮어씌워진다.
# 실행되는 지점에서 더 가까운 명령어가 실행된다는 느낌?
# x=1
# y=2
# z=3
# def x_logic(c):
#     c = x

# a = y
# b = y
# c = y

# x_logic(c) # > s1.name = '강감찬' 기능 1

# a = z
# b = z
# c = z 이 연결이 끊어진다. > s1.name = '강감찬' 기능 2

# print(a,b,c)


# 클래스 변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 재 할당받으면 해당 객체는 더 이상 참조하지 않는다.

# -------------------------------------------------------------------

# 클래스 변수 VS 인스턴스 변수

class StudentMng():
    name = '홍길동'  # 클래스변수    

s1 =  StudentMng() 
s2 =  StudentMng() 
s3 =  StudentMng() 

print(s1.name, s2.name,s3.name)
s1.name = '강감찬'  # 인스턴스 변수
StudentMng.name = '이순신'  # 클래스 변수
print(s1.name, s2.name,s3.name)

# 클래스변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 재 할당받으면 해당객체는 더이상 참조하지 않는다