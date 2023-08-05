import numpy as np
import matplotlib.pyplot as plt

SIR = np.zeros((10, 3))
p = np.zeros((11, 3))
p[0] = np.array([1, 1, 1]) # the initial power
gain_matrix = np.array([[1, 0.1, 0.3], [0.2, 1, 0.3], [0.2, 0.2, 1]])
noise = np.array([0.1, 0.1, 0.1])
target = np.array([1, 1.5, 1])

for i in range(10): # ten iterations
    for j in range(3):
        SIR[i][j] = p[i][j] / (np.dot(gain_matrix[j], p[i]) + noise[j] - p[i][j])
        p[i+1][j] = target[j]*p[i][j] / SIR[i][j]

plt.subplot(2, 1, 1)
plt.title('transmit powers')
plt.xlabel('iterations') 
plt.ylabel('transmit powers')
plt.plot(p[:, 0], label='p1')
plt.plot(p[:, 1], label='p2')
plt.plot(p[:, 2], label='p3')
plt.legend()

plt.subplot(2, 1, 2)
plt.title('SIR')
plt.xlabel('iterations')
plt.ylabel('SIR')
plt.plot(SIR[0:, 0], label='SIR1')
plt.plot(SIR[0:, 1], label='SIR2')
plt.plot(SIR[0:, 2], label='SIR3')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

SIR = np.zeros((10, 4))
new_p = np.zeros((11, 4))
new_p[0] = np.append(p[10], 1)
new_gain_matrix = np.array([[1, 0.1, 0.3, 1], [0.2, 1, 0.3, 0.1], [0.2, 0.2, 1, 0.1], [0.1, 0.1, 0.1, 1]])
cal_matrix = np.array([[0, 0.1, 0.3, 1], [0.2, 0, 0.3, 0.1], [0.2, 0.2, 0, 0.1], [0.1, 0.1, 0.1, 0]])
noise = np.array([0.1, 0.1, 0.1, 0.1])
target = np.array([1, 1.5, 1, 1])

for i in range(10):
    for j in range(4):
        SIR[i][j] = new_p[i][j] / (np.dot(cal_matrix[j], new_p[i]) + noise[j]) / new_gain_matrix[j][j]
        new_p[i+1][j] = target[j]*new_p[i][j] / SIR[i][j]

plt.subplot(2, 1, 1)
plt.title('transmit powers')
plt.xlabel('iterations')
plt.ylabel('transmit powers')
x = np.array(list(range(11,21)))
plt.plot(x, new_p[1:, 0], label='p1')
plt.plot(x, new_p[1:, 1], label='p2')
plt.plot(x, new_p[1:, 2], label='p3')
plt.plot(x, new_p[1:, 3], label='p4')
plt.legend()

plt.subplot(2, 1, 2)
plt.title('SIR')
plt.xlabel('iterations')
plt.ylabel('SIR')
x = np.array(list(range(11,21)))
plt.plot(x, SIR[0:, 0], label='SIR1')
plt.plot(x, SIR[0:, 1], label='SIR2')
plt.plot(x, SIR[0:, 2], label='SIR3')
plt.plot(x, SIR[0:, 3], label='SIR4')
plt.legend()
plt.show()


