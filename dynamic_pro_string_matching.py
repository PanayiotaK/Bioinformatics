#!/usr/bin/python
import time
import sys
import numpy as np


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

seq1 = 'AC'
seq2 = 'AG'
score_matrix = np.zeros((len(seq2)+1,len(seq1)+1), dtype = int )
backtrack_matrix = np.chararray((len(seq2)+1,len(seq1)+1), unicode = True )
backtrack_matrix [:] = 'D'


def populate (seq1, seq2):
    
    global backtrack_matrix
    global score_matrix    
   
    for i in range (len(seq2)+1):
        for j in range (len(seq1)+1):    
            if i == 0 and j == 0:
                score_matrix[i][j] = 0
                backtrack_matrix[i][j] = 'E'
                
            elif i == 0 and j != 0:                
                score_matrix[i][j] = -2*j
                
                backtrack_matrix[i][j] = 'L'
                
            elif i != 0 and j == 0:
                score_matrix [i][j] = -2*i
                backtrack_matrix[i][j] = 'U'
                
            elif i!= 0 and j != 0 :
                if seq1[j-1] == seq2[i-1]:
                    if seq2[i-1] == 'A':
                        c =2
                    elif seq2[i-1] == 'C':
                        c = 2
                    elif seq2[i-1] == 'G':
                        c = 2
                    elif seq2[i-1] == 'T':
                        c = 2
                else:
                    c = -1
                    
                score1 = c + score_matrix[i -1 ][j -1]
                #print("gia i: ",i , "geia j: ",j, " ","score 1: ",score1)
                score2 = score_matrix[i -1][j] -2
                score3 = score_matrix[i][j-1] -2
                #print("score2: ",score2, " ","score 3: ",score3)
                max_val = score1                
               
                if  score2 > max_val:
                    max_val = score2
                    backtrack_matrix[i][j] = 'U'
                    
                if score3 > max_val :
                    #print("if tou L" , "i: ",i ,"j: ", j)
                    max_val = score3
                    backtrack_matrix[i][j] = 'L'
                    #print( backtrack_matrix[i][j])
                    #print("backtrack matrix:  ",backtrack_matrix)
                    
                score_matrix[i][j] = max_val
   
    print("score matrix:  ")
    print(score_matrix)
    print("backtrack matrix:")
    print(backtrack_matrix)
                
def Backtrack( seq1,seq2 ):
    i = len(seq2)
    j = len(seq1)
    global backtrack_matrix
    global score_matrix
    position = backtrack_matrix[i][j]
    align2 = ""
    align1 = ""
    while(position != 'E'):
        #print("seq1: " ,seq1)
        #print("seq2: " , seq2)
        #print("i: ",i,"j: ",j,"position: ",position)
        if position == 'L':
            j =j-1
            position = backtrack_matrix[i][j]
            align1 += seq1[len(seq1)-1]
            align2 += '-'
            seq1 = seq1[:-1]
            
        elif position == 'U':
            i = i-1
            position = backtrack_matrix[i][j]
            align2 += seq2[len(seq2)-1]
            align1 += '-'
            seq2 = seq2[:-1]
            
        elif position == 'D':
            i = i-1
            j = j-1
            position = backtrack_matrix[i][j]
            #print(len(seq2)-1)
            align2 += seq2[len(seq2)-1]
            align1 += seq1[len(seq1)-1]
            seq1 = seq1[:-1]
            seq2 = seq2[:-1]
            
    align1 = align1[::-1]
    align2 = align2[::-1]
    print("align1: ", align1)
    print("align2: ", align2)
            
   

                 

populate (seq1, seq2)   
Backtrack(seq1,seq2 )


# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them

# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 



#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

