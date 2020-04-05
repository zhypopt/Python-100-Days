"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from random import randint

def print_the_fig(num):
    if num == 1:
        print(" —————————")
        print("|         |")
        print("|    *    |")
        print("|         |")
        print(" —————————")
    elif num == 2:
        print(" —————————")
        print("|         |")
        print("|  *  *   |")
        print("|         |")
        print(" —————————")
    elif num == 3:
        print(" —————————")
        print("|    *    |")
        print("|    *    |")
        print("|    *    |")
        print(" —————————")
    elif num == 4:
        print(" —————————")
        print("|  *  *   |")
        print("|         |")
        print("|  *  *   |")
        print(" —————————")
    elif num == 5:
        print(" —————————")
        print("|  *  *   |")
        print("|   *     |")
        print("|  *  *   |")
        print(" —————————")
    elif num == 6:     
        print(" —————————")
        print("|  *  *   |")
        print("|  *  *   |")
        print("|  *  *   |")
        print(" —————————")    


def game_help():
    print("The rule of this game:")
    print(" ---玩家第一次摇骰子如果摇出了7点或11点，玩家胜；")
    print(" ---玩家第一次如果摇出2点、3点或12点，庄家胜；")
    print(" ---其他点数玩家继续摇骰子:")
    print(" ---如果玩家摇出了7点，庄家胜；")
    print(" ---如果玩家摇出了第一次摇的点数，玩家胜；")
    print(" ---其他点数，玩家继续要骰子，直到分出胜负")

def main_game(money):
    """
    the money now have 
    return the money current have 
    """
    print("===> Start a new round >===")      
    while True:
        str_in = input('Please set your debt (0, %d]:' % money)
        try:
            debt = int(str_in)
            if 0 < debt <= money:
                break
        except ValueError:
            if "n" in str_in.lower():
                return money
            elif "h" in str_in.lower():
                game_help()
            else:
                continue
    
    roll_str = input("----> roll a dice >----")
    first = randint(1, 6)
    second = randint(1, 6)
    num_tot1 = first + second
    print('You have points %d here' % num_tot1)
    print_the_fig(first)
    print_the_fig(second)
    
    needs_go_on = False
    if num_tot1 == 7 or num_tot1 == 11:
        print('You win %d !' % debt)
        money += debt
    elif num_tot1 == 2 or num_tot1 == 3 or num_tot1 == 12:
        print('The banker win, you lose %d !' % debt)
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        roll_str = input("----> roll a dice >----")
        first = randint(1, 6)
        second = randint(1, 6)
        current = first + second
        print('You have points %d here' % current)
        print_the_fig(first)
        print_the_fig(second)

        if current == 7:
            print('The banker win, you lose %d !' % debt)
            money -= debt
            needs_go_on = False
        elif current == num_tot1:
            print('You win %d !' % debt)
            money += debt
            needs_go_on = False
    
    return money
        

if __name__ == "__main__":
    money = 1000
    print("************* Small gambling game ******************")
    game_help()
    print("***===>begin game, you have money: %d >===***" % money)

    continue_flag = True
    while money > 0 and continue_flag:
        money = main_game(money)
        
        print('You still have money: %d ' % money)
        str_in = str(input("Will you continue(Y/N)?"))
        if "n" in str_in.lower():
            continue_flag = False
        if "h" in str_in.lower():
            game_help()

    if not continue_flag:
        print("You have quited the game. You still have money: %d" % money)
    elif money <= 0:
        print("You have break down! Game over!")
        
