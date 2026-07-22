import asyncio
import time

async def worker(name, delay):
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 完成")
    return f"结果——{name}"

async def main():
    #并发执行worker("A")贺worker("B")，总耗时取最长的时间
    results = await asyncio.gather(
        worker("two", 2),
        worker("one", 1),
        worker("oneHalf", 1.5)
    )
    print(results)
    #结果按照顺序打印

print(f"开始 {time.strftime('%X')}")
asyncio.run(main())
#使用的地方通过asyncio.run执行
print(f"结束 {time.strftime('%X')}")








