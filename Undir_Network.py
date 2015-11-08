#usr/bin/python!
import numpy as np
import sys

def ind_degree(matrix):
	d=[]
	N=np.size(matrix[0])
	i=0
	j=0
	while i<N:
		while j<N:
			di+=matrix[i,j]
			j+=1
		d.append(di)
		i+=1
		di=0
	return d

def ind_clustering(matrix):
	i=0
	j=0
	k=0
	cli=0.
	cli_=0.
	cl=[]
	N=np.size(matrix[0])
	while i<N:
		j=0
		while j<N:
			k=0
			while k<N:
				if j!=k and j!=i and k!=i:
					cli+=matrix[i,j]*matrix[i,k]*matrix[j,k]
					cli_+=matrix[i,j]*matrix[i,k]
				k+=1
			j+=1
		if cli!=0:
			cli=cli/cli_					
		cl.append(cli)
		cli=0
		cli_=0
		i+=1
	return cl
def overall_clustering(matrix):
	i=0
	j=0
	k=0
	cl=0.
	cl_=0.
	N=np.size(matrix[0])
	while i<N:
		j=0
		while j<N:
			k=0
			while k<N:
				if j!=k and j!=i and k!=i:
					cl+=matrix[i,j]*matrix[i,k]*matrix[j,k]
					cl_+=matrix[i,j]*matrix[i,k]
				k+=1
			j+=1
		i+=1

	if cl!=0:
		cl=cl/cl_
	else:
		cl=0					
	return cl


def main():
	m=np.matrix([[0.,1.,1.,1.] ,[1.,0.,1.,0.], [1.,1.,0.,0.],[ 1.,0.,0.,0.]])
	
	print ind_clustering(m)	
	print overall_clustering(m)	

if __name__=="__main__":
	main()

