import time
import functools

def timer(func):
    '''计时装饰器，可以装饰在任何函数上'''
    @functools.wraps(func)#保留原函数的函数名/文档等元信息
    def wrapper(*args, **kwargs):
        start = time.perf_counter() #装饰的部分
        result = func(*args, **kwargs) #执行原始函数
        cost = time.perf_counter() - start #装饰的部分

        print(f"[计时]{func.__name__} 耗时：{cost:.4f} 秒")
        return result
    
    return wrapper

#该函数使用了timer装饰器
@timer 
def process_data():
    time.sleep(3)
    return "处理完成"

#调用时自动即时
process_data()

@timer
def baize():
    print("我是白泽，我在测试计时器")
    print("现在消耗了多少时间？")

baize()   


'''重试装饰器'''
def retry(max_attempts=3):
    #带参重试装饰器【重试次数】
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for at in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"重试{at}/{max_attempts} 失败：{e}")

            raise Exception(f"函数 {func.__name__} 重试{max_attempts}次后仍失败")        
        return wrapper
    return decorator

import random
@retry(max_attempts=5)
def unstable_network_call():
    if random.random() < 0.7:
        raise ConnectionError("网络抖动")
    return "数据获取成功"

print(unstable_network_call())



'''缓存装饰器'''
def cache(func):
    _cache = {}
    @functools.wraps(func)
    def wraps(*args):
        if args not in _cache:
            _cache[args] = func(*args) #第一次算，将值缓存起来
        return _cache[args] #有值直接返回
    return wraps

@cache
def expensive_computation(n):
    print(f"正在进行耗时操作花费{n}秒")
    time.sleep(n)
    return n * 2

print(expensive_computation(3))
print(expensive_computation(3))
