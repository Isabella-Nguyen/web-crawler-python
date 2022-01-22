#TUTORIAL 4 PROBLEM 1

import math

def mult_scalar(matrix, scale):
    newMatrix=[]
    for row in range (len(matrix)):
        newMatrix.append([]) #Add a new list in the matrix for each row
        for column in matrix[row]:
            newMatrix[row].append(column*scale) #add the number multiplied by the scalar into the row in the matrix
    return newMatrix

def mult_matrix(a, b):
    matrix=[]
    multNum=0
    if len(a[0])!= len(b): #Check if the dimensions of the matrices are compatible
        return None
    for row in range(len(a)): #Find each row in 'a'
        matrix.append([]) #Add a new list in the matrix for each row
        for colNumB in range(len(b[0])): #Get the index for each column in 'b' (assuming all the rows have the same length)
            for column in range(len(a[row])): #Get the index for each number in the row for 'a'
                numB=b[column][colNumB]
                numA=a[row][column]
                multNum+=(numA*numB)
            matrix[row].append(multNum) #add the number to the row in the matrix
            multNum=0
    return matrix
	
def euclidean_dist(a,b):
    dist=0
    if len(a[0])!=len(b[0]): #Make sure both inputs have the same amount of numbers
        return -1
    for point in range(len(a)):
        for num in range(len(a[point])):
            dist+=(a[point][num]-b[point][num])**2
    eucl_dist=math.sqrt(float(dist)) #square root the whole distance and make sure it's not an integer
    return eucl_dist