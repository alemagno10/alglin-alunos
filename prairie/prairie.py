import numpy as np

#print(np.linalg.norm([5,8,5,6]) + np.linalg.norm([8,8,5,8]))
#v = np.array([[0.73, 0.78, 0.21, 0.35, 0.04, 0.31], [0.06, 0.75, 0.58, 0.81, 0.02, 0.59], [0.69, 0.18, 0.19, 0.98, 0.23, 0.82], [0.37, 0.31, 0.65, 0.44, 0.07, 0.98], [0.02, 0.00, 0.85, 0.95, 0.72, 0.11], [0.48, 0.30, 0.40, 0.11, 0.64, 0.62], [0.30, 0.70, 0.58, 0.75, 0.74, 0.89], [0.64, 0.92, 0.41, 0.92, 0.17, 0.36], [0.14, 0.20, 0.53, 0.32, 0.48, 0.92], [0.45, 0.89, 0.27, 0.24, 0.19, 0.38], [0.91, 0.46, 0.39, 0.25, 0.17, 0.88]])
#print(np.linalg.norm(v))

A = np.array([[0.52, 0.90, 0.35, 0.57, 0.33, 0.85, 0.43, 0.81, 0.02, 0.19, 0.91], [0.18, 0.72, 0.29, 0.10, 0.22, 0.67, 0.43, 0.19, 0.35, 0.95, 0.69], [0.44, 0.49, 0.53, 0.13, 0.74, 0.71, 0.89, 0.68, 0.27, 0.09, 0.49], [0.27, 0.47, 0.41, 0.38, 0.50, 0.40, 0.95, 0.35, 0.54, 0.86, 0.46], [0.73, 0.44, 0.94, 0.53, 0.89, 0.87, 0.91, 0.57, 0.22, 0.38, 0.11], [0.81, 0.41, 0.84, 0.00, 0.98, 0.77, 0.56, 0.59, 0.47, 0.52, 0.30], [0.44, 0.72, 0.99, 0.82, 0.82, 0.42, 0.70, 0.99, 0.98, 0.32, 0.83], [0.57, 0.32, 0.32, 0.73, 0.26, 0.79, 0.54, 0.53, 0.59, 0.00, 0.50], [0.63, 0.60, 0.23, 0.42, 0.34, 0.06, 0.39, 0.15, 0.78, 0.80, 0.16], [0.11, 0.23, 0.93, 0.14, 0.96, 0.62, 0.64, 0.81, 0.12, 0.46, 0.77], [0.33, 0.82, 0.96, 0.88, 0.87, 0.48, 0.28, 0.82, 0.24, 0.77, 0.59]])
B = np.array([[0.14, 0.37, 0.44, 0.33, 0.54, 0.75, 0.47, 0.57, 0.67, 0.30, 0.82, 0.14], [0.00, 0.39, 0.80, 0.94, 0.06, 0.03, 0.10, 0.76, 0.07, 0.03, 0.52, 1.00], [0.53, 0.99, 0.67, 0.58, 0.41, 0.57, 0.02, 0.29, 0.58, 0.98, 0.67, 0.33], [0.42, 0.07, 0.60, 0.54, 0.47, 0.42, 0.34, 0.62, 0.38, 0.29, 0.66, 0.66], [0.93, 0.98, 0.94, 0.05, 0.19, 0.37, 0.93, 0.57, 0.08, 0.87, 0.90, 0.14], [0.80, 0.74, 0.41, 0.96, 0.23, 0.51, 0.52, 0.45, 0.15, 0.12, 0.05, 0.33], [0.04, 0.91, 0.29, 0.66, 0.91, 0.45, 0.79, 0.90, 0.72, 0.01, 0.12, 0.05], [0.68, 0.37, 0.46, 0.15, 0.01, 0.19, 0.77, 0.72, 0.65, 0.06, 0.35, 0.60], [0.19, 0.19, 0.15, 0.48, 0.90, 0.37, 0.24, 0.13, 0.99, 0.60, 0.93, 0.54], [0.89, 0.13, 0.76, 0.89, 0.52, 0.86, 0.04, 0.73, 0.51, 0.90, 0.83, 0.56], [0.39, 0.09, 0.09, 0.60, 0.61, 0.56, 0.12, 0.78, 0.28, 0.82, 0.39, 0.44]])
#print(A@B)
[[2.5804, 2.6836, 2.9106, 3.4909, 2.0757, 2.4393, 2.3691, 3.8272, 2.1925, 2.0625,
  2.7109, 2.8163],
 [2.289,  2.0666, 2.4397, 3.3524, 2.1253, 2.3495, 1.4402 ,3.0238, 1.9526, 2.3071,
  2.515,  2.3189],
 [2.4738, 3.3069, 2.7293, 2.8951, 2.2547, 2.3187, 2.7219, 3.3724, 2.3848, 2.1273,
  2.6197, 2.0145],
 [2.5231, 2.7515, 2.844, 3.363, 2.7895, 2.6899, 2.2235, 3.4944, 2.7095, 2.5958,
  2.5975, 2.1679],
 [1.7909, 1.7788, 2.429, 2.669, 2.3183, 2.2246, 1.5129, 2.6322, 2.3966, 2.1893,
  3.12,   2.1578],
 [3.2648, 3.4945, 3.0912, 2.9836, 2.2527, 2.6628, 2.625, 3.5314, 2.4085, 3.0739,
  2.9743, 2.1629],
 [3.6475, 3.4187, 4.1197, 3.8783, 2.5496, 3.1188, 2.626, 4.2431, 2.8414, 3.5069,
  4.141,  3.3704]]

#import numpy as np


A = np.array([[0.13, 0.42, 0.85, 0.89, 0.83], [0.79, 0.98, 0.57, 0.63, 0.70], [0.82, 0.53, 0.60, 0.63, 0.91], [0.93, 0.81, 0.06, 0.76, 0.82], [0.57, 0.92, 0.16, 0.72, 0.99]])
B = np.array([[0.50, 0.23, 0.89, 0.03, 0.76, 1.00], [0.67, 0.82, 0.85, 0.05, 0.34, 0.14], [0.91, 0.89, 0.41, 0.06, 0.97, 0.61], [0.07, 0.72, 0.77, 0.53, 0.70, 0.44], [0.40, 0.07, 0.40, 0.63, 0.16, 0.75]])
C = np.array([[0.47, 0.47, 0.54, 0.03, 0.20, 0.73], [0.98, 0.43, 0.26, 0.70, 0.79, 0.25], [0.84, 0.48, 0.94, 0.79, 0.32, 0.72], [0.58, 0.93, 0.26, 0.94, 0.67, 0.35], [0.18, 0.34, 0.98, 0.99, 0.50, 0.29], [0.52, 0.80, 0.16, 0.44, 0.80, 0.95]])
#print(A@B@C)

[[5.89308,  5.373056, 5.360796, 6.345998, 5.341928, 5.424867],
 [6.933626, 6.14024,  6.484848, 7.217964, 6.038492, 6.58017],
 [6.446372, 5.99135,  6.048876, 6.88497,  5.822924, 6.340719],
 [6.182131, 5.641634, 5.737632, 6.568651, 5.427057, 5.973624],
 [6.09329,  5.521874, 5.502994, 6.374701, 5.30132,  5.747557]]

# print(4.7/3.6)
# print(9.7/9.4)
# print(4/6.24)
# print(5/7.8)
# print(2.5/3.9)
# print(2.9/9.4)
# print(1.6/9.2)

import numpy as np

A = np.array([[0.20, 0.10, 0.10, 1.00, 0.20, 0.80, 0.50, 0.20, 1.00, 0.90, 0.10, 0.50], [0.50, 0.00, 0.30, 0.00, 0.10, 0.20, 0.60, 0.90, 0.70, 0.60, 0.80, 0.30], [0.50, 0.70, 0.50, 0.80, 0.10, 0.70, 0.10, 0.90, 0.20, 0.10, 0.00, 0.40], [0.90, 0.70, 0.30, 0.90, 0.30, 0.20, 0.20, 0.60, 0.40, 0.40, 0.20, 0.90], [0.30, 0.50, 0.60, 0.10, 0.70, 0.90, 0.30, 0.00, 1.00, 0.10, 0.80, 0.50], [0.70, 0.60, 0.30, 0.40, 0.50, 0.00, 0.60, 0.30, 0.00, 1.00, 0.10, 0.30], [0.70, 0.10, 0.30, 0.70, 0.80, 1.00, 0.90, 0.30, 0.60, 1.00, 0.60, 0.20], [0.90, 0.80, 0.60, 0.80, 0.20, 0.30, 0.90, 0.50, 1.00, 0.40, 0.80, 1.00], [1.80, 1.40, 0.60, 1.80, 0.60, 0.40, 0.40, 1.20, 0.80, 0.80, 0.40, 1.80], [0.20, 0.70, 1.00, 0.50, 0.90, 1.00, 0.10, 0.60, 0.90, 0.40, 1.00, 0.50], [0.20, 0.80, 0.10, 1.00, 0.40, 0.60, 0.60, 0.20, 0.60, 0.10, 0.20, 0.40], [0.30, 0.20, 0.90, 0.20, 0.30, 0.90, 0.90, 0.70, 0.70, 0.90, 0.30, 0.30]])
#print(np.linalg.det(A))

A = np.array([[5,6], [8,7]])
B = np.array([6,5])
print(np.linalg.solve(A,B))