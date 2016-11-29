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
def fract1(linesegment):
	def distance(p0, p1):
		# print("DISTANCE FUCNTION:", p0, p1)
		return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)	

	def midpoint(p1, p2):
		distancep1p2 = distance(p1, p2)
		return ((p1[0] + p2[0])/2, math.sqrt( (distancep1p2/3)**2 - (distancep1p2/6)**2 ))

	def third(p0, p1):
	    return ()

	def fract1equation(linesegment):
		p0, p1 = linesegment[0], linesegment[1]

		p12 = midpoint(p0, p1)
		p13 = third(p0, p1, 1)
		p23 = third(p0, p1, 2)

		# print("POINTS:",p0, p13, p12, p23, p1)


		l1 = (p0, p13)
		l2 = (p13, p12)
		l3 = (p12, p23)
		l4 = (p23, p1)

		return [l1, l2, l3, l4]



	return fract1equation(linesegment)


def segments_to_graph(segemnts):
	G = {}
	for segment in segments:
		p0, p1 = segment

		if p0 not in G:
			G[p0] = [p1]
		else:
			G[p0].append(p1)
		if p1 not in G:
			G[p1] = [p0]
		else:
			G[p1].append(p0)
	return G

if __name__ == "__main__":

	segments = fract1(((0, 0), (5, 10)))

	# for i in range(2):
	# 	frontier = set()
	# 	for seg in segments:
	# 		print(seg)
	# 		frontier.update(fract1(seg))
	# 	segments = frontier

	# print("SEGEMNTS:", segments)

	G = segments_to_graph(segments)

	# print("GRAPH:", G)

	G, pos = plot.list_graph_to_networkx(G)


	# print(G.nodes())


	plot.save_graph(G, pos, "fract1", 1000)














