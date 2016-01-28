#!/usr/bin/env python
import os
import sys
import distance
from utils import run_kruskal, run_prim

class Comparator:

	def __init__(self, pm):
		self.pm = pm
		self.pl = len(pm[0])
		self.n = len(pm)

	def get_distances(self):
		dm = [[0 for x in range(self.pl)] for x in range(self.n)]
		pm = self.pm
		
		for i in range(self.n):
			for j in range(i+1, self.n):
				dm[i][j] = distance.hamming(pm[i], pm[j])

		self.dm = dm

		return self.dm

	def CalcLVs(self):
		maxlen= len(self.pm[0])
		nprof=len(self.pm)

		lvs=[[0 for x in range(maxlen)] for x in range(nprof)]

		for i in range(nprof):
			for j in range(i+1,nprof):
				diff=distance.hamming(self.pm[i],self.pm[j])
				lvs[i][diff-1]+=1
				lvs[j][diff-1]+=1

		self.lvs = lvs

		return self.lvs


	def goeBURST(self, algorithm):

		return {
			'prim': lambda x, y, w, z: run_prim(x, y, w, z),
			'kruskal': lambda x, y, w, z: run_kruskal(x, y, w, z)
		}.get(algorithm, 'Invalid')(self.pm, self.pl, self.n, self.CalcLVs())

		
















