# Python program to print boundary element  
# of matrix. 
  
MAX = 100
   
def printBoundary(a, m, n): 
    sum = 0
    for i in range(m): 
        for j in range(n): 
            if (i == 0): 
                sum += a[i][j] 
            elif (i == m-1): 
                sum += a[i][j] 
            elif (j == 0): 
                sum += a[i][j] 
            elif (j == n-1): 
                sum += a[i][j] 
    return sum
      
# Driver code 
a = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], 
    [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ] 
sum = printBoundary(a, 4, 4) 
print ("Sum of boundary elements is", sum)
