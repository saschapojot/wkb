from plot4AllFuncs4R12 import *

# this script calculates and plots eigenvalues, potential 4, V(x)=x^{2}-igx^{5}
# Region I-II

num=5
startG=1e-3
stopG=1e-1

gnIndAll = np.linspace(start=np.log10(startG), stop=np.log10(stopG), num=num)
gAll = [10 ** elem for elem in gnIndAll]
EWKB = []



y2=np.exp(-1j*5/6*np.pi)
y1=np.exp(-1j*1/6*np.pi)
# calculate WKB eigenvalues

# calculate WKB eigenvalues
threadNum = 24
energyLevelMax = 3
levelsAll = range(0, energyLevelMax + 1)
inDataAll=[]
for nTmp in levelsAll:
    for gTmp in gAll:
        EEst=2*((nTmp+1/2)*np.pi-gTmp**(-2/3)*I4(y2,y1))/I5(y2,y1)
        if np.abs(gTmp**(2/3)*EEst)<1:
            EEst=np.abs(nTmp+0.5)+0.01j
            inDataAll.append([nTmp,gTmp,EEst])

        else:
            inDataAll.append([nTmp,gTmp,dom5E(nTmp,gTmp)])

tWKBParalStart = datetime.now()
pool1 = Pool(threadNum)
retAll=pool1.map(computeOneSolutionWithInitWith5Pairs,inDataAll)
# inDataAll = []
# for nTmp in levelsAll:
#     for gTmp in gAll:
#         inDataAll.append((nTmp, gTmp))
#
# tWKBParalStart = datetime.now()
# pool1 = Pool(threadNum)
# retAll = pool1.map(computeOneSolution, inDataAll)

tWKBParalEnd = datetime.now()
print("WKB time: ", tWKBParalEnd - tWKBParalStart)

tPltStart = datetime.now()

# plot WKB
fig, ax = plt.subplots(figsize=(20, 20))

# ax.set_xscale('log')
ax.set_yscale('symlog')
ax.set_ylabel("E")
ax.set_xlabel("g")
ax.set_title("Eigenvalues for potential $V(x)=x^{2}-igx^{5}$")

# data serialization
nSctVals = []
gSctVals = []
ERealSctVals = []
EImagSctVals = []
#data serialization
for itemTmp in retAll:
    nTmp, gTmp, ERe, EIm = itemTmp
    nSctVals.append(nTmp)
    gSctVals.append(gTmp)
    ERealSctVals.append(ERe)
    EImagSctVals.append(EIm)


# partitionByN=dict()
# energyLevelSet=set(nSctVals)
# for nTmp in energyLevelSet:
#     partitionByN[nTmp]=[]

#data partition
# for itemTmp in retAll:
#     nTmp,gTmp,ERe,EIm=itemTmp
#     partitionByN[nTmp].append([gTmp,ERe,EIm])

#plot for the same energy level
# for nTmp in partitionByN.keys():
#     gVecTmp=[]
#     EReVecTmp=[]
#     for vecTmp in partitionByN[nTmp]:
#         gVecTmp.append(vecTmp[0])
#         EReVecTmp.append(vecTmp[1])
#     ax.plot(gVecTmp,EReVecTmp,color="red")

# -igx^5 dominant plot

# ngEDom5ValsAll=[]
# for nTmp in levelsAll:
#     for gTmp in gAll:
#         ngEDom5ValsAll.append([nTmp,gTmp,dom5E(nTmp,gTmp)])

#data serialization for -igx^5
# gDom5Vals=[]
# EDom5Vals=[]
# for itemTmp in ngEDom5ValsAll:
#     gDom5Vals.append(itemTmp[1])
#     EDom5Vals.append(itemTmp[2])

#scatter plot of dom5
# dom5Scatter=ax.scatter(gDom5Vals,EDom5Vals,color="blue",marker="+",s=50,label="$-igx^{5}$ dominant")


sctRealPartWKB = ax.scatter(gSctVals, ERealSctVals, color="red", marker=".", s=50, label="WKB real part")
plt.legend()
dirName="/home/users/nus/e0385051/Documents/pyCode/wkb/wkbp4/"
plt.savefig("start"+str(startG)+"stop"+str(stopG)+"num"+str(num)+"tmp125.png")

tPltEnd = datetime.now()
print("plotting time: ", tPltEnd - tPltStart)
