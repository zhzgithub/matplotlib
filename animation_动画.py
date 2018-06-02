 
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib import animation		# animation:动画
import matplotlib.animation as ani

fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)		# 0~2*pi,步长为0.01的一维数组
line, = ax.plot(x,np.sin(x))

def animate(i):
	line.set_ydata(np.sin(x+i/10))
	return line,

def init():
	line.set_ydata(np.sin(x))
	return line,
	
ani = ani.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=False)

plt.show()

