import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from six.moves import range
from meshpy.tet import MeshInfo, build
from math import pi, cos, sin
from meshpy.geometry import generate_surface_of_revolution,\
            EXT_CLOSED_IN_RZ, GeometryBuilder


big_r = 3
little_r = 2.9

points = 50
dphi = 2*pi/points

rz = [(big_r+little_r*cos(i*dphi), little_r*sin(i*dphi))
        for i in range(points)]

geob = GeometryBuilder()
geob.add_geometry(*generate_surface_of_revolution(rz,
        closure=EXT_CLOSED_IN_RZ, radial_subdiv=20))

mesh_info = MeshInfo()
geob.set(mesh_info)

print(mesh_info)