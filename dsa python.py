import numpy as np
def leetcode(arr):

    rstart = 0
    rend = len(arr)
    cstart = 0
    cend = len(arr[0]) - 1
    rcount = 0
    while rstart != rend:
        while cstart <= cend:
            if arr[rstart][cstart] == 1:
                rcount += 1
            
    print(rcount)
    return


# Set the dimensions of the matrix
rows = 5
columns = 5

# Generate a random 2D matrix
random_matrix = np.random.rand(rows, columns)

print("Random 2D Matrix:")
print(random_matrix)
leetcode(random_matrix)
