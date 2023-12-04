# SIMULATION OF HALOS
# SIMPLE CASE

import matplotlib.pyplot as plt
import numpy as np
import scienceplots
plt.style.use(["science", "nature"])

def mysin(x):
    return np.sin(x*np.pi/180)

def mycos(x):
    return np.cos(x*np.pi/180)

def mytan(x):
    return np.tan(x*np.pi/180)

def get_a2(a1, n):
    x = mysin(a1)/n
    r = np.arcsin(x)
    r = r*180/np.pi #converting to degrees
    return r

def get_a4(a1, n):
    x = mysin(a1)*n
    r = np.arcsin(x)
    r = r*180/np.pi #converting to degrees
    return r


def perpen(a1, a2):
    n = mysin(a1 - a2)
    d = mysin(a1 + a2)
    return -n/d

def paralel(a1, a2):
    n = mytan(a1 - a2)
    d = mytan(a1 + a2)
    return n/d

def fresnel(a1, a2):
    par = paralel(a1, a2)
    per = perpen(a1, a2)
    r = (par**2 + per**2)
    return r

## start params
nrays = 50000
n = 1.31 #refrction
gam = 60 #gamma of prism

a_1 = np.random.uniform(0,90,nrays)
a_2 = get_a2(a_1, n)
fres = fresnel(a_1, a_2)
probs = np.random.uniform(0,1,nrays)

angle = np.zeros(nrays)
angle2 = []; angle3 = []
cnta = 0
cnta2 = 0

for j in range(len(probs)):
    if probs[j] <= fres[j]:
        #is reflected
        angle[j] = 180 - 2*a_1[j]
        
    else:
        #is transmitted
        a_3 = gam - a_2[j]
        aux = n*mysin(a_3)
        
        if aux >= 1:
            #angle[j] = np.random.uniform(0,180,1)
            angle[j] = np.nan
        else:
            a_4 = get_a4(a_3, 1.31)
            frs = fresnel(a_3, a_4)
            #print(frs)
            prb = np.random.uniform(0, 1,1)
            if prb <= frs:
                #reflected
                cnta2 = cnta2 + 1
                angle[j] = 180 - 2*a_3
                angle2.append(180 - 2*a_3)
            else:
                cnta = cnta + 1
                angle[j] = a_1[j] + a_4 - a_2[j] - a_3
                angle3.append(angle[j])


print(cnta2)
print(cnta)
plt.figure()
plt.hist(angle, bins = 40)
plt.savefig("histo.png", dpi = 400)


plt.figure()
plt.hist(fres, bins = 40)
plt.savefig("fresnel.png", dpi = 400)


theta = np.random.uniform(0,2*np.pi,len(angle))
r = angle
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
ax.set_rlim(0,50)
c = ax.scatter(theta, r, s = 0.5, alpha = 0.5)
plt.savefig("polar3.png", dpi = 400)
plt.show()
