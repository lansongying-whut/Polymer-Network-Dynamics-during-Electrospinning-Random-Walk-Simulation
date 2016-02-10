# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import random

chain_num = 1
monomer_num = 10000
bond_len = 0.1

# 拉力
fz = float(raw_input('请输入fz的值: '))
# z轴方向正负概率
Pzplus = np.exp(fz)/(np.cosh(fz)+2)/2
Pzminus = np.exp(-fz)/(np.cosh(fz)+2)/2
# 横向之间概率相同
Pother = 1/(np.cosh(fz)+2)/2
some_list = [0, 1, 2, 3, 4, 5]
probabilities = [Pother, Pother, Pother, Pother, Pzplus, Pzminus]

# 以指定概率取值
def random_pick(some_list, probabilities):
    x = random.uniform(0,1) # 返回(0, 1)之间的浮点数
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:break
    return item

def gen_line(monomer_num, dims=2):
    line_data = np.zeros((dims, monomer_num))
    line_data[:, 0] = [0, 0, 0]
    for i in range(1, monomer_num):
        dir = random_pick(some_list, probabilities)
        # dir = np.random.randint(0,6)
        if dir == 0:
            step = [bond_len, 0, 0]
        if dir == 1:
            step = [-bond_len, 0, 0]
        if dir == 2:
            step = [0, bond_len, 0]
        if dir == 3:
            step = [0, -bond_len, 0]
        if dir == 4:
            step = [0, 0, bond_len]
        if dir == 5:
            step = [0, 0, -bond_len]
        line_data[:,i] = line_data[:, i-1] + step
    return line_data

def update_line(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data = [gen_line(monomer_num, 3) for index in range(chain_num)]
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
ax.set_xlim3d([0.0, 1.0])
ax.set_ylim3d([0.0, 1.0])
ax.set_zlim3d([0.0, 1.0])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
line_ani = animation.FuncAnimation(fig, update_line, monomer_num, fargs=(data, lines), interval=10, repeat=False, blit=False)
plt.show()
