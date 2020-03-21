import numpy
from numpy import array
from scipy import linalg
from scipy.linalg import svd
A = array([[1, 2], [2,1],[3, 4], [4, 3]])
print(A)
U, sig, VT = svd(A, full_matrices=False)
print(U)
print(sig)
print(VT)
print("Eigenvalues and Eigenvectors below")
evals, evecs = linalg.eigh(numpy.dot(numpy.transpose(A),A))
dict={}
for i in range(0,evals.size):
    dict.update({evals[i]:evecs[:,i]})
for key in sorted(dict.items(),reverse=True):
    print(key)

