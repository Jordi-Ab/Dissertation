import numpy as np
import meshtools as mt
import numpy.linalg as la
import matplotlib.pyplot as pt

length = 0.3

center = [0,0]

radius1 = 2
p1,v1=mt.CircleSegments(center,radius1,edge_length=length)

p2,v2=mt.CircleSegments([0,0],1,edge_length=length)
p,v=mt.AddCurves(p1,v1,p2,v2)
# function for refinement
def myrefine2(tri_points, area):
  center_tri = np.sum(np.array(tri_points), axis=0)/3.
  r=np.sqrt(center_tri[0]**2+center_tri[1]**2) 
  max_area=0.3+(0.01-0.3)/(1+0.5*(r-1)**2)
  return bool(area>max_area);
#mesh_pts1, elems1 = mt.DoTriMesh(p1,v1,tri_refine=myrefine2)  
mesh_pts2, elems2 = mt.DoTriMesh(p,v,tri_refine=myrefine2)

#spt.triplot(mesh_pts1[:, 0], mesh_pts1[:, 1], elems1)
pt.triplot(mesh_pts2[:, 0], mesh_pts2[:, 1], elems2)

pt.show()