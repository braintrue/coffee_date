class MildangDate:
    def __init__(self):
        self.milestones = {
            1: "과자 챙겨줌 -> 그 사람이 무의식적으로 받음",
            2: "네가 없던 날에도 네 책상을 떠올리고 간식 놔둠",
            3: "다시 과자 챙겨줌 -> 이젠 말 없이 손만 내밀어 받음 (더 편해짐)",
            4: "오늘은 아예 커피까지 사다 줌 (상호 교환의 시작?!?)"
        }
        self.current_milestone = 0

    def update_milestone(self):
        if self.current_milestone < len(self.milestones):
            self.current_milestone += 1
            return self.milestones[self.current_milestone]
        else:
            return "이미 모든 상황을 다 경험했습니다!"

    def get_current_status(self):
        if self.current_milestone == 0:
            return "아직 시작되지 않았습니다. 상대방과의 첫 만남이 필요합니다."
        elif self.current_milestone > len(self.milestones):
            return "모든 상황이 종료되었습니다."
        return self.milestones[self.current_milestone]

    def reaction(self):
        if self.current_milestone == 1:
            return "창섭: '오늘은 과자 챙겨줘야지. 그 사람도 좋겠지?'"
        elif self.current_milestone == 2:
            return "창섭: '그 사람이 나의 책상에 과자를 놔둔 걸 보니, 그 사람도 나를 생각하는 거지?'"
        elif self.current_milestone == 3:
            return "창섭: '아, 이제 말 없이 손 내밀기만 하면 되네. 점점 편해진다.'"
        elif self.current_milestone == 4:
            return "창섭: '이제 커피까지 주네! 상호 교환이 시작된 건가?'"
        else:
            return "창섭: '모든 게 완벽하게 잘 진행되고 있어!'"

# 프로그램 실행
def main():
    print("창섭의 밀당 시뮬레이션 프로그램!")
    mildang = MildangDate()

    while True:
        print("\n현재 상황:")
        print(mildang.get_current_status())
        user_input = input("\n상황을 진행하려면 '진행'을 입력하세요. 종료하려면 '종료'를 입력하세요: ").strip().lower()
        
        if user_input == "진행":
            print(f"\n진행된 상황: {mildang.update_milestone()}")
            print(f"창섭의 반응: {mildang.reaction()}")
        elif user_input == "종료":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 입력을 해주세요.")

if __name__ == "__main__":
    main()
