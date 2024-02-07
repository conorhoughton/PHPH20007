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

theta_E=0.5
theta_I=0.0

t0=0
t1=0.5
n_points=1000

t=np.linspace(t0,t1,n_points)
delta=(t1-t0)/n_points


e=np.full_like(t, 0.5)
h=np.full_like(t, 0.0)

e_input=theta_E+w_EE*e[0]-w_IE*h[0]
initial_dedt=dadt(e[0],tau_E,beta,e_input)

dedt_list=np.full_like(t, initial_dedt)


h_input=theta_E+w_EI*e[0]
initial_dhdt=dadt(h[0],tau_I,beta,h_input)

dhdt_list=np.full_like(t, initial_dhdt)



#avoid using "i" as a variable, since we often use i for an index
#it is easy to make a mistake, it is common to use h in this situation
#I imagine for iHibatory.

for t_index in range(1,n_points):
  e_input=theta_E+w_EE*e[t_index-1]-w_IE*h[t_index-1]
  dedt_list[t_index]=dadt(e[t_index-1],tau_E,beta,e_input)
  e[t_index]=e[t_index-1]+delta*dedt_list[t_index]
  h_input=theta_I+w_EI*e[t_index-1]
  dhdt_list[t_index]=dadt(h[t_index-1],tau_I,beta,h_input)
  h[t_index]=h[t_index-1]+delta*dadt(h[t_index-1],tau_I,beta,h_input)


plt.figure(figsize=(3, 2))
plt.plot(e[1:],dedt_list[1:],label="$E$")
plt.plot(h[1:],dhdt_list[1:],label="$I$")

plt.xlabel('E or I')
plt.ylabel('dE/dt or dI/dt')
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.savefig('phase.png')
plt.show()


# plt.figure(figsize=(6, 4))
# plt.plot(t, e,label=r"$E$")
# plt.plot(t, h,label=r"$I$")
# plt.xlabel('t')
# plt.ylabel('a')
# plt.legend()
# plt.grid(True)
# plt.show()
