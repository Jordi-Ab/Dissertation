import meshpy.triangle as triangle
import numpy as np

def Delaunay(points):
	"""
	points must be in counter-clockwise ordering.
	"""
	
	def round_trip_connect(start, end):
	    return [(i, i+1) for i in range(start, end)] + [(end, start)]

	info = triangle.MeshInfo()
	info.set_points(points)
	vertices = round_trip_connect(0, len(points)-2)
	info.set_facets(vertices)

	mesh = triangle.build(info)

	mesh_points = np.array(mesh.points)
	mesh_tris = np.array(mesh.elements)

	return mesh_points, mesh_tris
