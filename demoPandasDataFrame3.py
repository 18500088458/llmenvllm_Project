import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#快速生成图标
#pandas与matplotlib深度集成，无需复杂绘图设置，利用内置'plot()'方法，
#只需要一行代码可将DataFrame数据转换为直观的图表

#核心中的核心——快速生成图表
#--操作                       --语法                               --示例
#---------------------------------------------------------------------------------------
#line                       折线图 默认，展示趋势                                                      
#bar                        柱状图 比较分类数值                                                   
#pie                        饼图 展示部分占整体比例                              
#box                        线箱图 分析数据分布与离群值                       
#hist                       直方图（展示数据频率分布）   

df = pd.DataFrame({
    '姓名': ['张三','李四','王五', '同学1', '同学2', '同学3', '同学4', '同学5', '同学6', '同学7', '同学8', '同学9', '同学10'],
    '年龄': [18, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19],
    '成绩': [98, 89, 95, 65, 68, 45, 77, 75, 86, 22, 59, 43, 83]    
})

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False #显示负号

df['成绩'].plot(kind='line', title='成绩趋势', grid=True)
plt.show()

