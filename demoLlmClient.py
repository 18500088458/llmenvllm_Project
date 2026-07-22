import os
import requests

class LLMClient:
    def __init__(self, api_key=None, base_url="https://api.siliconflow.cn/"):
        api_key = api_key or os.getenv("SILICONFLOW_API_KEY")
        if not api_key:
            raise ValueError("请先设置 SILICONFLOW_API_KEY 环境变量，或传入 api_key 参数")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def chat(self, model, messages):
        """一个简单的聊天请求函数，包含完整的异常处理"""
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model,
            "messages": messages,
        }

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.Timeout:
            print("错误：请求大模型超时，请重试。")
        except requests.exceptions.HTTPError as e:
            response_text = e.response.text if e.response is not None else ""
            print(f"HTTP 错误：{e} {response_text}")
        except Exception as e:
            print(f"未知错误：{e}")
        return None


# 测试代码
if __name__ == "__main__":
    client = LLMClient("sk-jirqhyzpjvusiyrjtaaiapwlcoqhrccyomlibchwhbtbcgzd")
    resp = client.chat(
        model="Qwen/Qwen3.5-122B-A10B",
        messages=[
            {"role": "system", "content": "你是一个有用的助手x"},
            {"role": "user", "content": "你好，请介绍一下你自己"},
        ],
    )

    if resp:
        print("请求成功！")
        print(resp["choices"][0]["message"]["content"])
    else:
        print("请求失败，已经进行错误处理")
