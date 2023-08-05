# import numpy as np
# A = np.array([[1,0,0,0,0,1,0,0,0],
# [1,0,0,0,0,0,0,1,0],
# [1,0,0,0,0,0,0,0,1],
# [0,1,0,0,0,0,1,0,0],
# [0,1,0,0,0,0,0,1,0],
# [0,1,0,0,0,0,0,0,1],
# [0,0,1,0,0,1,0,0,0],
# [0,0,1,0,0,0,1,0,0],
# [0,0,1,0,0,0,0,1,0],
# [0,0,1,0,0,0,0,0,1],
# [0,0,0,1,0,1,0,0,0],
# [0,0,0,1,0,0,1,0,0],
# [0,0,0,1,0,0,0,0,1],
# [0,0,0,0,1,1,0,0,0],
# [0,0,0,0,1,0,1,0,0],
# [0,0,0,0,1,0,0,1,0]])
# B = A.T @ A
# I = np.linalg.pinv(B)
# X = I @ A.T
# c = np.array([1.875,1.875,0.875,-2.125,-2.125,0.875,0.875,-2.125,-1.125,0.875,-0.125,0.875,-0.125,-2.125,1.875,-0.125])
# output = X @ c
# print(output)

# R = [[5, 3.125, 5, 4],[3.125, 1, 1, 4],[4, 1, 2, 4],[3, 4, 3.125, 3],[1, 5, 3, 3.125]]
# Rbar = [[3.125, 3.125, 3.125, 3.125],[3.125, 3.125, 3.125, 3.125],[3.125, 3.125, 3.125, 3.125],[3.125, 3.125, 3.125, 3.125],[3.125, 3.125, 3.125, 3.125]]
# Bu = [1.5202, -1.2071, -0.3889,  0.0657,  0.0657]
# Bi = [-0.1907, -0.0088, -0.3725,  0.6275]
# for i in range(5):
#     for j in range(4):
#         Rbar[i][j] += Bu[i]+Bi[j]

# print(Rbar)

# import numpy as np
# import matplotlib.pyplot as plt
# A = np.array([[1, 0, 2],[1, 1, 0],[0, 2, 1],[2, 1, 1]])
# c = np.array([2, 1, 1, 3])
# I = np.identity(3)
# b_list=[]
# o_list=[]
# x=[]
# for i in range(0, 52, 2):
#     x.append(0.1*i)
#     B = A.T @ A + 0.1*i*I
#     In = np.linalg.pinv(B)
#     X = In @ A.T
#     output = X @ c
#     M = A@output-c
#     b_list.append(output.T @ output)
#     o_list.append(M.T @ M)
# print(b_list)
# plt.figure(figsize=(10,6),dpi = 100)
# plt.plot(x,o_list,color = 'green',linestyle = '-',label = r'$||Ab - c||_2^2$')
# plt.plot(x,b_list,color = 'r',linestyle = '-',label = r'$||b||_2^2$')
# plt.ylabel('Values')
# plt.xlabel(r'$\lambda$')
# plt.xticks(np.arange(0,5.2,0.2))
# plt.yticks(np.arange(0,2,0.1))
# plt.legend()
# plt.show()

import numpy as np
R3 = [[5,4.64,5,4],[1.72,1,1,4],[4,1,2,4],[3,4,3,3],[1,5,3,4]]

# R2 = np.array([[4.4545,1.7273,2.5455,3,3],[4.6364,1.9091,2.7273,3.1818,3.1818]])
R = [[4.45,4.64,4.27,5.27],[1.72,1.91,1.55,2.55],[2.55,2.73,2.36,3.36],[3.00,3.18,2.82,3.82],[3.00,3.18,2.82,3.82]]
for i in range(5):
    for j in range(4):
        R[i][j] -= 3.125
R = np.array(R)
r1 = R[:,0]
r2 = R[:,1]
r3 = R[:,2]
r4 = R[:,3]
dAB = (r1.T @ r2) / (np.linalg.norm(r1) * np.linalg.norm(r2))
dAC = (r1.T @ r3) / (np.linalg.norm(r1) * np.linalg.norm(r3))
dAD = (r1.T @ r4) / (np.linalg.norm(r1) * np.linalg.norm(r4))
dBC = (r2.T @ r3) / (np.linalg.norm(r2) * np.linalg.norm(r3))
dBD = (r2.T @ r4) / (np.linalg.norm(r2) * np.linalg.norm(r4))
dCD = (r3.T @ r4) / (np.linalg.norm(r3) * np.linalg.norm(r4))
print(dAB)
print(dAC)
print(dAD)
print(dBC)
print(dBD)
print(dCD)