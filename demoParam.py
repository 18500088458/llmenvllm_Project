def user_profile(name, age = 18, *hobbies, **kwargs):
    print(f"姓名：{name},年龄：{age}")
    if hobbies:
        print(f"爱好：{', '.join(hobbies)}")
    if kwargs:
        print(f"附加信息{kwargs}")

#调用上面的函数
user_profile("alice", 25, "阅读", "编程", city="北京", job="工程师")
user_profile("alice", "阅读2", "编程2", city="北京", job="工程师")

