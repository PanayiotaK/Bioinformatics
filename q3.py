import numpy as np
"""
file = open("matrix.txt",'r')
data = file.read()
### remove ABCD from the top of the matrix


"""

c = np.zeros((2,2),dtype = int)
"""
a = np.array([[1, 2],
              [3, 4],
              [5, 6]]TTTTTTT)
"""
c = np.insert(c,1,[[11,13]], axis = 1)
#a3 = np.insert(a3, 1,[[2,3,4]],axis  = 0 )
#a2 = np.insert(a,3,[11,12]) 
print(c)
print(c[0][1])
c = np.delete(c,0,axis = 0)
print (c)
"""
b = np.array([[1,2], [3,4]])
s = slice (2,5)
my_tuple = [1, 2, 3, 4, 5, 6]
print(my_tuple[s])
#print(slice(1,3,1))
"""


letters = ['A','B','C','D','E','F']
matrix = np.array([[0, 15, 24, 29, 25, 37],
[15, 0, 32, 31, 23, 43],
[24, 32, 0, 30, 43, 49],
[29, 31, 30, 0, 45, 57],
[25, 23, 43, 45, 0, 55],
[37, 43, 49, 57, 55, 0]])

while matrix.shape != (2,2) :
    print(matrix)
    minElement = matrix[0][1]
    min_i = 0
    min_j = 1
    for i in range (np.size(matrix,0)):        
        for j in range (np.size(matrix, 1)):            
            if matrix[i][j] < minElement and i != j:               
                minElement = matrix[i][j]
                min_i = i
                min_j = j
                
    new_Array = []
    for k in range(np.size(matrix,1)):
        if k == min_j:
            continue
        if k == min_i :
            new_Array.append(0)
            continue
        new_Array.append((matrix[k][min_i] + matrix[k][min_j])/2 )
        
   
    new_node = letters[min_i] + letters[min_j]
    
    if(min_i >  min_j):
        matrix = np.delete(matrix, min_j, axis = 0)
        matrix = np.delete(matrix, min_i , axis = 1)
        matrix = np.insert(matrix ,min_i , new_Array, axis = 0 )
        matrix = np.insert(matrix , min_i , new_Array, axis = 1 )
        letters[min_i] = new_node
        letters.remove(letters[min_j])
    else:
        
        matrix = np.delete(matrix, min_i,axis = 0)
        matrix = np.delete(matrix,min_i , axis = 1)    
        matrix = np.insert(matrix ,min_j , new_Array, axis = 0 )
        matrix = np.insert(matrix , min_j , new_Array, axis = 1 ) ### DE TA INSERT JAI TA DELETE 
        letters[min_j] = new_node
        letters.remove(letters[min_i])
        
    
    
    

    



                
