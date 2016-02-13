# coding:utf8
import matplotlib.pyplot as plt
import numpy as np

# fz设置为拉伸应力
fz = np.linspace(0.0001, 6., 50)
const = np.linspace(1., 1., 50)

# Rz/Rmax = fz/3
gaussian = fz/3
rw = np.sinh(fz)/(np.cosh(fz)+2)
langevin = ((np.cosh(fz))/(np.sinh(fz))-1/fz)

plt.style.use('bmh')

# 拉力和伸长关系
plt.figure(1)
line1=plt.plot(fz, gaussian, 'b-o', label='Gaussian Chain')
line2=plt.plot(fz, rw, 'r-o', label='RW Chain')
line3=plt.plot(fz, langevin, 'g-o', label='Langevin Chain')
line4=plt.plot(fz, const, '--', color='#455667')
plt.ylim(0.0, 1.5)
plt.xlabel('Stretching force, '+r'$f_z$')
plt.ylabel('Relative elongation, '+r'$R_z/R_{max}$')
plt.title("Force-elongation Relation of a Freely-jointed Chain")
legend = plt.legend(bbox_to_anchor=(1,0.3), frameon=False)

# 拉力和方向概率关系
zplus = np.exp(fz)/(2*np.cosh(fz)+4)
zminu = np.exp(-fz)/(2*np.cosh(fz)+4)
pplus = 1/(2*np.cosh(fz)+4)
const2 = np.linspace(1./6., 1./6., 50)

plt.figure(2)
linep = plt.plot(fz, zplus, 'r-o', label=r"$+z$")
linem = plt.plot(fz, zminu, 'b-o', label=r"$-z$")
linepp = plt.plot(fz, pplus, 'g--', label=r"$+\rho$")
linepm = plt.plot(fz, pplus, 'r-', label=r"$-\rho$")
lineconst2 = plt.plot(fz, const2, '--', color='#455667')

plt.xlim(-0.1, 5.0)
plt.ylim(-0.1, 1.0)
plt.xlabel('Stretching force, '+r'$f_z$')
plt.ylabel('Stepping probabilities')
plt.title('Stepping probabilities along the z axis')
legend = plt.legend(bbox_to_anchor=(1,0.7), frameon=False)
plt.show()
