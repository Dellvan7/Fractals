'''
fractal-art.py

generate some fractal art

'''
import math
import matplotlib.pyplot as plt
import networkx as nx
import plot

'''
	DEFINITIONS:
		Point = [xcoordinate, ycoordinate]
		LineSegment = [Point1, Point2]
'''

'''
	fract1 - 
		take a line segment, remove the middle third
		replace with two line segments equal in length to middle third
		these two segments meet at exactly 1 point


		---------------------------
		             ^
		            / \
		           /   \
		          /     \
		---------/       \---------

	Algorithm:
		take line segment, l = [p0, p1]
		compute l1, l2, l3
			l1 = [p0, p1/3]
			l2 = [p1/3, p2/3]
			l3 = [p2/3, p1]
		compute p1/2
			where p1/2 = [midpoint(p0,p1), y]
			and where y = sqrt((x/3)^2 - (x/6)^2), where x = dist(p0, p1)
				^^ consider right traingle of height y, created by midpoint(l), p1/2, and either p1/3, or p2/3
					using this triangle, solve for y coordinate of p1/2
		return linesegments = [
			[p0, p1/3],
			[p1/3, p1/2],
			[p1/2, p2/3],
			[p2/3, p1]
		]
'''
def fract1(linesegments, iterations):
	def distance(p0, p1):
		# print("DISTANCE FUCNTION:", p0, p1)
		return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)	

	def midpoint(p1, p2):
		distancep1p2 = distance(p1, p2)
		return ((p1[0] + p2[0])/2, math.sqrt( (distancep1p2/3)**2 - (distancep1p2/6)**2 ))

	def third(p0, p1):
		a = p0[0]
		b = p0[1]
		c = p1[0]
		d = p1[1]
		#print(a,b)
		#print(c,d)
		v1x = c-a
		v1y = d-b
		#print("vector1:", v1x, v1y)
		v2x = v1x/2 - (math.sqrt(3)*v1y/2)
		v2y = (math.sqrt(3)*v1x/2) + v1y/2
		#print("vector2:", v2x, v2y)
		third = ((a+v2x, b+v2y))
		return(third)

	def fract1equation(linesegment):
		p0, p1 = linesegment[0], linesegment[1]

		#Compute points that make up middle line segment
		p23 = ( (p0[0] + 2 * p1[0]) / 3, (p0[1] + 2 * p1[1]) /3)
		p13 = ( (2 * p0[0] + p1[0]) / 3, (2 * p0[1]+ p1[1]) / 3)

		#compute the third point of the triangle
		p12 = third(p13, p23)

		#print("POINTS:",p0, p13, p12, p23, p1)
		l1 = (p0, p13)
		l2 = (p13, p12)
		l3 = (p12, p23)
		l4 = (p23, p1)
		return [l1, l2, l3, l4]

	segments = linesegments
	counter = 0
	while segments and counter < iterations:
		print("ITERATION: ", counter)
		frontier = []
		for segment in segments:
			for lineseg in fract1equation(segment):
				frontier.append(lineseg)
		segments = frontier
		counter += 1

	return segments


if __name__ == "__main__":
	iterations = 5
	orig_segments = [( (10, 0), (0, 0) ), ( (0, 0), (0, 10) ), ( (0, 10), (10, 10) ), ((10, 10), (10, 0))]
	G = plot.segments_to_graph(orig_segments)
	G, pos = plot.list_graph_to_networkx(G)
	plot.save_graph(G, pos, "orig_fract1_" + str(iterations) + "_", 100000)

	segments = fract1(orig_segments, iterations)
	# for i in range(2):
	# 	frontier = set()
	# 	for seg in segments:
	# 		print(seg)
	# 		frontier.update(fract1(seg))
	# 	segments = frontier

	# print("SEGEMNTS:", segments)

	G = plot.segments_to_graph(segments)

	# print("GRAPH:", G)

	G, pos = plot.list_graph_to_networkx(G)


	# print(G.nodes())


	plot.save_graph(G, pos, "fract1_" + str(iterations) + "_", 100000)















