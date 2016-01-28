from union_find import UF
import distance
import heapq


def EdgeComp(e1,e2):
	u,v=e1
	x,y=e2
	leveluv = distance.hamming(profiles[u],profiles[v])  
	levelxy = distance.hamming(profiles[x],profiles[y])

	if leveluv != levelxy:
		return leveluv - levelxy

	for k in range (maxlen):				
	 	maxuv = max(lvs[u][k], lvs[v][k])	
	 	maxxy = max(lvs[x][k], lvs[y][k])

		if maxuv != maxxy:
			return maxxy - maxuv

		minuv = min(lvs[u][k], lvs[v][k])
		minxy = min(lvs[x][k], lvs[y][k])

	 	if minuv != minxy:
			return minxy - minuv 

		maxuv = max(u,v) 
		maxxy = max(x,y)

		if maxuv != maxxy:
			return maxxy - maxuv

		minuv = min(u,v)
		minxy = min(x,y)

		if minuv != minxy:
			return minxy - minuv


def run_kruskal(pm, pl, n, lvs1):

	global profiles
	global maxlen
	global lvs

	maxlen = pl #profile length
	lvs = lvs1
	
	profiles = pm
	
	edges=[] 
	n = n

	for i in range(n):
		for j in range(i +1, n):
			edges.append([i,j])
	edges.sort(EdgeComp) 

	# var uf = new UnionFind(n)
	uf = UF(n)

	tree = []
	i=0
	while i<len(edges) and len(tree)<n-1:
	 	
		if uf.find(edges[i][0]) != uf.find(edges[i][1]): 
			tree.append(edges[i])		
			uf.union(edges[i][0], edges[i][1])
		
		i+=1

	return tree


def run_prim(pm, pl, n, lvs1):
	
	global profiles
	global maxlen
	global lvs

	maxlen = pl #profile length
	lvs = lvs1 #lvs calculated previously (Comparator.goeBURST)
	profiles = pm
	n = n

	pi = {}
	color = [ 0 for i in range(n)]

	tree = []
	pqueue = []

	heapq.heappush(pqueue, 0)

	while len(pqueue) > 0:
		u = heapq.heappop(pqueue)
		color[u] = 2
		if u != 0:
			tree.append([pi[u][0],pi[u][1]])

		for v in range(len(profiles)):
			if color[v] == 0:
				color[v] = 1
				pi[v] = [u,v]
				heapq.heappush(pqueue, v)
			elif color[v] == 1 and EdgeComp([u,v], pi[v]) < 0:
				pi[v] = [u,v]
				#heapq.heapify(pqueue)

	#print tree
	return tree







