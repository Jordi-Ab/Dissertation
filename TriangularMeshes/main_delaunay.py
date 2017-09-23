import numpy as np
from Delaunay_mesh import Delaunay
import matplotlib.pyplot as pt

points = [(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1), (1,0), (0,0)]
mesh_points, triangles = Delaunay(points)

print(triangles)
print(mesh_points)

vertices = {}
for i,tri in enumerate(triangles):
    vertices[i] = mesh_points[tri]

pt.triplot(mesh_points[:, 0], mesh_points[:, 1], triangles)
pt.xlim(-2,2)
pt.ylim(-2,2)
pt.show()