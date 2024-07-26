from player import Player
from stage import Stage
from trash import TrashItem
import random
def print_divider():
    print("-"*40)

def end_of_stage():
    print("="*40)

def setup_game():
    tumbler_stainless = TrashItem("텀블러(스테인리스)", 1, ["캔류에 버린다", "일반쓰레기에 버린다", "캔류,일반쓰레기 둘 다 가능하다"])
    tumbler_silicone = TrashItem("텀블러(실리콘)", 2, ["캔류에 버린다", "일반쓰레기에 버린다", "캔류,일반쓰레기 둘 다 가능하다"])
    kitchen_knife = TrashItem("식칼", 2, ["그대로 일반쓰레기에 버린다", "신문지로 여러 겹 겹친 후 일반쓰레기에 버린다", "캔류에 버린다"])
    Pringles = TrashItem("프링글스 통(몸통)", 3, ["일반쓰레기에 버린다", "몸체와 바닥을 분리한 후 몸체는 폐지, 바닥은 캔에 버린다", "몸체와 바닥을 분리한 후 몸체는 일반쓰레기, 바닥은 캔에 버린다"])
    scissors = TrashItem("가위", 1, ["신문지로 여러 겹 겹친 후 일반쓰레기에 버린다", "캔류에 버린다", "그대로 일반쓰레기에 버린다"])
    wet_tissue = TrashItem("물티슈", 1, ["일반쓰레기에 버린다", "폐지에 버린다", "변기에 넣고 내린다"])
    cup_noodles = TrashItem("컵라면용기", 2, ["일반쓰레기에 버린다", "햇볕에 말려 얼룩을 지우고 스티로폼에 버린다", "얼룩진 상태로 스티로폼에 버린다"])
    chicken_bone = TrashItem("치킨 뼈", 3, ["변기에 넣고 내린다", "음식물 쓰레기에 버린다", "일반쓰레기에 버린다"])
    stocking = TrashItem("스타킹", 3, ["비닐에 버린다", "의류수거함에 버린다", "일반쓰레기에 버린다"])
    egg = TrashItem("계란껍질", 2, ["음식물 쓰레기에 버린다", "일반쓰레기에 버린다", "변기에 넣고 내린다"])
    cd = TrashItem("CD", 2, ["플라스틱에 버린다", "일반쓰레기에 버린다", "캔에 버린다"])
    mouse = TrashItem("마우스", 1, ["일반쓰레기에 버린다", "플라스틱에 버린다", "캔에 버린다"])
    glasses = TrashItem("안경", 3, ["플라스틱에 버린다", "유리에 버린다", "일반쓰레기에 버린다"])
    multi_tab = TrashItem("멀티탭", 2, ["일반쓰레기에 버린다", "폐가전제품 수거에 버린다", "플라스틱에 버린다"])
    soju_glass = TrashItem("소주병", 3, ["뚜껑과 병 둘 다 일반쓰레기에 버린다", "뚜껑과 병을 분리하여 배출한다", "뚜껑과 병을 합친 후 유리에 배출한다"])
    sub_battery = TrashItem("보조배터리", 1, ["폐건전지 수거함에 버린다", "일반쓰레기에 버린다", "플라스틱에 버린다"])

    trash_list = [tumbler_stainless, tumbler_silicone, kitchen_knife, Pringles, scissors, wet_tissue, cup_noodles, chicken_bone, stocking, egg, cd, mouse, glasses, multi_tab, soju_glass, sub_battery]
    #print(trash_list)
    numbers = list(range(16))
    random.shuffle(numbers)
    trash_items = [trash_list[i] for i in numbers]

    stages =  [
        Stage(1,"자취방", trash_list[:4]),
        Stage(2,"식당", trash_list[4:8]),
        Stage(3,"복지관", trash_list[8:12]),
        Stage(4,"학교", trash_list[12:16])
    ]

    return stages

def main():
    end_of_stage()
    player_name = input("플레이어 이름을 입력하세요 : ")
    end_of_stage()
    player = Player(player_name)
    stages = setup_game()
    print()

    #print(stages[1].trash_items)
    end_of_stage()
    print(f"환영합니다! {player.name}님 게임 방법에 대해서 소개 해 드리겠습니다!")
    print_divider()
    print(f"{player.name}님은 각 방을 돌면서 쓰레기를 수집합니다. 총 네 개의 방을 돌고 난 후 분리수거장에 도착합니다.")
    print_divider()
    print(f"분리수거장에서 지금까지 수집한 쓰레기들을 분리수거하면 됩니다.")
    print_divider()
    print(f"시스템은 쓰레기에 대한 여러가지 분리수거 방법을 제공하고. 플레이어는 그 중 올바른 분리수거 방법을 골라 숫자로 입력하면 됩니다.")
    print_divider()
    print(f"올바른 분리수거 방법을 선택하면 1점을 획득합니다.")
    print_divider()
    print(f"제 설명은 여기까지 입니다. 행운을 빌겠습니다! ")
    end_of_stage()
    print()

    for stage in stages:
        end_of_stage()
        print(f"{stage.stage_number}번방 : {stage.stage_name}")
        print_divider()
        trash_names = [stage.trash_items[i].name for i in range(4)]
        print(f"{stage.stage_name}에 있는 쓰레기 : {trash_names}")
        print_divider()
        #player.add_trash(trash for trash in stage.trash_items)
        player.trash_items.extend(stage.trash_items)
        print("다음방으로 넘어가시겠습니까?[Y/N]")
        print_divider()
        while True:
            answer = input("Y나N을 입력하세요 : ")
            if answer.lower() == 'y' or answer.lower() == 'n':
                break
            else:
                print("잘못된 입력입니다.")
        if answer.lower() == 'n':
            break
        end_of_stage()
        print()

    end_of_stage()
    print("분리수거장에 도착했습니다. 지금까지 수집한 쓰레기를 분리수거하세요.")
    print_divider()
    for trash in player.trash_items:

        print(f"{trash.name}에 대한 올바른 분리수거 방법은?")
        print_divider()
        for i,choice in enumerate(trash.choices,1):
            print(f"{i} : {choice}")
        print_divider()

        while True:
            
            try:
                print_divider()
                answer = int(input("정답을 입력하세요 : "))
                print_divider()
                if answer in [1,2,3]:
                    break
                else:
                    print("올바른 선택지를 입력하세요 (1, 2, 3).")
            except ValueError:
                print("숫자를 입력하세요.")

        if answer == trash.correct_choice:
            player.increase_score()
        print_divider()
        print(trash.check_disposal(answer))
        print_divider()

    end_of_stage()
    print(f"{player_name}님의 최종 점수는 {player.score}")
    end_of_stage()
if __name__ == "__main__":
    main()
