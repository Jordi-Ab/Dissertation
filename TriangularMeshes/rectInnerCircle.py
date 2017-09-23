import meshtools as mt
import numpy.linalg as la
import matplotlib.pyplot as pt

length=0.2
p1,v1=mt.RectangleSegments([-2,-2],[2,2],edge_length=length)
p2,v2=mt.CircleSegments([0,0],1,edge_length=length/5)
p,v=mt.AddCurves(p1,v1,p2,v2)
mesh_pts, elems = mt.DoTriMesh(p,v,edge_length=length/2)

pt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)

pt.show()