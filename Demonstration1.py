import numpy as np
import matplotlib.pyplot as plt

x = int(input("请输入迭代次数: "))

# 定义单位矩阵E和矩阵P
E = np.array([[1, 0], [0, 1]])
P = np.array([[0, -1], [1, 0]])
vector = np.array([2, 2])

# 函数用于计算给定n的(E + (1/n * P))^n * vector
def calculate_vector_updated(n):
    if n != 0:
        return np.linalg.matrix_power(E + (1 / x) * P, n) @ vector
    else:
        return vector  # 当n为0时，结果是原始向量

# 计算从0到x的n的向量
n_values_updated = range(x + 1)
vectors_updated = [calculate_vector_updated(n) for n in n_values_updated]

# 每个向量的颜色
color_cycle = plt.cm.viridis(np.linspace(0, 1, x + 1))

# 用不同颜色绘制
plt.figure(figsize=(10, 8))
for n, v, color in zip(n_values_updated, vectors_updated, color_cycle):
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=color, label=f'n={n}')

# 调整坐标轴限制
plt.xlim(-1, 2.5)
plt.ylim(0, 3.3)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('The vector (E + (1/n * P))^n * [2, 2], as n varies from 0 to x, each represented in a different color.')
plt.show()
