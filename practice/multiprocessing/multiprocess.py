import os
import time
from multiprocessing import Pool
from multiprocessing import Process
import psutil
import random

class multiprocess:
	m1 = []
	m2 = []
	pairs = []
			
	def create_matrix(l,m,n,minValue,maxValue):
		# 1 матрица l*m 2 матрица m*n
		m1 = [[random.randint(minValue,maxValue) for elem in range(l)] for row in range(m)]
		m2 = [[random.randint(minValue,maxValue) for elem in range(m)] for row in range(n)]
		pairs = [[i,j,m, m1, m2] for i in range(l) for j in range(n)]

	def multiply(arglist):
		p = psutil.Process(os.getpid())
		before = p.memory_info().rss
		column_index, row_index, m, m1, m2 = arglist
		elem = 0
		column = [row[column_index] for row in m1]
		row = m2[row_index]
		for index in range(m):
			elem += column[index]*row[index]
		mem = p.memory_info().rss - before
		return elem, mem

	def mem_checker(arglist):
		p = psutil.Process(os.getpid())
		before = p.memory_info().rss


	'''def get_pair():
		pair = pairs[0]
		del pairs[0]
		return pair'''


if __name__ == "__main__":
	l = 1000
	m = 3000
	n = 400
	mp = multiprocess()
	mp.create_matrix(l,m,n,-100000000,100000000000000000000000)
	#print((*mp.pairs[0]))
	maxMem = 0;
	for i in range(5):
		p = Process(target=mp.multiply, args=([mp.pairs[i]]))
		print(p.start())
		print(p.join())
	#pool = Pool(processes = 3)
	#mres = (pool.map(mp.multiply, mp.pairs))
	#print(mp.m1)
	#print(mp.m2)
	#print([[mres[i*n+j] for i in range(l)] for j in range(n)])



