import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3*np.pi, 300)
y = np.sin(x)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(x, y)
ax1.set_xlim(min(x), max(x))
# plt.show()
plt.savefig('test_under.png')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.plot(x, y)
ax2.set_xlim(min(x), max(x))
ax2.xaxis.tick_top()
# plt.show()
plt.savefig('test_top.png')