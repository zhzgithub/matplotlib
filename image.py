import matplotlib.pyplot as plt
import numpy as np

# image data
# a = np.array([0.3,0.6,0.9,0.3,0.6,0.9,0.3,0.6,0.9]).reshape(3,3)
a = np.array([30,120,90,100,10,60,30,150,200]).reshape(3,3)

# plt.imshow(a)
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
# plt.colorbar()		# 色度条
plt.colorbar(shrink=0.9)		# shrink=0.9是压缩色度条0.9倍长宽，		shrink:收缩

plt.xticks(())
plt.yticks(())
plt.show()