import numpy as np
import matplotlib.pyplot as plt



def f(theta,beta):
    return 1/(1+np.exp(-beta*(theta-1)))

def dadt(a,tau,beta,input):
  return (-a+f(input,beta))/tau

beta=4.0

tau_E=0.0032
tau_I=0.0032

w_EE=2.4
w_IE=2.0
w_EI=2.0

theta_points=100
theta0=0.0
theta1=2.0
theta_E_values=np.linspace(theta0,theta1,theta_points)
theta_I=0.0

t0=0
t1=0.5
n_points1=500
n_points =1000

t=np.linspace(t0,t1,n_points)
delta=(t1-t0)/n_points

e_max=[]
e_min=[]

for theta_E in theta_E_values:
    e=np.full_like(t, 0.5)
    h=np.full_like(t, 0.0)

    for t_index in range(1,n_points):
        e_input=theta_E+w_EE*e[t_index-1]-w_IE*h[t_index-1]
        e[t_index]=e[t_index-1]+delta*dadt(e[t_index-1],tau_E,beta,e_input)
        h_input=theta_I+w_EI*e[t_index-1]
        h[t_index]=h[t_index-1]+delta*dadt(h[t_index-1],tau_I,beta,h_input)

    max_val=max(e[n_points1:])
    min_val=min(e[n_points1:])
        
    e_max.append(max_val)
    e_min.append(min_val)



    
plt.figure(figsize=(4, 3))
plt.plot(theta_E_values, e_max,  color='black')
plt.plot(theta_E_values, e_min,  color='black')

plt.xlabel(r'$\theta_E$')
plt.ylabel(r'$e$')
plt.grid(True)
plt.tight_layout()
plt.savefig('theta.png')
plt.show()
