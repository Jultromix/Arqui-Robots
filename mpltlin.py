from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

def plot_3D_cylinder(radius, height, elevation=0, resolution=100, color='r', x_center = 0, y_center = 0):
    fig=plt.figure()
    ax = Axes3D(fig, azim=30, elev=30)

    x = np.linspace(x_center-radius, x_center+radius, resolution)
    z = np.linspace(elevation, elevation+height, resolution)
    X, Z = np.meshgrid(x, z)

    Y = np.sqrt(radius**2 - (X - x_center)**2) + y_center # Pythagorean theorem

    ax.plot_surface(X, Y, Z, linewidth=0, color=color)
    ax.plot_surface(X, (2*y_center-Y), Z, linewidth=0, color=color)

    #Caras superior e inferior del cilindro
    floor = Circle((x_center, y_center), radius, color=color)
    ax.add_patch(floor)
    art3d.pathpatch_2d_to_3d(floor, z=elevation, zdir="z")

    ceiling = Circle((x_center, y_center), radius, color=color)
    ax.add_patch(ceiling)
    art3d.pathpatch_2d_to_3d(ceiling, z=elevation+height, zdir="z")

    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')

    plt.show()

# params
radius = 3
height = 10
elevation = -5
resolution = 100
color = 'r'
x_center = 3
y_center = -2

plot_3D_cylinder(radius, height, elevation=elevation, resolution=resolution, color=color, x_center=x_center, y_center=y_center)
# #https://stackoverflow.com/questions/26989131/add-cylinder-to-plot


#Cilindro sin "tapas"
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Scatter graph
# N = 100
# X = np.random.uniform(-1, 1, N)
# Y = np.random.uniform(-1, 1, N)
# Z = np.random.uniform(-2, 2, N)
# ax.scatter(X, Y, Z)

# # Cylinder
# x=np.linspace(-1, 1, 100)
# z=np.linspace(-2, 2, 100)
# Xc, Zc=np.meshgrid(x, z)
# Yc = np.sqrt(1-Xc**2)

# # Draw parameters
# rstride = 20
# cstride = 10
# ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)
# ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)

# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# plt.show()