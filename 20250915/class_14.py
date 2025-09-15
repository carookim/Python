# 클래스
# 클래스 변수, 인스턴스 변수
# 생성자 __init__
# 메소드 __str__, __eq__, __ne__, __lt__, __gt__, __le__, __ge__
# property, getter, setter, deleter, private -> 함수를 변수처럼 사용 # private를 로직으로 만들기 위해서 사용
# 객체생성

class Student:
    def __init__(self, name, score):
        self.name = name        # public 변수
        self._score = score     # private 변수

    # -------------------------
    # score에 대한 property
    # -------------------------
    @property
    def score(self):            # getter
        print(f"{self.name} 점수 조회")
        return self._score

    @score.setter
    def score(self, value):     # setter
        if 0 <= value <= 100:
            print(f"{self.name} 점수 변경: {self._score} -> {value}")
            self._score = value
        else:
            print("점수는 0~100 사이여야 합니다!")

    @score.deleter
    def score(self):            # deleter
        print(f"{self.name} 점수 삭제됨")
        del self._score

# -------------------------
# 사용 예제
# -------------------------
s1 = Student("홍길동", 90)
s2 = Student("김철수", 85)

# public 변수 접근
print(s1.name)   # 홍길동
s1.name = "박영희"
print(s1.name)   # 박영희

# private 변수 score 접근
print(s1.score)  # getter 호출
s1.score = 95    # setter 호출
s1.score = 120   # setter 호출 → 검증 실패

# deleter
del s1.score
ㄴ