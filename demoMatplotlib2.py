import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#中文显示与全局设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False #显示负号



#核心中的核心——plt与ooapi
#--操作                                --语法                               --适用场景                                        --掌握程度
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#pyplot                            plt.plot(x,y)                      快速探索数据/绘制简单图表或交互式分析                     弱，操作基于“隐含”的当前图形和轴  
#ooapi创建'Figure'画布           plt.figure(figsize=(10, 8))           构建复杂图标/多子图布局及生产级应用代码                   强，适合构建复杂夺标/多子图布局及生产级应用代码
#ooapi创建'Axes'绘图区对象        fig.add_subplot(1, 1, 1)



#折线图 plt.plot(x,y)  #折线图
#----------------------------------------------
#展示数据随时间或连续变量的变化趋势，只管表达数据波动/上升或下降的整体走向，时间序列分析的核心图标
# x = np.arange(0, 3*np.pi, 0.1)
# y1,y2 = np.sin(x), np.cos(x)
# plt.plot(x, y1, 'b-', linewidth=2, label='sin') #折线图
# plt.plot(x, y2, 'r--', linewidth=2,label='cos') #折线图
# plt.title('正弦函数与余弦函数图像')     
# plt.legend(loc='best') #必须调用legend()才能显示图例
# plt.show()

#折线画圆
# theta = np.linspace(0, 2*np.pi, 200)
# plt.plot(np.cos(theta), np.sin(theta), 'y--', linewidth=2, label='圆形') #折线图
# plt.axis('equal') #x y轴比例相等
# plt.show()

#折线——直线
# plt.plot([1,2,3,4],[3,6,9,12], 'g--', linewidth=2, label='直线') #折线图
# plt.show()



#散点图 plt.scatter(x,y)  #散点图
#----------------------------------------------
#展示两个变量之间的关系，判断是否存在相关性，相关性强弱/正负相关性，散点图的点越密集，相关性越强
#通过点的颜色(c)或大小(s)，可同时展示第三或第四维度的数据，信息密度极高

# np.random.seed(0) #设置随机种子，保证每次生成的随机数相同
# x,y =np.random.rand(100), np.random.rand(100)
# colors = np.random.rand(100) #点的颜色
# sizes = 300 * np.random.rand(100) #点的大小

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.8, cmap='viridis') #alpha透明度
# plt.colorbar() #显示颜色条
# plt.title('散点图示例')
# plt.show()



#条形图 plt.bar(x,y)  
#----------------------------------------------
#适用于比较不同分类数据的数值大小，只管展示各类别间的差异
# classes = ['A班', 'B班', 'C班', 'D班']
# scores = [85, 90, 78, 92]

## plt.bar(classes, scores, color='skyblue', edgecolor='black')
# plt.barh(classes, scores, color='skyblue', edgecolor='black')
# plt.title('各班成绩比较')
# plt.xlabel('班级')
# plt.ylabel('成绩')
# plt.show()



#饼图 plt.pie(x,y)  
#----------------------------------------------
#适用于展示各部分占整体的比例构成，清晰反映局部与整体的关系
# sizes = [25, 30, 20, 25]
# labels = ['优', '良', '中', '差']

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title('成绩分布饼图')
# plt.axis('equal') #保持饼图为圆形
# plt.show()



#直方图 plt.hist(x,y)  
#----------------------------------------------
#展示数据的分布情况，不同区间的出现频率
#班级成绩的分数段分布
#不同年龄段人群的身高分布
# data = np.random.randn(1000) #生成1000个随机数
# plt.hist(data, bins=30, color='lightblue', edgecolor='black') 
# plt.xlabel('值')
# plt.ylabel('频数')
# plt.show()



#箱线图 plt.boxplot(x,y)  
#----------------------------------------------
#比较不同组数据的分布，发现异常值
#清晰展示中位数/四分位数及离群点
#多组数据差异对比分析
# data = [np.random.normal(70, 15, 100),
#         np.random.normal(75, 17, 100),
#         np.random.normal(80, 20, 100)
# ]
# plt.boxplot(data, tick_labels=['A班', 'B班', 'C班'], patch_artist=True)
# plt.ylabel('成绩')
# plt.show()






#子图布局 Subplots(x,y)  
#----------------------------------------------
#多组数据或再一张画布上综合展示不同维度信息
#画布分割为多个区域来绘制图表：子图
# x = np.array([1,4,6,7,3,5,8,9])
# y1 = np.array([2,8,12,14,6,10,16,18])
# y2 = np.array([1,3,5,7,9,11,13,15])
# y3 = np.array([5,10,15,20,25,30,35,40])
# y4 = np.array([3,6,9,12,15,18,21,24])

# #基础方式：方法1
# plt.subplot(2, 2, 1) #2行2列第1个子图
# plt.plot(x, y1)
# # plt.show()

# plt.subplot(2, 2, 2) #2行2列第2个子图
# plt.scatter(x, y2)
# plt.show()



#面向对象的方法 方法2
# fig, axes = plt.subplots(2, 2, figsize=(10, 8)) #2行2列子图 fig：画布   Axes：绘图区对象
# axes[0, 0].plot(x, y1)
# axes[0, 1].scatter(x, y2)
# axes[1, 0].bar(x, y3)
# axes[1, 1].hist(x, y4)
# plt.tight_layout() #自动调整子图间距
# plt.savefig('subplots_example.png', dpi=300, bbox_inches='tight') #保存图像
# plt.show()

# #读取
# img = plt.imread('subplots_example.png') #读取图像
# print(type(img)) #<class 'numpy.ndarray'>
# print(img.shape)
# plt.imshow(img) #显示图像
# plt.axis



#面向对象的使用方式
# fig = plt.figure(figsize=(10, 8)) #创建画布
# ax = fig.add_subplot(1, 1, 1) #创建绘图区——布局
# ax.plot(x, y1, 'r-', linewidth=2) #绘制折线图
# ax.set_title('折线图示例', fontsize=16) #设置标题
# plt.show()

# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# y2 = np.cos(x)

# fig = plt.figure(figsize=(8,6))
# ax1 = fig.add_subplot(1, 2, 1)
# ax1.plot(x, y, 'r-')
# ax1.set_title('面向对象绘图')
# ax2 = fig.add_subplot(1,2,2)
# ax2.scatter(x, y2)
# plt.show()



# #3D散点图
# np.random.seed(42)         #随机种子，保证可重复性  
# n = 100                    #点的数量
# x = np.random.rand(n) * 10 #x坐标
# y = np.random.rand(n) * 10 #y坐标
# z = np.random.rand(n) * 10 #z坐标
# colors = np.random.rand(n) #颜色值
# sizes = np.random.rand(n) * 100 #点大小

# #绘图
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# sc = ax.scatter(x, y, z, c = colors, s = sizes, cmap='viridis', alpha = 0.8)

# #添加颜色条
# plt.colorbar(sc, label='颜色值')
# ax.set_xlabel('X')
# ax.set_xlabel('Y')
# ax.set_xlabel('Z')
# plt.show()



# np.random.seed(42)
# #控制np随机数生成器 相同的种子数意味着每次运行代码生成的随机数一致

# df = pd.DataFrame({
#     '班级': np.random.choice(['A班','B班','C班']), #从选项中随机抽样
#     '数学': np.random.normal(70, 10, 150).clip(0, 100), #生成连续浮点数，高斯分布 均值/标准差[2/3的样本集中在60-80之间]/正态分布 截断上下边界
#     '语文': np.random.normal(68, 12, 150).clip(0, 100), #clip防止数字越界
#     '英语': np.random.normal(72, 11, 150).clip(0, 100)
# })

# df['总分']  = df[['数学', '语文', '英语']].sum(axis=1)
# print(f'df\n{df}')

# #创建画布和子图【箱线图】
# fig = plt.figure(figsize=(14, 10))

# #1.箱线图
# ax1 = fig.add_subplot(2, 2, 1)
# ax1.boxplot([df['数学'], df['语文'], df['英语']], label=['数学','语文','英语'], patch_artist=True) 
# ax1.set_title('各科成绩分布')
# ax1.set_ylabel('分数')

# #2.总分直方图
# ax2 = fig.add_subplot(2, 2, 2)
# ax2.hist(df['总分'], bins=20, color='lightgreen', edgecolor='black')
# ax2.set_title('总分分布')
# ax2.set_xlabel('总分')

# #3.班级平均分条形图
# ax3 = fig.add_subplot(2,2,3)
# mean_scores = df.groupby('班级')['总分'].mean()
# ax3.bar(mean_scores.index, mean_scores.values, color='skyblue', edgecolor='black')
# ax3.set_title('各班平均总分')
# ax3.set_ylabel('平均总分')

# #4.数学-语文散点图
# ax4 = fig.add_subplot(2,2,4)
# ax4.scatter(df['数学'],df['语文'], alpha=0.6, c='coral')
# ax4.set_title('数学 VS 语文')
# ax4.set_xlabel('数学成绩')
# ax4.set_ylabel('语文成绩')

# plt.tight_layout()
# plt.savefig('成绩分布报告.png', dpi=150, bbox_inches='tight')
# plt.show()



np.random.seed(51)
df = pd.DataFrame({
    '班级': np.random.choice(['A班','B班','C班'], 150),
    '数学': np.random.normal(70, 10, 150).clip(0, 100),
    '语文': np.random.normal(68, 12, 150).clip(0, 100),
    '英语': np.random.normal(72, 11, 150).clip(0, 100)
})
#DataFrame中 size需要保持统计，这样数据量才能统一

df['总分'] = df[['数学','语文','英语']].sum(axis=1) #axis=1——>按行求和 axis=0——>按列求和

fig = plt.figure(figsize=(14,10))

ax1 = fig.add_subplot(2, 2, 1)
ax1.boxplot([df['数学'], df['语文'], df['英语']], label=['数学','语文','英语'], patch_artist=True)
ax1.set_title('各科成绩分布')
ax1.set_ylabel('分数')

#总分
ax2 = fig.add_subplot(2, 2, 2)
ax2.hist(df['总分'], bins=20, color='lightgreen', edgecolor='black') #bins表示多少个柱子，这里是将数据分为20份，20个柱子
ax2.set_title('总分分布')
ax2.set_ylabel('总分')

#平均分
ax3 = fig.add_subplot(2, 2, 3)
mean_scores = df.groupby('班级')['总分'].mean()
ax3.bar(mean_scores.index, mean_scores.values, color='skyblue', edgecolor='black')
ax3.set_title('各班平均总分')
ax3.set_ylabel('平均总分')

#语文VS数学 比对
ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(df['数学'],df['语文'],alpha=0.6, c='coral')
ax4.set_title('数学 VS 语文')
ax4.set_xlabel('数学成绩')
ax4.set_ylabel('语文成绩')

plt.tight_layout()
plt.show()



#绘制一条二次函数曲线(y = x平方)， x范围[-5, 5]，线为蓝色虚线，标记点为红色圆点，并添加标题和坐标轴标签
# x = np.linspace(-5, 5, 20)
# y = x * 2
# plt.plot(x, y, 'b--o', markerfacecolor='red')
# plt.title('二次函数 y = x^2')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# x = np.linspace(-5, 5, 30)
# y = x * 2
# plt.plot(x, y, 'b--o', markerfacecolor='red')
# plt.title('二次函数 有= 2x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()



#y永远在[-1, 1]之间波动，最高1，最低-1
#周期 每个2pi 约等于 6.28，波形重复一遍
#对称 光华波浪，无限向左右一直延伸
# fig,(ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
# x = np.linspace(0, 2 * np.pi, 100) #返回指定区间内均匀分布的数值。

# ax1.plot(x, np.sin(x))
# ax1.set_title('sin(x)')
# ax2.plot(x, np.cos(x), 'r')
# ax2.set_title('cos(x)')
# plt.show()



# fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2,3, figsize=(10, 3))
# fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(10, 3))
# x = np.linspace(0,2 * np.pi)  #0到6.28的完整区间
# ax1.plot(x, np.sin(x))
# ax1.set_title('sin(x)')
# ax2.plot(x, np.cos(x))
# ax2.set_title('cons(x)')
# ax3.scatter(x, np.cos(x))
# plt.show()



#读取iris数据集，绘制花瓣长与宽的散点图，按品种不同着色，并添加颜色条和图例
# df = pd.read_csv('iris.csv', names=['花萼长','花萼宽','花瓣长', '花瓣宽', '种类'], header=0)
# species_map = {'setosa':0, 'versicolor':1, 'virginica':2}
# df['类型'] = df['种类'].map(species_map)
# print(f'dfall:\n{df}')

# # print(f'类型：{df['类型']}')

# colors = df['类型']
# plt.scatter(df['花瓣长'], df['花瓣宽'], c=colors, cmap='Set1', alpha=0.5)
# plt.colorbar(label='种类') #颜色调
# plt.xlabel('花瓣长(cm)')
# plt.ylabel('花瓣宽(cm)')
# plt.show()


