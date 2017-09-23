import numpy as np
import meshtools as mt
import numpy.linalg as la
import matplotlib.pyplot as pt

length=0.5

#Left circle
l_center = [-6,0]
l_radius = 3
pc1,vc1=mt.CircleSegments(l_center,l_radius,num_points=20)

#Rectangle
rp,rv=mt.RectangleSegments([-6,-1],[6,1],edge_length=length)

# join them
#p,v=mt.AddSegments(pc1,rp,closed = True)
p1,v1 = mt.AddCurves(pc1,vc1,rp,rv)

#Right circle
r_center = [6,0]
r_radius = 3
pc2,vc2=mt.CircleSegments(r_center,r_radius,num_points=20)

# join them
#p,v=mt.AddSegments(pc1,rp,closed = True)
p,v = mt.AddCurves(pc2,vc2,p1,v1)

# plot mesh 
mesh_pts, elems = mt.DoTriMesh(p,v,edge_length=length)

fig = pt.figure(figsize = (10,10))
ax = fig.add_subplot(111)
ax.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)
pt.axis('scaled')

pt.show()