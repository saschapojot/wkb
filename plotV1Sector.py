import numpy as np

import matplotlib.pyplot as plt
from decimal import Decimal
#potential1, V=x^2+igx^3
N=100
R=140

c=20
rs=np.linspace(start=0,stop=R,num=N)


a1=1/10*np.pi
a2=-3/10*np.pi
a3=-7/10*np.pi
a4=-11/10*np.pi


p0x=[0]*len(rs)
p0y=rs

p1x=[elem*np.sign(np.cos(a1)) for elem in rs]
p1y=[xtmp*np.tan(a1) for xtmp in p1x]

p2x=[elem*np.sign(np.cos(a2)) for elem in rs]
p2y=[xtmp*np.tan(a2) for xtmp in p2x]

p3x=[elem*np.sign(np.cos(a3)) for elem in rs]
p3y=[xtmp*np.tan(a3) for xtmp in p3x]

p4x=[elem*np.sign(np.cos(a4)) for elem in rs]
p4y=[xtmp*np.tan(a4) for xtmp in p4x]


b0=1/4*np.pi

b1=-1/4*np.pi

b2=-3/4*np.pi

b3=-5/4*np.pi



q0x=[elem*np.sign(np.cos(b0)) for elem in rs]
q0y=[xtmp*np.tan(b0) for xtmp in q0x]

q1x=[elem*np.sign(np.cos(b1)) for elem in rs]
q1y=[xtmp*np.tan(b1) for xtmp in q1x]

q2x=[elem*np.sign(np.cos(b2)) for elem in rs]
q2y=[xtmp*np.tan(b2) for xtmp in q2x]

q3x=[elem*np.sign(np.cos(b3)) for elem in rs]
q3y=[xtmp*np.tan(b3) for xtmp in q3x]



fig,ax=plt.subplots(figsize=(20,20))

ax.spines['bottom'].set_color('grey')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_color('grey')
ax.spines['left'].set_position('center')
# ax.set_yticks([])
# ax.set_xticks([])
ax.plot(p0x,p0y,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,color="blue")
ax.plot(q0x,q0y,q1x,q1y,q2x,q2y,q3x,q3y,color="red")
ax.fill_between(p1x, p1y, q1y,color='gainsboro')
ax.fill_between(p4x,p4y,q2y,color="gainsboro")
# ax.fill_between(p2x,p2y,q1y,color="aquamarine")
# ax.fill_between(p5x,p5y,q2y,color="aquamarine")
ax.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
#color filling
p=int(N/2)
#region right I-I

tx=p1x[p]
ty=1/3*(2*p1y[p]+q1y[p])
ax.text(tx,ty,"I-I",fontsize=16)
#region left I-I
tx=p4x[p]
ty=1/3*(2*p4y[p]+q2y[p])
ax.text(tx,ty,"I-I",fontsize=16)


#compute roots
g=0.01
E=g**(-1)*c
coefs=[1j*g,1,0,-E]
rootsAll=np.roots(coefs)

sVal=30
for tmp in rootsAll:
    ax.scatter(np.real(tmp),np.imag(tmp),color="black",s=sVal)


ERe=np.real(E)
EIm=np.imag(E)
ax.set_title("$x^{2}+igx^{3}-E=0$, $g=$"+str(g)+", $E=$"+'{:.2e}'.format(Decimal(str(ERe)))+"+i"+'{:.2e}'.format(Decimal(str(EIm))))




plt.savefig("./potential1/"+str(coefs)+".png")