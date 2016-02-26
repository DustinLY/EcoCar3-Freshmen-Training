# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import random
from scipy import linalg

m = numpy.zeros((3,3))
test = [0,1,2]

#uses nexted for loops to add random values to a matrix
def random_matrix(matrix_val):
    for i in test:
        for j in test:
           # print random_num
            #print i
            #print j
            matrix_val[i, j] = random.randrange(1,21)
    return matrix_val

#asks user input for row and column then prints it.
def index_loc():
    mat_row = raw_input("Which row do you choose?\n")
    mat_col = raw_input("Which column do you choose?\n")
    try:    
        if int(mat_row)>=1 and int(mat_row)<=3 and int(mat_col)>=1 and int(mat_col)<=3:        
            print m[int(mat_row) - 1, int(mat_col) - 1]
        else:
            print "Please enter 1, 2, or 3, to select your rows and columns.\n"
            index_loc()
    except:
        print "Please enter 1, 2, or 3, to select your rows and columns.\n"
        index_loc()

#trasnposes matrix m
def transpose_matrix():
    #print m
    print m .T

# prints inverse of matrix m
def inverse_matrix():
    print linalg.inv(m)

#makes new matrix, adds random values to it, then prints the dot product, multiply, subtract, and added  to matrix m.
def matrix_operators():
    new_mat=numpy.zeros((3,3))
    random_matrix(new_mat)
    print numpy.dot(new_mat, m)
    print new_mat*m
    print new_mat-m
    print new_mat+m



random_matrix(m)
index_loc()
transpose_matrix()
inverse_matrix()
matrix_operators()















