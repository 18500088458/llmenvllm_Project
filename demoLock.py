#处理协程访问共享资源的场景，防止数据竞争 async with lock:上下文管理器语法
#买票场景
#协程互斥

import asyncio

# counter = 0

# async def increment():
#     global counter
#     temp = counter
#     await asyncio.sleep(0.1) #模拟io
#     counter = temp + 1

# async def main():
#     # tasks = [asyncio.create_task(increment()) for _ in range(8)]
#     tasks = [asyncio.create_task(increment()) for _ in range(5)]
#     await asyncio.gather(*tasks)
#     print(counter)

# asyncio.run(main())



# lock = asyncio.Lock()
# counter = 0

# async def increment():
#     global counter
#     async with lock:
#         temp = counter
#         await asyncio.sleep(0.1)
#         counter = temp + 1

# async def main():
#     # tasks = [asyncio.create_task(increment()) for _ in range(8)]
#     tasks = [asyncio.create_task(increment()) for _ in range(15)]
#     await asyncio.gather(*tasks)
#     print(counter)

# asyncio.run(main())
    


lock = asyncio.Lock()

async def write_log(msg:str):
    async with lock:
        with open("result.txt", "a", encoding="utf-8") as f:
            f.write(msg + '\n')

async def worker(name: str):
    for i in range(3):
        await asyncio.sleep(0.2)
        await write_log(f"{name} = line {i}")

async def main():
    await asyncio.gather(
        worker("A"),
        worker("B"),
        worker("C")
    )

asyncio.run(main())

    
