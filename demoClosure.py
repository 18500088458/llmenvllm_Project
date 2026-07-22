request_count = 0 #全局变量

#计数器：单例模式写法
def track_request():
    global request_count
    request_count += 1
    print(f"api 调用次数：{request_count}")

track_request()
track_request()

#计数器：多实例模式【闭包-工厂函数】 python装饰器的基石
#闭包3要素
#1.函数嵌套
#2.内函数使用了外函数的变量 外函数显示定义需nonlocal，外函数的传参直接使用
#3.返回内函数
#把外函数理解为1个类 所以：one_count = create_count();只是创建实例
def create_count():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment;


#第一个实例
one_count = create_count()
print(one_count())
print(one_count())
print(one_count())
print(one_count())
print(one_count())

#第二个实例
two_count = create_count()
print(two_count())
print(two_count())
print(two_count())


#简易类
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

one_multiply = make_multiplier(3)
print(one_multiply(7))
print(one_multiply(9)) 


two_multiply = make_multiplier(5)
print(two_multiply(10))
print(two_multiply(20)) 

