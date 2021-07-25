import numpy as np

import matplotlib.pyplot as plt
from decimal import Decimal
#potential 8, V(x)=x^{4}-igx^{5}
N=100
R=650

c=1e10
rs=np.linspace(start=0,stop=R,num=N)



a1=3/14*np.pi

a2=-1/14*np.pi

a3=-5/14*np.pi

a4=-9/14*np.pi

a5=-13/14*np.pi

a6=-17/14*np.pi

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

p5x=[elem*np.sign(np.cos(a5)) for elem in rs]
p5y=[xtmp*np.tan(a5) for xtmp in p5x]

p6x=[elem*np.sign(np.cos(a6)) for elem in rs]
p6y=[xtmp*np.tan(a6) for xtmp in p6x]



b1=1/6*np.pi

b2=-1/6*np.pi

b4=-5/6*np.pi

b5=-7/6*np.pi

q0x=[0]*len(rs)
q0y=rs

q1x=[elem*np.sign(np.cos(b1)) for elem in rs]
q1y=[xtmp*np.tan(b1) for xtmp in q1x]

q2x=[elem*np.sign(np.cos(b2)) for elem in rs]
q2y=[xtmp*np.tan(b2) for xtmp in q2x]

q3x=[0]*len(rs)
q3y=[-elem for elem in rs]

q4x=[elem*np.sign(np.cos(b4)) for elem in rs]
q4y=[xtmp*np.tan(b4) for xtmp in q4x]

q5x=[elem*np.sign(np.cos(b5)) for elem in rs]
q5y=[xtmp*np.tan(b5) for xtmp in q5x]

fig,ax=plt.subplots(figsize=(20,20))

ax.spines['bottom'].set_color('grey')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_color('grey')
ax.spines['left'].set_position('center')
# ax.set_yticks([])
# ax.set_xticks([])
ax.plot(p0x,p0y,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y,p6x,p6y,color="blue")
ax.plot(q0x,q0y,q1x,q1y,q2x,q2y,q3x,q3y,q4x,q4y,q5x,q5y,color="red")
ax.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
#color filling
#right I-I
ax.fill_between(q1x, q1y, p2y,color='gainsboro')
#left I-I
ax.fill_between(q5x,q5y,p5y,color="gainsboro")
#right I-II
ax.fill_between(p2x,p2y,q2y,color="aquamarine")
#left I-II
ax.fill_between(p5x,p5y,q4y,color="aquamarine")
#text
p=int(N/2)
#region right I-I

tx=q1x[p]
ty=1/3*(2*q1y[p]+p2y[p])
ax.text(tx,ty,"I-I",fontsize=16)
#region left I-I
tx=q5x[p]
ty=1/3*(2*q5y[p]+p5y[p])
ax.text(tx,ty,"I-I",fontsize=16)
#region right I-II
tx=p2x[p]
ty=1/3*(2*p2y[p]+q2y[p])
ax.text(tx,ty,"I-II",fontsize=16)
#region left I-II
tx=p5x[p]
ty=1/3*(2*p5y[p]+q4y[p])
ax.text(tx,ty,"I-II",fontsize=16)
#compute roots
g=0.01
E=g**(-1)*c
coefs=[-1j*g,1,0,0,0,-E]
rootsAll=np.roots(coefs)
print(np.abs(rootsAll))
sVal=30
for tmp in rootsAll:
    ax.scatter(np.real(tmp),np.imag(tmp),color="black",s=sVal)

ax.set_title("$x^{4}-igx^{5}-E=0$, $g=$"+str(g)+", $E=$"+'{:.2e}'.format(Decimal(str(E))))



plt.savefig("./potential8/"+str(coefs)+".png")