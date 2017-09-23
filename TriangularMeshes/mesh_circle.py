import numpy as np
import meshtools as mt
import numpy.linalg as la
import matplotlib.pyplot as pt


length=3 # Distance between points in the circumference

center = [0,0]
radius = 20

# simple mesh circle
p,v=mt.CircleSegments(center,radius,edge_length=length)
mesh_pts, elems = mt.DoTriMesh(p,v,edge_length=length)

pt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)
pt.axis('scaled')
pt.show()

