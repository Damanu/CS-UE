#/usr/bin/python!

import numpy as np
import sys
import matplotlib.pyplot as plt
import networkx as nx


X_PLOTS=1
Y_PLOTS=3


def main():
	path="net.net"
	G=nx.read_pajek(path)
	G=nx.Graph(G)
#-------------1--------------------------	
	Nnodes = G.number_of_nodes()
	Nedges = G.number_of_edges()

	print "number of nodes: ", Nnodes
	print "number of links: ",Nedges
	
	degree=list(G.degree().values())
	print len(degree)
	meandeg=0
	for x in degree:
		meandeg+=x
	meandeg=meandeg/float(Nnodes)
	print "average degree: ", meandeg
	plt.subplot(Y_PLOTS,X_PLOTS,1)
	plt.hist(degree)	
#------------------------------------------------
	
#------------------2---------------------------
	clustering=list(nx.clustering(G).values())
	plt.subplot(Y_PLOTS,X_PLOTS,2)
	plt.bar(np.linspace(0,18,19),clustering)
	ave_cluster=nx.average_clustering(G)
	print "average clustering: ",ave_cluster
	print "-------------------------"
	print "-----ER-Network--------------"
	print "average degree: ", 2*Nedges/float(Nnodes)
	
	print "-------------------------"
	
	cluster_degree=[]
	i=0
	for x in degree:
		if x > 1:
			cluster_degree.append(x)
		else:
			clustering.pop(i)
		i+=1
	print len(cluster_degree)
	plt.subplot(Y_PLOTS,X_PLOTS,3)
	plt.plot(clustering,cluster_degree,'o')
#----------------------------------------------

#	Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
#	pos=nx.spring_layout(Gcc)
#	nx.draw_networkx_nodes(Gcc,pos,node_size=20)
#	nx.draw_networkx_edges(Gcc,pos,alpha=0.4)

	
	plt.show()

if __name__=="__main__":
	main()
