import numpy as np

from BrownRobins import inverse_matrix_method, brown_robinson_method

C = np.array([
    [1., 11., 11.],
    [7., 5., 8.],
    [16., 6., 2.]
])


inverse_matrix_method(C)
brown_robinson_method(C)
