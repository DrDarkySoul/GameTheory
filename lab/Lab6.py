import numpy as np

from BrownRobins import inverse_matrix_method, brown_robinson_method

C = np.array([
    [1., 11., 11.],
    [7., 5., 8.],
    [16., 6., 2.]
])

# C = np.array([
#     [2., 1., 3.],
#     [3., 0., 1.],
#     [1., 2., 1.]
# ])


inverse_matrix_method(C)
brown_robinson_method(C)
