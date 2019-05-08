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
		pairs = [[[row[i] for row in m1], m2[j]] for i in range(l) for j in range(n)]
		return pairs

	def multiply(arglist):
		column, row = arglist
		elem = 0
		for index in range(len(column)):
			elem += column[index]*row[index]
		return elem

	def mem_checker(arglist):
		ps = psutil.Process()
		before = ps.memory_info().rss
		print(before)
		multiprocess.multiply(arglist)
		mem = ps.memory_info().rss - before
		return mem

if __name__ == "__main__":
	l = 1000
	m = 300
	n = 400
	pairs = multiprocess.create_matrix(l,m,n,-100000000000000000,1000000000000000000000000000000000000000)
	#for i in range(5):
	#	print(pairs[i])
	pool = Pool(processes = 1)
	mem_res = pool.map(multiprocess.mem_checker, [pairs[i] for i in range(5)])
	print(mem_res)



