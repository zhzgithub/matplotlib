import matplotlib.pyplot as plt
import numpy as np
# 在图中画图
# ax1是大axes,		ax2和后面的plt.axes都是嵌入在ax1之中

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]
# x =np.array( [1,2,3,4,5,6,7] )
# y =np.array( [1,3,4,2,5,8,6] )

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])		# 添加一个axes,返回值赋给ax1，ax1的尺寸比例相对于整个figure是0.1,0.1,0.8,0.8
ax1.plot(x,y,'r')
plt.title('title')

# method 1
left,bottom,width,height = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])		# 添加一个axes,返回值赋给ax2，ax1的尺寸比例相对于ax1是0.1,0.1,0.8,0.8。注意，不是新打开一个figure，新打开一个figures是plt.figure()
ax2.plot(x,y,'b')
plt.title('title inside 1')

# method 2
plt.axes([.6,0.2,0.25,0.25])	# 添加一个axes,下面的语句都是针对于这个axes。注意，不是新打开一个figure，新打开一个figures是plt.figure()
plt.plot(y,x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()