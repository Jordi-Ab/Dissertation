
# coding: utf-8

# In[1]:

from meshtools import *
import numpy as np
import matplotlib.pyplot as pt


# Triangulate mesh
upp_crnr = [2,2]
low_crnr = [0,0]
p, v = RectangleSegments(upp_crnr,low_crnr,edge_length=1)
mesh_pts, elems = DoTriMesh(p,v,edge_length=1)

print("Mesh Points:")
print(mesh_pts)
print("Elements:")
print(elems)
# In[35]:

pt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems, color='b')
pt.title(r"$\Omega$")
pt.xlim(-0.3,2.3)
pt.ylim(-0.3,2.3)
pt.xlabel("x")
pt.ylabel("y")
for i, elem in enumerate(elems):
	v1,v2,v3 = mesh_pts[elem]
	pt.text(v1[0], v1[1], str(elem[0]), color='r')
	pt.text(v2[0], v2[1], str(elem[1]), color='r')
	pt.text(v3[0], v3[1], str(elem[2]), color='r')
	m_p1 = (v1+v2)/2
	m_px = v3[0] + (2/3)*(m_p1[0]-v3[0])
	m_py = v3[1] + (2/3)*(m_p1[1]-v3[1])
	pt.text(m_px, m_py, str(i), color='g')
	
pt.savefig("Connectivity.png")
pt.show()



