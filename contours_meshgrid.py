import matplotlib.pyplot as plt
import numpy as np


# contours:等高线、轮廓

def f(x,y):
	return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
	
n=256
x=np.linspace(-3,3,n)		# x是数组类型array，不是列表类型
y=np.linspace(-3,3,n)

#将两个一维数组x,y变为两个二维矩阵，分别赋值给X,Y。注意np.meshgrid()的返回值是一个包含两个元素的列表，每个元素是数组类型，并且两个数组维度一样
# np.meshgrid()函数的作用是为了对x和y的每个元素两两之间，都配一个坐标对。两个数组维度相同，则其中一个数组的每个元素与另一数组对应元素配对，正好全部配对
# https://blog.csdn.net/grey_csdn/article/details/69663432
X,Y=np.meshgrid(x,y)  # 把x,y绑定为网格的输入值   mesh:网  meshgrid:网格



# 填充等高线区域，并没有画等高线
# 下面的这个8，是表示设置多少个等高线，0的话有两个等高线，8的话就有10个等高线
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)		# contourf(X,Y,Z)			cmap=plt.cm.cool表示冷色调

# 画等高线
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=5)

#对等高线加上数字描述  clabel即contour-label
plt.clabel(C,inline=True,fontsize=10)		# inline是True的话，就是描述的字体嵌入等高线中，如果为False的话，等高线就直接穿过字体，比较丑

plt.xticks(())
plt.yticks(())
plt.show()