from implementation import ECC
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sb



class Grapher:
	## this library returns counter and degree dictionary
	def makeCurve(self,a,b,p):
		curve = ECC(a,b,p)
		all_points = curve.findAllPoints()
		return self.getCounter(curve,all_points)

	def getCounter(self, curve, all_points):
		c = Counter()
		degree = dict()
		for point in all_points:
			seq = curve.findBinarySequence(point,10)
			for i in range(1,1000):
				t = curve.multiply(seq,i)
				if not t:
					degree[point] = i
					break
				else:
					c[t] += 1
		return c,degree


if __name__ == "__main__":
	g = Grapher()
	a,b,p = map(int,input().strip().split(" "))
	c,d = g.makeCurve(a,b,p)
	print(c)
	print()
	print(d)



