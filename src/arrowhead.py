import math
import matplotlib.pyplot as plt
import networkx as nx
import plot
from dragon import pointNode




def arrowhead(segment, iterations):
	filenames = []

	end = pointNode(segment[1])
	start = pointNode((segment[0]), end)

	while (iterations>0):
		
		current = start
		if iterations%2 == 1:
			left = True
		else:
			left = False
		while current.next:
			step = current.next
			p2 = step.point
			p1 = current.point
			#print("making new points from: ")
			#print(p1)
			#print(p2)
			#define vector to be rotated
			x = (p2[0]-p1[0])/2
			y = (p2[1]-p1[1])/2
			#print("rotation vector:", x, y)

			#Rotate 60 degrees
			if left:
				v1x = (x - math.sqrt(3)*y)/2
				v1y = (math.sqrt(3)*x + y)/2
				left = False
			#Rotate -60
			else: 
				v1x = (x + math.sqrt(3)*y)/2
				v1y = (-1*math.sqrt(3)*x + y)/2
				left = True

			
			n1 = (p1[0] + v1x, p1[1] + v1y)
			n2 = (n1[0] + x, n1[1] +y)
			#print ("new points: ", n1, n2)
			new2 = pointNode(n2, step)
			new1 = pointNode(n1, new2)
			current.next = new1
			current = step
			#print("next point:", current.point, current.next)
		
		iterations -=1

		points = []
		current = start
		while current:
			points.append(current.point)
			current = current.next
		segments  = []
		for i in range(len(points)-1):
			seg = [points[i], points[i+1]]
			segments.append(seg)
		G = plot.segments_to_graph(segments)
		G, pos = plot.list_graph_to_networkx(G)
		filename = "arrrowhead" + str(iterations) + ".png"
		filenames.append(filename)
		plot.save_graph(G, pos, filename, 1000)

	plot.images_to_gif("arrrowhead", filenames)

	return segments



if __name__ == '__main__':

	iterations = 10
	seg = [(0,0), (16,0)]
	segments = arrowhead(seg, iterations)
