score = float(input("请输入成绩（0-100）："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

print(f"成绩为 {score}，等级为 {grade}")

#三元表达式
num = 20
result = "偶数" if num % 2 == 0 else "奇数"
print(result)  # Output: 偶数   


#match-case 模式匹配
month = int(input("请输入月份（1-12）："))

match month:
    case 3 | 4 | 5:
        print("春季")
    case 6 | 7 | 8:
        print("夏季")
    case 9 | 10 | 11:
        print("秋季")
    case 12 | 1 | 2:
        print("冬季")
    case _:#通配符 匹配任意情况
        print("无效的月份")

age = int(input("请输入年龄："))

match age:
    case 0 | 1 | 2:
        print("婴儿")
    case 3 | 4 | 5 | 6:
        print("幼儿")
    case 7 | 8 | 9 | 10:
        print("儿童")
    case _ if age >= 11 and age <= 17:
        print("青少年")
    case _ if age >= 18 and age <= 64:
        print("成年人")
    case _ if age >= 65:
        print("老年人")
    case _:
        print("无效的年龄")





