
#the tag/attribute of root node of the file
import xml.etree.ElementTree as ET
tree = ET.parse('blast_sample.xml')
root = tree.getroot()


print(root.tag)

# matrix was used for alignment scoring
for each in root.findall('.//Parameters'):
         rating = each.find('.//Parameters_matrix')
         print(rating.text)
         
#number of similar sequences (Hits) as entry sequence in database
for each in root.findall('.//Hit'):
    similar_sequences = each.find('.//Hit_num')

print(similar_sequences.text)

#number of similar sequences (Hits) with less than 0.01 
for each in root.findall('.//Hsp'):
    value = each.find('.//Hsp_evalue')
    if value.text < '0.01':
       print(value.text)
       
#calculate the eigen values and eigen vectors of the matrix. 
import numpy as np
Matrix = np.matrix('2 4 6; 8 10 12; 14 16 18')
print(Matrix)

tMatrix = Matrix.transpose()
print(tMatrix)
from numpy import linalg as L
a, b = np.linalg.eig(Matrix)
print("Eigenvalues of Matrix is : ", a)
print("Eigenvector of Matrix is : ", b)
from numpy import linalg as L
c, d = np.linalg.eig(tMatrix)
print("Eigenvalues of Matrix is : ", c)
print("Eigenvector of Matrix is : ", d)
print("Eigenvector of Matrix is : ", d)

#calculate the singular value decomposition (SVD)
a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
myU, mys, myV = np.linalg.svd(a, full_matrices=True)
myU.shape, myV.shape, mys.shape
((9, 9), (6, 6), (6,))
theS = np.zeros((9, 6), dtype=complex)
theS[:6, :6] = np.diag(mys)
print(np.diag(mys))
