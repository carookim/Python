# 파일 위치 : class_8.py

# 2] 클래스 개념 정리 예제

# 학생클래스 생성
# 인스턴스 변수  : 이름 국 영 수
# 인스턴스 메서드 : 총점, 평균, 학점, __str__
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math

    def average(self):
        return self.total() / 3

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    def __str__(self):
        return f'이름: {self.name}, 총점: {self.total()}, 평균: {self.average():.2f}, 학점: {self.grade()}' # ^ .2f 소숫점 둘째 자리수까지
    
# 인스턴스 생성
s1 = Student('홍길동', 95, 85, 75)
s2 = Student('임꺾정', 70, 90, 89)
print(s1)
print(s2)

# 다시 작성해보기 :
