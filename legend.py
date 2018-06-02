
import matplotlib.pyplot as plt
import numpy as np

# legend:图例

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num=3, figsize=(8, 5))

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel("X-label")
plt.ylabel("Y-label")

new_ticks = np.linspace(-1, 2, 5)  # ticks指的是坐标轴的小标
print(new_ticks)
plt.xticks(new_ticks)

# 被$ $包起来的部分是为了使得字体更好看，数学字体，有空格的需要使用\转义空格.并且\alpha 可以变成字符.  前面加上r表示读取为原始字符串
plt.yticks([-2,-1,0,1,2,3],['a','b',r'$c$',r'd','$you\ are\ cool$',r'$\alpha$'])	

# # method 1
# plt.plot(x, y2,label='up')		# 这里的label的值是legend的名称
# plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--',label='down')
# plt.legend()


# # method 2
l1, = plt.plot(x, y2,label='up')		# plt也是有返回值的。注意l1后面的逗号不能少
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--',label='down')
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')		# loc可取'best'，'upper right'等等。labels和上面的label一样的作用，只不过这里是复数加s。上面如果设置了label，这里会覆盖上面设置的。

plt.show()
