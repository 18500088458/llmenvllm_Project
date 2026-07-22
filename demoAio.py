import asyncio
import time
import aiohttp

# 异步请求函数，接受session/url/sem[信号量]
async def fetch(session, url, sem):
    async with sem:#使用信号量限制并发
        try:
            async with session.get(url, timeout = 5) as resp:
                text = await resp.text()
                print(f"{url} 状态：{resp.status},长度：{len(text)}")
                return len(text)
        except Exception as e:
            print(f"{url} 异常：{e}")
            return 0

async def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/json",
        "https://www6.baidu.com",
    ]

    #信号量限制 3
    sem = asyncio.Semaphore(3)
    start = time.time()

    #aiohttp.ClientSession()：复用链接，提升性能 async with aiohttp 
    #asyncio.gather(*tasks)：用于将列表解包为多个参数
    #return_exceptions=True：某个任务失败不影响其他任务
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, sem) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions = True)

    print(f"总耗时：{time.time() - start:.2f} 秒")
    print("各页面大小：", results)

asyncio.run(main())
    
