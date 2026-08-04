import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False #显示负号



#图形基本构成
#---------------------------------------------------------------------------------
#Figure 画布：整个窗口或图像
#Axes 绘图区：包含坐标轴/标题/数据的区域
#Axis 坐标轴：x轴/ y轴



#准备数据
x = np.linspace(0,2*np.pi,50)
y = np.sin(x)

#绘图
# plt.plot(x,y,'r-o', label='sin(x)') #label标准图例 r-o红色的点
# plt.plot(x,y,'r-', label='sin(x)') #label标准图例  r-红色的线
plt.plot(x,y,'r-s', label='sin(x)') #label标准图例 r-红色的方块

#美化/标注
plt.title('正弦函数图像')
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.legend() #必须调用legend()才能显示图例
plt.grid()

#显示/保存图形
plt.show()

