#推导式 快速创建列表【列表/集合/字典推导式】
#语法糖

'''列表推导式'''
#传统写法
odds = []
for i in range(1, 11):
    if i % 2 == 1:
        odds.append(i)

print(odds)  # Output: [1, 3, 5, 7, 9]  

#列表推导式(声明式，更pythonic)
odds = [i for i in range(1, 11) if i % 2 == 1]
print(odds)  # Output: [1, 3, 5, 7, 9]

#嵌套循环推导式
ucc = [i+ j for i in 'ABCDE' for j in '甲乙丙丁']
print(ucc)  # Output: ['A甲', 'A乙', 'A丙', 'A丁', 'B甲', 'B乙', 'B丙', 'B丁', 'C甲', 'C乙', 'C丙', 'C丁', 'D甲', 'D乙', 'D丙', 'D丁', 'E甲', 'E乙', 'E丙', 'E丁']  



'''集合推导式'''
text = "hello world python programming"
vowels = {char for char in text if char in 'aeiou'}
print(vowels)  # Output: {'o', 'e', 'a', 'i



'''集合推导式'''
#生成立方映射
squares = {x:x**3 for x in range(1, 11)}#**3表示立方映射
print(squares)  # Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}

#反转键值对
ori = {'a': 1, 'b': 2, 'c': 3}
inv = {v: k for k, v in ori.items()}
print(inv)  # Output: {1: 'a', 2: 'b',



'''生成器表达式（惰性计算，节省内存）'''
#海量计算时使用生成器能显著节省内存
nums_list = [x*2 for x in range(1000000)]  # 列表推导式，生成一个包含100万个元素的列表
print(nums_list[:50])  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#生成器表达式，生成一个包含100万个元素的生成器对象:按需生成
nums_gen = (x*2 for x in range(1000000))
print(next(nums_gen))  # Output: 0
print(next(nums_gen))  # Output: 0
print(next(nums_gen))  # Output: 0
print(next(nums_gen))  # Output: 0
print(next(nums_gen))  # Output: 0


