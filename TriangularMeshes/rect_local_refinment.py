import numpy as np
import meshtools as mt
import numpy.linalg as la
import matplotlib.pyplot as pt

# rectangle with a local refinement 
length = 0.3

p1,v1=mt.RectangleSegments([0,0],[1,1],num_points=20)
p2,v2=mt.RectangleSegments([0.05,0.05],[0.95,0.95],num_points=40)
p,v=mt.AddCurves(p1,v1,p2,v2)
p3,v3=mt.RectangleSegments([0.1,0.1],[0.9,0.9],num_points=200)
p,v=mt.AddCurves(p,v,p3,v3)
mesh_pts, elems = mt.DoTriMesh(p,v,edge_length=length)

pt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)

pt.show()