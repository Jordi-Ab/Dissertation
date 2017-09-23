import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import meshtools as mt

#
# 2D curve
#
length = 0.3

t=np.linspace(0,2*np.pi,120)

r=3+np.sin(8*t)
x=r*np.cos(t)
y=r*np.sin(t)

p=[(x[j],y[j]) for j in range(len(t))]
p1,v1=mt.PointSegments(p)

mesh_pts, elems = mt.DoTriMesh(p1,v1,edge_length=length)
#plt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)

# Triangulate parameter space to determine the triangles
tri = mtri.Triangulation(mesh_pts[:,0], mesh_pts[:,1], triangles=elems)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y,t, triangles=tri.triangles, color = 'w')
ax.set_title('2D Torus with Delaunay Triangulation')
ax.set_zlim(-1, 1)

plt.show()