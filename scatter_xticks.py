import matplotlib.pyplot as plt
import numpy as np

# scatter:散点图

n=1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)		# 颜色的公式，为了让散点图更好看，记住就行了

plt.scatter(X,Y,s=75,c=T,alpha=0.5)		# s即size，c即color,cmap即colormap颜色映射，alpha即透明度
# plt.scatter(np.arange(5),np.arange(5),s=100)		# arange函数用于创建等差数组,np.arange(5)即生成等差数组[0 1 2 3 4]
plt.xlim((-5,5))
plt.ylim((-5,5))
plt.xticks(())		#把刻度标注给隐藏起来。。。注意这里不是xlabel,xlabel是x轴表示的什么内容，xtick是x轴刻度标注
plt.yticks(())		# 注意这里是双括号，千万别忘了而只写了一个括号



plt.show()