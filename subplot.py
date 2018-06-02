import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# # method 0
plt.figure(1)

plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

plt.subplot(234)
plt.plot([0,1],[0,3])

plt.subplot(2,3,5)
plt.plot([0,1],[0,5])

plt.subplot(236)
plt.plot([0,1],[0,1])

# plt.show()

# method 1:subplot2grid
plt.figure(2)
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)		# (3,3)三行三列，从(0,0)开始，后面俩参数是列和行的跨度
ax1.plot([1,2],[1,2])
ax1.set_title("ax1_title")		# plt.xlabel(),plt.title(),plt.xlim()在这里都变成了ax1.set_xlabel(),ax1.set_title(),ax1.set_xlim(),因为ax1是一个axis,而不是一个figure
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)		# (3,3)三行三列，从(1,0)开始，后面俩参数是列和行的跨度,不设置就默认1
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)		# (3,3)三行三列，从(1,2)开始，后面俩参数是列和行的跨度,不设置就默认1
ax4 = plt.subplot2grid((3,3),(2,0))		# (3,3)三行三列，从(2,0)开始，后面俩参数是列和行的跨度,不设置就默认1
ax5 = plt.subplot2grid((3,3),(2,1))		# (3,3)三行三列，从(2,1)开始，后面俩参数是列和行的跨度,不设置就默认1

# plt.show()

# method 2:gridspec
plt.figure(3)
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])

# plt.tight_layout()
# plt.show()

# method 3:easy to define structure
# plt.figure(4)
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)		#注意，这里是subplots,不是subplot,多了个s。  sharex=True共享x轴
ax11.scatter([1,2],[1,2])		# 散点(1,1),(2,2)

# plt.tight_layout()
plt.show()