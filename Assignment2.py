#This matrix will find inverse of an nxn matrix using elementary transformations

import numpy as np
from numpy import c_


def diagonal_row(A, R):
    for i in range(0,R):
        temp = A[i][i]
        #print('A[{}][{}] is {}'.format(i,i, temp))
        for j in range(len(A[0])):
            A[i][j] = A[i][j]/temp
    print('Diagonal function')
    return A

def conv_echelon(A, R):
    for i in range(0,R):
        #print('A[{}][{}] is {}'.format(i,i, temp))
        for j in range(0,R):
            if j != i:
                temp = A[j][i] / A[i][i] 
                for k in range(len(A[0])):
                    A[j][k] -= A[i][k] * temp 
    return A

def main():
    
    R = int(input("Enter the number of rows:")) 
    C = int(input("Enter the number of columns:")) 
      
      
    print("Enter the entries of {} x {} matrix in a single line (separated by space): ".format(R,C)) 
      
    # User input of entries in a  
    # single line separated by space 
    entries = list(map(int, input().split())) 
      
    # For printing the matrix 
    matrix = np.array(entries).reshape(R, C) 
    print(matrix) 

    I = np.identity(R, dtype = float)
    print ( 'identity: ', I)

    A = c_[matrix, I]
    print ( 'Augmented: ', A)

    A_R = conv_echelon(A, R)
    print ( 'Echelon form: \n', A_R)
    
    A_D = diagonal_row(A, R)
    print ( 'Diagonal: \n', A_D)

    if R != C:
        print('Can\'t find inverse of the matrix as it is not a square matrix')
        exit(0)

    print('Inverse of the given matrix is:\n')
    for i in range(0, R):
        for j in range(R,2*R):
            print("{0:0.2f}  ".format(A_D[i][j]), end='')
        print(' ')
      
if __name__=='__main__':
    main() 


    
        
           
