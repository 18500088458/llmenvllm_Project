import asyncio

#全局事件：初始化完成信号
init_done = asyncio.Event()

#初始化
async def initializer():
    '''模拟初始化过程'''
    print('开始初始化')
    await asyncio.sleep(7)
    print('初始化完成')
    init_done.set() #发送信号：初始化完成

#工人
async def worker(name:str):
    '''工作协程，等待初始化完成'''
    print(f'{name} 等待初始化...') 
    await init_done.wait() #阻塞，知道event.set()
    print(f'{name} 开始处理任务')   

async def main():
    tasks = [
        asyncio.create_task(initializer()),
        asyncio.create_task(worker('worker-A')),
        asyncio.create_task(worker('worker-B')),
        asyncio.create_task(worker('worker-C')),
        asyncio.create_task(worker('worker-D'))
    ]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())