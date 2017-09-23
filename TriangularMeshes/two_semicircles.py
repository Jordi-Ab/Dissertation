import numpy as np
import meshtools as mt
import numpy.linalg as la
import matplotlib.pyplot as pt
 
# two semicircles

length=0.5 # Distance between points in the circumference

#Right circle
l_center = [-2,0]
l_radius = 3
p1,v1=mt.CircleSegments(l_center,l_radius,num_points=20)

# Left circle
r_center = [2,0]
r_radius = 3
p2,v2=mt.CircleSegments(r_center,r_radius,num_points=20)

# join them
p,v=mt.AddCurves(p1,v1,p2,v2)

# plot mesh 
mesh_pts, elems = mt.DoTriMesh(p,v,edge_length=length)

fig = pt.figure(figsize = (10,10))
ax = fig.add_subplot(111)
ax.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)
pt.axis('scaled')
pt.show()