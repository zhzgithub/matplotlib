# 主次坐标轴
# 本例讲的是共用x坐标轴，而y坐标轴不同

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 = -1*y1

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()		# 用镜面的效果把ax1颠倒过来赋给ax2
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'r--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color='g')
ax2.set_ylabel('Y2',color='r')

plt.show()