# coding:utf8
import matplotlib.pyplot as plt
import numpy as np

# fz设置为拉伸应力
fz = np.linspace(0., 6., 50)
const = np.linspace(1., 1., 50)

# Rz/Rmax = fz/3
gaussian = fz/3
rw = np.sinh(fz)/(np.cosh(fz)+2)
langevin = ((np.cosh(fz))/(np.sinh(fz))-1/fz)
line1=plt.plot(fz, gaussian, 'bo', label='Gaussian Chain')
line2=plt.plot(fz, rw, 'ro', label='RW Chain')
line3=plt.plot(fz, langevin, 'go', label='Langevin Chain')
line4=plt.plot(fz, const, '--', color='#455667')
plt.ylim(0.0, 1.5)
plt.xlabel('Stretching force, '+r'$f_z$')
plt.ylabel('Relative elongation, '+r'$R_z/R_{max}$')
plt.title("Force-elongation Relation of a Freely-jointed Chain")
legend = plt.legend(bbox_to_anchor=(1,0.25))
plt.show()
