import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from astropy.io import ascii


infile='../GRB_Models_Thomas/data/GRB080916009.out'

#data=pd.read_csv(infile,comment='!', sep='',header=None,skiprows=None,skip_blank_lines=True)
#data=pd.read_csv(infile,header=None)
#data_array=data.values
#table=data_array[np.logical_not(np.isnan(data_array[:,0])),:]
#table=data.values
table=ascii.read(infile)
en=table['col1']
flux=table['col2']

en100GeV=en[np.where(en < 100000.0)]
flux100GeV=flux[np.where(en < 100000.0)]

bestfit=np.polyfit(np.log10(en100GeV),np.log10(flux100GeV),1,full= False,cov=True)
# a1=PL index
a1=bestfit[0][0]
# norm A = 10**a2
a2=bestfit[0][1]
da1=(bestfit[1][0,0])**0.5
da2=(bestfit[1][1,1])**0.5
#print "A=",a1,"+/-",da1
#print "n=",a2,"+/-",da2
N0=10**a2

# best fit model
F0=N0*(en100GeV)**a1

#F0=(N0*(1000000.0)**a1)*(en100GeV/1000000.0)**a1
K=N0*(1000000.0)**a1
F0=K*(en100GeV/1000000.0)**a1


print "Prefactor N0 =",K
print "index = ", a1
print "Pivot En. = 1e6 MeV"



plt.xlabel('E[MeV]')
plt.ylabel('flux [ph/cm2/s/MeV]')
plt.loglog(en100GeV,flux100GeV,label='data')
plt.loglog(en100GeV,F0,label='best fit model')
plt.legend()
plt.show()
