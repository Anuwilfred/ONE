import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.tri import Triangulation
 
def f(x, y):
 def f(x,y):
 
x = np.linspace(-6, 6, 3
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid 
 
tri = Triangulation(X.ravel(), Y.ravel
 
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
 
ax.plot_trisurf(tri, Z.ravel(), cmap='cool', edgecolor='none', alpha=0.2)
 
ax.set_title('Surface Triangulation Plot of f(x, y) =\
                sin(sqrt(x^2 + y^2))', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
 
plt.show(
