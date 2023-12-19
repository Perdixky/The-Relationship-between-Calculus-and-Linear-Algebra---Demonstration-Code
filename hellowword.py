import numpy as np
import matplotlib.pyplot as plt

x = int(input("Enter the number of iterations: "))

# Define the identity matrix E and the matrix P
E = np.array([[1, 0], [0, 1]])
P = np.array([[0, -1], [1, 0]])
vector = np.array([2, 2])

# Function to calculate (E + (1/n * P))^n * vector for a given n
def calculate_vector_updated(n):
    if n != 0:
        return np.linalg.matrix_power(E + (1 / x) * P, n) @ vector
    else:
        return vector  # When n is 0, the result is the original vector

# Calculating vectors for n from 0 to x
n_values_updated = range(x + 1)
vectors_updated = [calculate_vector_updated(n) for n in n_values_updated]

# Colors for each vector
color_cycle = plt.cm.viridis(np.linspace(0, 1, x + 1))

# Plotting with different colors
plt.figure(figsize=(10, 8))
for n, v, color in zip(n_values_updated, vectors_updated, color_cycle):
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=color, label=f'n={n}')

# Adjust the axis limits based on the vectors
all_vectors = np.array(vectors_updated)
x_min, y_min = np.min(all_vectors, axis=0)
x_max, y_max = np.max(all_vectors, axis=0)
plt.xlim(-1, 2.5)
plt.ylim(0, 3.3)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Vectors for (E + (1/n * P))^n * [2, 2] with n from 0 to x, Each in Different Color')
plt.show()
