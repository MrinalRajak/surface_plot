

# surface plot

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(0.0,20.0,100)
y=np.linspace(0.0,4.0,100)
X,Y=np.meshgrid(x,y)
Z=(20/np.pi)*np.exp(-np.pi*Y/10)*np.sin(2*np.pi*x/10)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
aa=ax.plot_surface(X,Y,Z,cmap='plasma')
fig.colorbar(aa,shrink=0.5)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_xticks([0.0,5.0,10.0,15.0,20.0])
ax.set_yticks([0.0,1.0,2.0,3.0,4.0])
ax.set_title("surface plot")
plt.show()
