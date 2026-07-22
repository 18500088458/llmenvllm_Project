print("100-999之间的水仙花数有：")
for num in range(100, 1000):
    # 分别获取百位、十位和个位数字
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10

    # 计算各位数字的立方和
    sum_of_cubes = hundreds**3 + tens**3 + units**3

    # 判断是否为水仙花数
    if sum_of_cubes == num:
        print(num)