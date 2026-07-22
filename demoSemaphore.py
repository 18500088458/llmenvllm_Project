import asyncio

#信号量：限制同时执行任务的协程数
sem = asyncio.Semaphore(2)

async def limited_task(name):
    #信号量：令牌桶
    async with sem:
        print(f"{name} 获得许可，开始执行")
        await asyncio.sleep(2)
        print(f"{name} 执行完毕，归还许可")

async def main():
    await asyncio.gather(
        limited_task("任务1"),
        limited_task("任务2"),
        limited_task("任务3"),
        limited_task("任务4"),
        limited_task("任务5"),
        limited_task("任务6")
    )

asyncio.run(main())
                