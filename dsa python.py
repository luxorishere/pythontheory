import numpy as np
def sell_stock(array):
    maximum = 0
    for i in range(0 , len(array)):
        for j in range(i + 1, len(array)):
            if array[j] > array[i]:
                temp = np.abs(array[j] - array[i])
                maximum = max(maximum, temp)
    return maximum

            