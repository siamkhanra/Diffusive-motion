import numpy as np

x = np.linspace(-2.5,2.5,33)
t = np.linspace(0,75,50)

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
print("x = ",x,"\n\nt = ",t,"\n\nc = ",c)
# def plot_diffusion(c,x):
    
#     import matplotlib.pyplot as plt
#     import matplotlib.cm as cm
#     plt.clf()
#     plt.figure()  
#     x = np.linspace(-2.5,2.5,33)
#     #t = np.linspace(0,75,50)
#     plt.plot(t,c[32,:],'g')
#     plt.xlabel('x')
#     plt.ylabel('c(x,t)')
#     plt.show()
   
# plot_diffusion(c,x)
