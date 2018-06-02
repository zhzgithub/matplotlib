import matplotlib.pyplot as plt
import numpy as np

# bar:条形图或柱状图


n=12
X = np.arange(n)	# 生成[0 1 2 3 4 5 6 7 8 9 10 11]的一维数组shape为(12,)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)   # np.random.uniform(0.5,1.0,n)生成n个0.5到1之间的随机数值。一维数组相乘就是对应元素相乘,最后得到的还是一维数组
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n) 

# facecolor是主体的颜色，edgecolor是边框颜色
# plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,+Y1,facecolor='g',edgecolor='blue')		# 设置颜色设置为简写或者全称都可以
plt.bar(X,-Y2,facecolor='#661234',edgecolor='g')

for x,y in zip(X,Y1):		# zip()把X和Y1打包起来，分别传给x和y，如果不使用zip()的话，(X,Y1)就只会传给一个值。	
	plt.text(x+0.4,y+0.05,'%.2f'%y,ha='center',va='bottom')	# ha:horizontal alignment 水平对齐		ha='center'居中对齐  
																# va:竖直对齐   va='bottom'底部对齐	
																
for x,y in zip(X,Y2):		
	plt.text(x+0.4,-y-0.05,'-%.2f'%y,ha='center',va='top')	

plt.xlim(-0.5,n)
# plt.xticks(())		# 隐藏x轴刻度标注
plt.ylim(-1.25,1.25)
# plt.yticks(())		# 隐藏y轴刻度标注

plt.show()