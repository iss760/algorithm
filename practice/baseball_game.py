import random


class BaseballGame:
    def __init__(self):
        # 기회 초기값 설정
        self.max_chance = 8

        # 출력값 초기값 설정
        self.n_strike = 0
        self.n_ball = 0
        self.n_out = 0

        # 정답 초기값 설정
        self.right_answer = []
        # 정답 생성
        self.generate_right_answer()

    # 난수 생성으로 정답을 만드는 메서드
    def generate_right_answer(self):
        for i in range(3):
            # 초기 난수 생성
            temp = random.randint(1, 9)
            # 생성된 초기 난수가 이미 정답 셋에 있다면, 다시 난수 생성
            while temp in self.right_answer:
                temp = random.randint(1, 9)
            # 중복이 없는 난수를 정답 셋에 입력
            self.right_answer.append(temp)

        return self.right_answer

    # 게임을 실행하는 메서드
    def game_start(self):
        print("Game Start")
        # 메인 구동
        self.game_main()

    # 실제 게임이 구동되는 메서드
    def game_main(self):
        while True:
            # 입력받기
            answer = self.input_answer()
            # 비교하기
            self.compare_answer(answer)
            # 결과 출력하기
            self.print_result()
            # 기회 한번 소진
            self.max_chance -= 1
            # 승리, 패배 여부 판단
            if self.is_game_over() or self.is_game_win():
                break
            # 결과 초기화
            self.reset_result()

    @staticmethod
    def input_answer():
        # 사용자로부터 3개의 숫자를 입력 받음
        answer = [0, 0, 0]
        temp = int(input())
        answer[0], temp = divmod(temp, 100)
        answer[1], answer[2] = divmod(temp, 10)

        return answer

    def compare_answer(self, answer):
        # 사용자가 입력한 값과 정답을 비교
        for i in range(3):
            # 스트라이크가 있는지 검사
            if answer[i] == self.right_answer[i]:
                self.n_strike = self.n_strike + 1
            # 볼이 있는지 검사
            elif answer[i] in self.right_answer:
                self.n_ball = self.n_ball + 1
            # 아웃이 있는지 검사
            else:
                self.n_out = self.n_out + 1

    # 스트라이크, 볼, 아웃 수를 출력해주는 메서드
    def print_result(self):
        # 현재 결과 출력
        print("%d strike, %d ball, %d out" % (self.n_strike, self.n_ball, self.n_out))

    # 스트라이크, 볼, 아웃 수를 초기화 해주는 메서드
    def reset_result(self):
        self.n_strike = 0
        self.n_ball = 0
        self.n_out = 0

    # 게임이 끝 유무를 반환하는 메서드
    def is_game_over(self):
        # 찬스 모두 소진 (패배 조건)
        if self.max_chance < 1:
            print("Game Over")
            print("Right Answer: ", self.right_answer)
            return True
        else:
            return False

    # 게임 승리 유무를 반환하는 메서드
    def is_game_win(self):
        # 스트라이크 3개 (승리 조건)
        if self.n_strike == 3:
            print("Game Win")
            return True
        else:
            return False
