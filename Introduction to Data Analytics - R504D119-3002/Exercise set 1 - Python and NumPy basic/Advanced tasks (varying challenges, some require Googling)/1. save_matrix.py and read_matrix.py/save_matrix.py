import numpy as np

matrix_array = np.arange(1, 226).reshape(15,15)
np.savetxt('matrix.txt', matrix_array)