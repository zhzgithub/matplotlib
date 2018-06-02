
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel("X-label")
plt.ylabel("Y-label")

new_ticks = np.linspace(-1, 2, 5)  # ticks指的是坐标轴的小标
print(new_ticks)
plt.xticks(new_ticks)

# 被$ $包起来的部分是为了使得字体更好看，数学字体，有空格的需要使用\转义空格.并且\alpha 可以变成字符.  前面加上r表示读取为原始字符串
plt.yticks([-2,-1,0,1,2,3],['a','b',r'$c$',r'd','$you\ are\ cool$',r'$\alpha$'])	

# 'gca'='get current axis'
ax = plt.gca()
#spine 脊梁、脊椎，即图片的四个边框
ax.spines['right'].set_color('none')			# 把右边的边框去掉，即无色
ax.spines['top'].set_color('none')				# 把上边的边框去掉，即无色

ax.xaxis.set_ticks_position('bottom')		# 设置下面的坐标轴为默认的x轴
ax.yaxis.set_ticks_position('left')		# 设置左边的坐标轴为默认的y轴

# 挪动x、y轴的位置到（0,0）
ax.spines['bottom'].set_position(('data',0))		# 设置x轴的位置在y=0处
ax.spines['left'].set_position(('data',0))		# 设置x轴的位置在x=0处

plt.show()
