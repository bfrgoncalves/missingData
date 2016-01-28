import numpy as np
import random

class Generator:

	def __init__(self, n, pl, dist):
		self.pl = pl
		self.dist = dist
		self.n = n
		self.pm = []
		self.mpm = []

	def set_distribution(self, dist):
		self.dist = dist

	def set_profileLength(self, pl):
		self.pl = pl

	def get_distribution(self):
		return self.dist
	
	def get_profileLength(self):
		return self.pl

	def get_profileMatrix(self):
		return self.pm

	def get_missingMatrix(self):
		return self.mpm

	def distributions(self, argument):

		randMean = np.random.randint(1, 5, 1)

		switcher = {
			"normal": np.random.normal(randMean, randMean*0.2, self.n),
			"poisson": np.random.poisson(randMean, self.n),
			"gamma": np.random.gamma(randMean, randMean, self.n),
		}

		return switcher.get(argument, "nothing")


	def generate_profiles(self):
		pl = self.pl
		n = self.n
		dist = self.dist
		pm = self.pm

		pm = []
		pmt = [[0 for x in range(pl)] for x in range(n)] #matrix initialized at 0 pl*n

		for i in range(0, n):
			pm.append([abs(int(i) + 1) for i in self.distributions(dist)])

		for qIndex, q in enumerate(pm):
			for zIndex in range(0, n):
				pmt[zIndex][qIndex] = pm[qIndex][zIndex]

		self.pm = pmt
		
		return pm

	def set_missings(self, mr):
		pm = self.pm
		random.seed(1)

		for Iindex, i in enumerate(pm):
			for Jindex, j in enumerate(i):
				rn = random.random()
				if rn <= mr:
					pm[Iindex][Jindex] = '-'

		self.mpm = pm

		return self.mpm











