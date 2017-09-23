import numpy as np
import meshtools as mt
import numpy.linalg as la
import matplotlib.pyplot as pt
 
# two semicircles

length=0.5 # Distance between points in the circumference

center1 = [1,0]
radius1 = 1
p,v=mt.CircleSegments(center1,radius1,a_min=-np.pi/2,a_max=np.pi/2,num_points=20)

# plot mesh 
mesh_pts, elems = mt.DoTriMesh(p,v,edge_length=length)

pt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)

pt.show()