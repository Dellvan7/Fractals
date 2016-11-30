import math
import matplotlib.pyplot as plt
import networkx as nx
import plot


class pointNode:
	def __init__(self, cargo=None, next=None): 
		self.point = cargo
		self.next = next


# Returns a list of points that can be used to plot a dragon curve.  
# Takes in an initial line segment, and the number of desired iterations
def dragon(segment, iteration):
	end = pointNode(segment[0])
	start = pointNode((segment[1]), end)
	while (iteration > 0):
		current = start
		left = True
		while current.next:
			step = current.next
			p2 = step.point
			p1 = current.point

			#define vector to be rotated
			x = p1[0]-p2[0]
			y = p1[1]-p2[1]
			if left:
				w = (x-y)/2
				z = (x+y)/2
				left = False
			else:
				w = (x+y)/2
				z = (y-x)/2
				left = True
			p3 = (p2[0]+w, p2[1]+z)
			new = pointNode(p3, step)
			current.next = new
			current = step
		iteration -= 1

	points = []
	current = start
	while current:
		points.append(current.point)
		current = current.next
	return points



if __name__ == '__main__':
	seg = [(0,0), (2,0)]
	points = dragon(seg, 2)
	print(points)