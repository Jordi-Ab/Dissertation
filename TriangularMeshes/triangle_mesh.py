import numpy as np
import meshpy.triangle as triangle
import numpy.linalg as la
import matplotlib.pyplot as plt


length=0.3

# Straight line
def LineSegments(P1,P2,num_points=10,edge_length=-1):
  
  number_points=num_points
  if edge_length>0:
    p1=np.array(P1)
    p2=np.array(P2)
    number_points=np.floor(np.sqrt(np.sum((p2-p1)**2))/edge_length)+1
  
  t=np.linspace(0,1,number_points)
  points=[(P1[0]+param*(P2[0]-P1[0]),P1[1]+param*(P2[1]-P1[1])) for param in t]
  vertices=[(j,j+1) for j in range(0,len(points)-1,1)]
  return points,vertices;

def DoTriMesh(points,vertices,edge_length=-1,holes=[],tri_refine=None):
  info = triangle.MeshInfo()
  info.set_points(points)
  if len(holes)>0:
    info.set_holes(holes)
  info.set_facets(vertices)


  if tri_refine!=None:
    mesh = triangle.build(info,refinement_func=tri_refine)
  elif edge_length<=0:
    mesh = triangle.build(info)   
  else:
    mesh = triangle.build(info,max_volume=0.5*edge_length**2)
  
  mesh_points = np.array(mesh.points)
  mesh_elements = np.array(mesh.elements)
  
  
  plt.triplot(mesh_points[:, 0], mesh_points[:, 1], mesh_elements,) 
  plt.show()
  return mesh_points,mesh_elements;  

# check relative position of two points   
def SamePoint(p1,p2,delta):
  dp=(np.array(p1)-np.array(p2))
  d=np.sqrt(dp[0]**2+dp[1]**2)
  ret=False  
  if d<delta:
    ret=True
  return ret;

#Connect two different polygons  
def AddSegments(P1,P2,closed=False):  
  p1=np.array(P1)
  p2=np.array(P2)
  # find smallest distance within points p1 and p2
  min1=np.min(np.sqrt(np.sum((p1[1:]-p1[:-1])**2,axis=1)))
  min2=np.min(np.sqrt(np.sum((p2[1:]-p2[:-1])**2,axis=1)))
  delta=np.min([min1,min2])
  
  # Add second curve to first curve 
  del_first=SamePoint(p1[-1],p2[0],delta)
  Pall=P1[:]  
  if del_first==True:
    Pall+=P2[1:]
  else:
    Pall+=P2
  
  # check if Pall is closed 
  del_last=SamePoint(Pall[-1],p1[0],delta)
  if del_last==True:
    Pall=Pall[:-1]
    
  vertices=[(j,j+1) for j in range(0,len(Pall)-1,1)]
  if (del_last==True) or (closed==True):
    vertices+=[(len(Pall)-1,0)]
  
  return Pall,vertices;  

#
# simple mesh triangle
#
p1,v1=LineSegments([2,2],[-1,-3],edge_length=length)
p2,v2=LineSegments([-1,-3],[3,-1],num_points=10)
p,v=AddSegments(p1,p2,closed=True)
DoTriMesh(p,v)