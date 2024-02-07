import numpy as np
import matplotlib.pyplot as plt

el = -70  # mV, resting potential
vt = -55  # mV, threshold voltage
tau = 10  # ms, membrane time constant

ri0=0
ri1=20
n_ri=200
ri_list=np.linspace(ri0,ri1,n_ri)
f=np.full_like(ri_list,0.0)

t_start=0.0
t_end=1000.0
n_points=50000
delta=(t_end-t_start)/n_points

t=np.linspace(t_start,t_end,n_points)
v0 = el
v=np.full_like(t, v0)

def dvdt(v, ri, el, tau):
    return (el+ri-v)/tau



for ri_i in range(len(ri_list)):
    v=np.full_like(t, v0)
    ri=ri_list[ri_i]
    
    for t_index in range(1,n_points):
        v[t_index]=v[t_index-1]+delta*dvdt(v[t_index-1],ri,el,tau)
        if v[t_index]>vt:
            v[t_index]=v0
            f[ri_i]+=1

f*=1000/(t_end-t_start)
            
plt.figure(figsize=(4, 3))
plt.plot(ri_list, f)
plt.xlabel('I')
plt.ylabel('f')
plt.grid(False)
plt.tight_layout()
plt.savefig('fIcurve.png')
plt.show()

