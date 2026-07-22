count = 0;

def fun():
    global count;#修改全局变量的语法声明
    count +=1

fun();
fun();
print(f"count:{count}");



msgs = ['a','b','c'];

#可变类型对象直接追加【修改/删除/新增】不需要使用global声明
def fun2():
    msgs.append('d');

fun2();
print(f"msgs:{msgs}");

#没有使用global msgs；所以对msgs引用的改动不生效
def fun3():
    msgs2 = ['y','z','x','w']
    msgs = msgs2;

fun3();
print(f"msgs:{msgs}");

def fun4():
    msgs2 = ['y','z','x','w']
    global msgs;
    msgs = msgs2;

fun4();
print(f"msgs:{msgs}");









