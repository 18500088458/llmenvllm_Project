import asyncio
import time

async def worker(name, delay):
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 完成")
    return f"结果——{name}"

async def main():
    #将协程包装成任务，立即开始调度
    task_two = asyncio.create_task(worker("two",2))
    task_one = asyncio.create_task(worker("one",1))
    task_oneHalf = asyncio.create_task(worker("oneHalf",1.5))

    print("主协程在干别的事...")

    #最后再等待任务完成并获取结果 结束/状态/撤销控制
    result_two = await task_two
    result_one = await task_one
    result_oneHalf = await task_oneHalf
    print(result_two,result_one,result_oneHalf)

#协程调用
print(f'开始{time.strftime('%X')}')
asyncio.run(main())
print(f'结束{time.strftime('%X')}')
