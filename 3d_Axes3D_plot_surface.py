import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D			# axis的复数是axes,轴线

fig = plt.figure()
ax = Axes3D(fig)

# X,Y value
x = np.arange(-4,4,0.25)		# 步长0.25
y = np.arange(-4,4,0.25)
X,Y= np.meshgrid(x,y)		# X,Y 是同维度数组
R = np.sqrt(X**2 + Y**2)	# X**2 + Y**2也是数组，求平方根后还是数组

# height value
Z=np.sin(R)		# Z 也是数组，并且和X,Y同维度

# 在ax上面画，plot_surface()是画3D图像的函数
# rstride即row-stride,cstride即column-stride,即行和列的跨度，这里的行和列的跨度即是指网格的大小，并非按照坐标轴的大小比例
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))	# rainbow:彩虹
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')		# zdir='z'表示把图像映射到什么方向，offset是距离0位置的偏移
ax.set_zlim(-2,2)			# plt.zlim(-2,2),ax.zlim(-2,2)都不可行

plt.show()