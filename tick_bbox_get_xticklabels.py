
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 3, 50)
y = 0.1 * x 


plt.figure()
plt.plot(x, y,linewidth=10)
# plt.scatter(x,y)	# 这样画出来的就是散点图，不是直线
plt.ylim(-2,2)


# 'gca'='get current axis'
ax = plt.gca()
#spine 脊梁、脊椎，即图片的四个边框
ax.spines['right'].set_color('None')			# 把右边的边框去掉，即无色
ax.spines['top'].set_color('none')				# 把上边的边框去掉，即无色

ax.xaxis.set_ticks_position('bottom')		# 设置下面的坐标轴为默认的x轴
ax.yaxis.set_ticks_position('left')		# 设置左边的坐标轴为默认的y轴

# 挪动x、y轴的位置到（0,0）
ax.spines['bottom'].set_position(('data',0))		# 设置x轴的位置在y=0处
ax.spines['left'].set_position(('data',0))		# 设置x轴的位置在x=0处

for label in ax.get_xticklabels()+ ax.get_yticklabels():
	label.set_fontsize(12)
	label.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.9))   #alpha是透明度,facecolor是主体颜色，edgecolor是边框颜色

plt.show()
