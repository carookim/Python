# 파일 위치 : class_10.py

# 4] 클래스 개념 활용하여, 숫자 맞추기 게임 만들기

# 숫자 맞추기 게임
# 규칙
# 1. 컴퓨터가 1~100 사이의 숫자 하나를 랜덤으로 선택합니다.
# 2. 사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞춥니다.
# 3. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "너무 커요!" 라고 출력합니다.
# 4. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "너무 작아요!" 라고 출력합니다.
# 5. 사용자가 숫자를 맞추면 "정답입니다!" 라고 출력하고 게임을 종료합니다.
# 6. 사용자가 숫자를 맞출 때까지 계속 입력을 받습니다.

import random
class NumberGuessingGame:
    def __init__(self): # * 클래스 변수가 아닌 생성자로 설정한 이유, ^ 아래 사용되는 변수들(count, computer_number)은
                        # 각 게임 인스턴스마다 다르게 유지되어야 하기 때문이다.
        self.computer_number = random.randint(1, 100)
        self.count = 0 # 시도 횟수 # 클래스 변수 (NumberGuessingGame.count) → 모든 인스턴스가 공유하는 값
                                   # 클래스 내부에서 공유하는 변수를 생성하고 싶을 때 사용한다.
    def guess_process(self):
        while True:
            user_number = int(input('숫자를 입력하세요 (1~100)'))
            self.count += 1
            if user_number > self.computer_number:
                print('너무 커요!')
            elif user_number < self.computer_number:
                print('너무 작아요!')
            else:
                print(f'정답입니다! {self.count}번 만에 맞추셨습니다.')
        
# 메인 코드
game = NumberGuessingGame() # 객체 생성 및 클래스를 부여
game.guess_process() # 클래스에 있는 메소드 호출