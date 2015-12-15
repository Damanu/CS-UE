#/usr/bin/python!

import numpy as np
import sys
import matplotlib.pyplot as plt
import networkx as nx


X_PLOTS=1
Y_PLOTS=3


def main(argv):
	mode=argv[1]
	path="net.net"
	G=nx.read_pajek(path)
	G=nx.Graph(G)
#-------------1--------------------------	
	Nnodes = G.number_of_nodes()
	Nedges = G.number_of_edges()

	
	degree=list(G.degree().values())
	meandeg=0
	for x in degree:
		meandeg+=x
	meandeg=meandeg/float(Nnodes)
	if mode=="1":
		print "number of nodes: ", Nnodes
		print "number of links: ",Nedges
		print "average degree: ", meandeg
		plt.title("degree distribution")
		plt.hist(degree)	
#------------------------------------------------
	
#------------------2---------------------------
	clustering=list(nx.clustering(G).values())
	ave_cluster=nx.average_clustering(G)
	if mode=="2":
		print "average clustering: ",ave_cluster
		print "-------------------------"
		print "-----ER-Network--------------"
		print "average degree: ", 2*Nedges/float(Nnodes)
		print "-------------------------"
		plt.title("clustering distribution")
		plt.bar(np.linspace(0,18,19),clustering)
	
	cluster_degree=[]
	i=0
	for x in degree:
		if x > 1:
			cluster_degree.append(x)
		else:
			clustering.pop(i)
		i+=1
	
	if mode == "3":	
		plt.title("degree over clustering coefficient")
		plt.plot(clustering,cluster_degree,'o')
#-----------------4---------------------
	neighbours=list(nx.k_nearest_neighbors(G).values())
	if mode=="4":
		print("average neares neighbour degree: ",sum(neighbours)/float(Nnodes))
#------------------5---------------------------
	r=nx.degree_pearson_correlation_coefficient(G)
	if mode=="5":
		print("r: ",r)
#-------------------6-------------------------
	eig_cent=list(nx.eigenvector_centrality(G).values())
	eig_top=sorted(range(len(eig_cent)), key=lambda i:eig_cent[i])[-7:]
	deg_top=sorted(range(len(degree)), key=lambda i:degree[i])[-7:]
	if mode=="6":
		print("degree top 7:",deg_top)
		print("eigenvector centrality top 7: ", eig_top)
#-----------------7--------------------
	pagerank_1=list(nx.pagerank(G,alpha=0.1).values())
	pagerank_2=list(nx.pagerank(G,alpha=0.85).values())
	pagerank_3=list(nx.pagerank(G,alpha=0.99).values())
	if mode=="7":
		plt.plot(range(Nnodes),pagerank_1,'r')
		plt.plot(range(Nnodes),pagerank_2,'g')
		plt.plot(range(Nnodes),pagerank_3,'y')
		
	
	if mode=="8":
		Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
		pos=nx.spring_layout(Gcc)
		nx.draw_networkx_nodes(Gcc,pos,node_size=20)
		nx.draw_networkx_edges(Gcc,pos,alpha=0.4)

	
	plt.show()

if __name__=="__main__":
	main(sys.argv)
