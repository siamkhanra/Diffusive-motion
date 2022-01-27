import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5,2.5,33)
t = np.linspace(0,75,100)

# Function Define
def diffusion(nt, nx, tmax, xmax, nu):
    dt = tmax/(nt-1)
    dx = xmax/(nx-1)
    x = np.linspace(-2.5,xmax,33)
    c = np.zeros((nx,nt))  
    
    # Initial conditions  
    c[:,0] = np.exp(-x**2/2)
    # Boundary conditions
    for i in range(0,5) : # 0 to 2L = 2*2.5 = 5 
     c[0,:] = c[5,:] = 0 
    # Generating the iterative equation       
    for n in range(0,nt-1):
        for i in range(0,nx-1):
            c[i,n+1] = c[i,n] + D*(dt/dx**2.0)*(c[i+1,n]-2.0*c[i,n]+c[i-1,n])        
    return c,x

# Initialize the value
D = 1.45
L = 2.5
Tmax =75
dx = 0.075
dt = 0.05
nx = int(L/dx)
nt = int(L/dt)

# Function calling 
c, x = diffusion(nt, nx, Tmax, L, D)

p = np.linspace(-2.5,2.5,50) # For keeping same shape 
k = np.linspace(0,75,33) # For keeping same shape 
X, T = np.meshgrid(p, k)
#Z = c[p,k]
#plt.contour(c,200, color='black')
plt.contourf(X,T,c,20,cmap='gist_heat')
plt.colorbar()

