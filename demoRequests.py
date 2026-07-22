import requests

def fetch_weather(city):
    '''调用公共api获取天气(示例使用wttr.in)'''
    url = f"https://wttr.in/{city}?format=j1"
    resp = requests.get(url, timeout=5)
    if resp.status_code == 200:
        data = resp.json()
        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        return f"{city}:{temp}°C,{desc}"
    else:
        return f"网络请求失败"

tj = fetch_weather("天津")
print(tj)