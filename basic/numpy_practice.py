import numpy as np

def matrix_tutorial(A):

    # 2
    # 전치 행렬 Aij->Aji
    B = A.transpose()
    try:
        #3 - 1
        #역행렬
        C = np.linalg.inv(B)
    except:
        #3 - 2
        return "not invertible"
    # 4
    #0보다 큰 갯수 (T:1,F:0)
    return np.sum(C>0)

def get_matrix():
    # 1
    mat = [] 

    first_line = input().strip() # receice first line
    first_line_splitted = first_line.split(" ") # split line by space " "
    n = int(first_line_splitted[0]) 
    m = int(first_line_splitted[1]) 

    for i in range(n):
        line = input().strip() # receive each line
        row = line.split(" ")  # split
        for j in range(m):
            row[j] = int(row[j]) # convert to integer
        mat.append(row)

    return np.array(mat)

if __name__ == "__main__":
    A = get_matrix()
    print(matrix_tutorial(A))
