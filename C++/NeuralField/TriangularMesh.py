from meshtools import *
import matplotlib.pyplot as pt
import numpy as np

generate_plot = False

# Triangulated mesh
Lx=-30; Ux=30
Ly=-30; Uy=30
p,v=RectangleSegments([Ux,Uy],[Lx, Ly],edge_length=5)
mesh_pts, elems = DoTriMesh(p,v,edge_length=5)

np.savetxt('mesh_points.dat',mesh_pts)
np.savetxt('elements.dat',elems, '%d')

# plot mesh
if generate_plot:
	pt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)
	pt.show()
