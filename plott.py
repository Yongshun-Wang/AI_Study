import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) # 以0.1 为单位，生成0 到6 的数据 
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形 
plt.plot(x, y1, label="sin") 
plt.plot(x, y2, linestyle = "--", label="cos") # 用虚线绘制 
plt.xlabel("x") # x 轴标签 
plt.ylabel("y") # y 轴标签 
plt.title('sin & cos') # 标题 
plt.legend() 
plt.show()