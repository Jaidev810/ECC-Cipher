#check for array indices of the generate all function`
from collections import Counter

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __lt__(self,other):
		if self.x < other.x:
			return True
		return False
	def __repr__(self):
		return "(%d,%d)"%(self.x,self.y)
	def __str__(self):
		return "(%d,%d)"%(self.x,self.y)
	def __hash__(self):
		return int.__hash__(self.x+self.y)
	def __eq__(self,other):
		if not other:
			return False
		if type(other) == int:
			return False
		if other.x == self.x and other.y == self.y:
			return True
		return False


class ECC:
	def __init__(self,a,b,p):
		self.a = a
		self.p = p
		self.b = b

	def check(self,x,y):
		lhs = (y**2)
		rhs = ((x**3)+(self.a*x)+self.b)
		return True if (lhs-rhs)%self.p == 0 else False


	def findAllPoints(self):
		l = list()
		for i in range(0,self.p):
			for j in range(0,self.p):
				if self.check(i,j):
					l.append(Point(i,j))
		return l


	def inverse(self,a):
		# fermant's theorem
		return pow(a,self.p-2,self.p)

	def valid(self,point):
		if point == None:
			return True
		lhs = (point.y**2)
		rhs = (point.x**3 + (self.a*point.x) + self.b)
		return True if (lhs-rhs)%self.p == 0 else False

	def inversePoint(self,point):
		if point.x == 0 and point.y  == 0:
			return point
		return Point(point.x,(-point.y)%self.p)


	def Double(self,point):
		m = (3*point.x**2 + self.a)*self.inverse(point.y*2)
		x = (m*m - (point.x*2))%self.p
		y = (m*(point.x-x) - point.y)%self.p
		result = Point(x,y)
		assert self.valid(result)
		return result

	def findBinarySequence(self, first_point, num_bits):
		l = [None]*num_bits
		l[0] = first_point
		for i in range(1,num_bits):
			try:
				l[i] = self.Double(l[i-1])
			except AssertionError:
				return l
		return l

	def Add(self,point1,point2):
		if point1 == point2:
			return self.Double(point1)
		elif point1 == self.inversePoint(point2):
			return None
		elif point1 == None:
			return point2
		elif point2 == None:
			return point1
		m = (point2.y - point1.y)*self.inverse((point2.x-point1.x))
		nx = ((m*m) - point1.x - point2.x)%self.p
		ny = ((m*(point1.x - nx)) - point1.y)%self.p
		try:
			assert self.valid(Point(nx,ny))
		except AssertionError:
			print("Error in points ",point1,point2,nx,ny)
		return Point(nx,ny)

	def multiply(self,binary_sequence,multiplier):
		t = 1
		p = None
		for i in range(len(bin(multiplier)) - 2):
			if (t<<i) & multiplier:
				if binary_sequence[i] == 0:
					return None
				if p:
					p = self.Add(p,binary_sequence[i])
				else:
					p = binary_sequence[i]
		return p


