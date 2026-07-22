import random

target = random.randint(1, 100)
#while else的情况容易被忽略
attempts = 0
max_attempts = 7
while attempts < max_attempts:
    guess = int(input(f"猜数字1-100(剩余{max_attempts - attempts}次机会): "))

    match(guess > target, guess < target):#元组作为入参
        case (True, _):
            print("太大了")
        case (_, True):
            print("太小了")
        case _:
            print("恭喜你，猜对了！")
            break #结束while循环

    attempts+=1
else:
    print(f"游戏结束，正确答案是 {target}")
