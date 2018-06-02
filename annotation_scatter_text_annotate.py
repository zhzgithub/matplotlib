
import matplotlib.pyplot as plt
import numpy as np

# annotation：注解

x = np.linspace(-3, 3, 50)
y = 2 * x + 1


plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y)
# plt.scatter(x,y)	# 这样画出来的就是散点图，不是直线



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

x0 = 1
y0 = 2*x0+1
plt.scatter(x0,y0,s=50,color='r')	# 显示出一个点。s表示size
plt.plot([x0,x0],[y0,0],'r--',lw=2.5)		# 画出连接两个点的直线，注意这里两个中括号里面的并非表示坐标，只需要类比plt.plot(x,y)即可，即x=[x0,x0],y=[y0,0]
									# 因为第一个中括号里面的都是x，第二个中括号里面的都是y，所以两点为(x0,y0)和(x0,0)。

# # annotate:标注									
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
				fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
				
# text
plt.text(-3.7,3,r'$This\ is\ \sigma_i$',fontdict={'size':16,'color':'r'})

plt.show()
