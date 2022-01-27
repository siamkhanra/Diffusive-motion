import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5,2.5,10)
f = lambda x : np.exp(-x**2/2)
x = np.linspace(-2.5,2.5,33)
t = np.linspace(0,75,100)
# plt.plot(x,f(x))
# plt.grid()
def diffusion(nt, nx, tmax, xmax, nu):
    dt = tmax/(nt-1)
    dx = xmax/(nx-1)
    x = np.linspace(-2.5,xmax,33)
    t = np.linspace(0,tmax,100)
    r = D*dt/(dx)**2 
    c = np.zeros((nx,nt))  
   # Boundary conditions
    c[-2,:] = c[3,:] = 0
   # Initial conditions 
  
    c[:,0] = 3         
   
    for n in range(0,nt-1):
        for i in range(0,nx-1):
            c[i,n+1] = c[i,n] + D*(dt/dx**2.0)*(c[i+1,n]-2.0*c[i,n]+c[i-1,n])        
    return c,x
D = 1.45
L = 2.5
Tmax =75
dx = 0.075
dt = 0.05
nx = int(L/dx)
nt = int(L/dt)
c, x = diffusion(nt, nx, Tmax, L, D)
def plot_diffusion(c,x,nt):
    """
    Plots the 1D velocity field
    """
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    plt.clf()
    plt.figure()  
    colour=iter(cm.rainbow(np.linspace(0,10,nt)))
    for i in range(0,nt,10):
        d=next(colour)
        plt.plot(x,c[:,i],c = d)
    plt.xlabel('x')
    plt.ylabel('c(x,t)')
    plt.show()
   
plot_diffusion(c,x,nt)
