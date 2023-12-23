import numpy as np
import matplotlib.pyplot as plt

# 获取 k 和 m 的值
k = float(input("Enter the value of k: ")) 
m = float(input("Enter the value of k: "))

# 定义方程组
def system(Y):
    y, v = Y
    return [v, -k/m * y]

# 创建网格
Y, V = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))

# 在每个网格点计算导数
U, W = np.zeros(Y.shape), np.zeros(V.shape)
for i in range(len(Y)):
    for j in range(len(V)):
        y = Y[i, j]
        v = V[i, j]
        Yprime = system([y, v])
        U[i, j] = Yprime[0]
        W[i, j] = Yprime[1]

# 规范化箭头
N = np.sqrt(U**2 + W**2)
U, W = U/N, W/N

# 自动计算颜色变化范围
# 绘制方向场
plt.quiver(Y, V, U, W, N, angles='xy', cmap=plt.cm.viridis, scale=35)  # Keeping scale to shorten arrow length
plt.xlabel('x')
plt.ylabel('v')
plt.title(f'Colored Direction Field for a + {k}/{m} x = 0')
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.colorbar(label='Arrow Magnitude')
plt.grid()
plt.show()
