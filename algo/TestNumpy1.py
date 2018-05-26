'''
Created on 08-Dec-2016

@author: timmy
'''
#from statsmodels.nonparametric.tests.test_kernel_density import nparam

if __name__ == '__main__':
    pass

import numpy as np
from datetime import datetime

############ lecture 5 #############


# a = np.random.random(100)
# b = np.random.random(100)
# 
# T = 100000
# 
# def slow_dot_product(a,b):
#     result =0
#     for e,f in zip(a,b):
#         result +=e*f;
#     return result
# t0 = datetime.now()
# for t in xrange(T):
#     slow_dot_product(a, b)
#     
# dt1 = datetime.now() - t0
# 
# t0 = datetime.now()
# for t in xrange(T):
#     a.dot(b)
#     
# dt2 = datetime.now() - t0
# 
# print 1,"dt1 / dt2 : ", dt1.total_seconds() / dt2.total_seconds() 


################## lecture 6 


# 2d list

L = [[1, 2], [3, 4]]

print L, L[0], L[0][0]

M = np.array([[1, 2], [3, 4]])

print M, M[0], M[0][0]

print M.T

################### lecture 6 over... there are just two types of things 1d and 2d arrays..

#### lecture 7

A = np.array([1, 2, 3])
B = np.array(xrange(4, 10))
Z = np.zeros(10)
O = np.ones((10, 2))
O2 = np.ones((10,))
print A
print B
print Z
print O
print O2

R = np.random.random((10, 10))
RI = np.random.random_integers(-10, 10, size=(10, 10))
print R
print RI

# produce gaussion distr

# tuple is not accepted as argument, so we need to pass r/c saperately
Rnd = np.random.randn(10, 10)
print Rnd
# gaussian distr have mean close to 0 and var close to 1

# note in numpy '*' means element by element multiplication but 'dot' means matrix multiplication
print Rnd.mean(), Rnd.var()

A = np.array([[1, 2], [3, 4]])

Ainv = np.linalg.inv(A)
print Ainv

print Ainv.dot(A)

# to calculate determinant
print np.linalg.det(A)

# pass 2d array get one d array of diagnol elements
print np.diag(A)

# pass 1d array and get two d array with 1d in diagonal and rest 0
print np.diag([1, 2])

a = np.array([1, 2])
b = np.array([3, 4])

# to understand
print np.outer(a, b)

print np.inner(a, b)

print np.dot(a, b)

# sum of diagonal elements
print np.trace(A)
print np.diag(A).sum()

X = np.random.randn(100, 3)

print X[0:5, 0:3]

# please remember when we want to calc covariance of a matrix transpose it first
cov = np.cov(X.T)

print cov
print cov.shape

# to calculate (eigen values , eigen vectors), for symmetrical and hermitian matrix use eigh else use eig, we know cov is always symmetric
print np.linalg.eigh(cov)
print np.linalg.eig(cov)

########### lecture 10
# Ax = b

A = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])

# remember matrix multiplications are not associative so first position is inverse then b
x = np.linalg.inv(A).dot(b)

print x
# easy and more efficient meth, never use inverse approach
x = np.linalg.solve(A, b)

print x

# [
# [1,1]
# [1.5,4]
# ]           * [x1,
#                x2]      = [2200,
#                            5050]


A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])

print np.linalg.solve(A, b)
