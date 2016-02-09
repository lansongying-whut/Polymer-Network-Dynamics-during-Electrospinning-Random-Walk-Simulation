import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

chain_num = 10
monomer_num = 2000
bond_len = 0.1

def gen_line(monomer_num, dims=2):
    line_data = np.zeros((dims, monomer_num))
    line_data[:, 0] = [0, 0, 0]
    for i in range(1, monomer_num):
        dir = np.random.randint(0,6)
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
line_ani = animation.FuncAnimation(fig, update_line, monomer_num, fargs=(data, lines), interval=30, blit=False)
plt.show()
