def load_config():
    pass

def speak():
    pass

count = 0

class BaiZe:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"学AI 找{self.name}")

#让if代码块里的内容只在直接运行该文件时才执行，当文件作为模块被导入时不执行
if __name__ == "__main__":
    b2 = BaiZe("张三", 25)
    b2.speak()




