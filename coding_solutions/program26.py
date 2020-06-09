# Python program to rotate a matrix right by k times 
M = 3
N = 3
matrix = [[12, 23, 34], 
          [45, 56, 67],  
          [78, 89, 91]] 
def rotateMatrix(k) : 
    global M, N, matrix 
    temp = [0] * M 
    k = k % M    
    for i in range(0, N) :  
        for t in range(0, M - k) : 
            temp[t] = matrix[i][t] 
        for j in range(M - k, M) : 
            matrix[i][j - M + k] = matrix[i][j] 
        for j in range(k, M) : 
            matrix[i][j] = temp[j - k] 
def displayMatrix() : 
  global M, N, matrix 
  for i in range(0, N) : 
        for j in range(0, M) : 
            print ("{} " .  
                   format(matrix[i][j]), end = "") 
        print () 
k = 2
rotateMatrix(k) 
displayMatrix() 
