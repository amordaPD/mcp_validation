
import sys

import itertools

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd 
from pandas.plotting import scatter_matrix
from sklearn import mixture

#####reading input data######
event_ID = str(sys.argv[1])
particle = ''
if(event_ID=='1111440100'):
    particle = '$\mu_{J/\psi}$'
elif(event_ID=='1111540100'):
    particle = '$e_{J/\psi}$'
elif (event_ID=='1110048100'):
    particle = '$\pi_{\eta^\prime}$'

output_path=''#D:\Padova\Presentazioni\DP_reports\DP_131017\PID_plots\ '    
#####MC9#####
print("reading mc9 input data")
PIDe_Jpsi_mc9  = []
PIDmu_Jpsi_mc9  = []
PIDpi_Jpsi_mc9  = []
PIDk_Jpsi_mc9  = []

with open('mc9_PID_'+event_ID+'.txt', 'r') as f_mc9:
    content = f_mc9.readlines()
    content = content[3:-2]
    for x in content:
        row = x.split("*")
        PIDe_Jpsi_mc9.append(float(row[2])) 
        PIDmu_Jpsi_mc9.append(float(row[3])) 
        PIDpi_Jpsi_mc9.append(float(row[4])) 
        PIDk_Jpsi_mc9.append(float(row[5])) 
print("input mc9 data read")
X_mc9=np.column_stack((PIDe_Jpsi_mc9,PIDmu_Jpsi_mc9,PIDpi_Jpsi_mc9,PIDk_Jpsi_mc9));

#####MC8#####
print("reading mc8 input data")
PIDe_Jpsi_mc8  = []
PIDmu_Jpsi_mc8  = []
PIDpi_Jpsi_mc8  = []
PIDk_Jpsi_mc8  = []

with open('mc8_PID_'+event_ID+'.txt', 'r') as f_mc8:
    content = f_mc8.readlines()
    content = content[3:-2]
    for x in content:
        row = x.split("*")
        PIDe_Jpsi_mc8.append(float(row[2])) 
        PIDmu_Jpsi_mc8.append(float(row[3])) 
        PIDpi_Jpsi_mc8.append(float(row[4])) 
        PIDk_Jpsi_mc8.append(float(row[5])) 
print("input mc8 data read")
X_mc8=np.column_stack((PIDe_Jpsi_mc8,PIDmu_Jpsi_mc8,PIDpi_Jpsi_mc8,PIDk_Jpsi_mc8));



'''
d_PID_mc8 = {particle+'0 PIDe':PIDe_Jpsi_mc8 ,particle+'0 PIDmu':PIDmu_Jpsi_mc8 , particle+'0 PIDpi':PIDpi_Jpsi_mc8}# ,particle+'0 PIDk':PIDk_Jpsi_mc8 }
df_PID_mc8 = pd.DataFrame(data=d_PID_mc8)
sm8= scatter_matrix(df_PID_mc8, alpha=0.2, figsize=(6, 6), diagonal='kde')
for i, sm8 in enumerate(sm8):
    for j, ax in enumerate(sm8):
        if i == j:  # only diagonal plots
            ax.set_yscale('log')
            ax.set_ylim(0,1000)
plt.suptitle('PID mc8 '+particle )
plt.savefig(output_path+'mc8_'+event_ID+'_scatter.png')

d_PID_mc9 = {particle+'0 PIDe':PIDe_Jpsi_mc9 ,particle+'0 PIDmu':PIDmu_Jpsi_mc9 , particle+'0 PIDpi':PIDpi_Jpsi_mc9}#  ,particle+'0 PIDk':PIDk_Jpsi_mc9 }
df_PID_mc9 = pd.DataFrame(data=d_PID_mc9)
sm9 = scatter_matrix(df_PID_mc9, alpha=0.2, figsize=(6, 6), diagonal='kde' )
for i, sm9 in enumerate(sm9):
    for j, ax in enumerate(sm9):
        if i == j:  # only diagonal plots
            ax.set_yscale('log')
            ax.set_ylim(0,1000)
#scatter_matrix(df_PID_mc9, alpha=0.2, figsize=(6, 6))#, diagonal='kde')
plt.suptitle('PID mc9 '+particle )
plt.savefig(output_path+'mc9_'+event_ID+'_scatter.png')
'''


labels= ["mc8","mc9"]
set_y_axis = True
fig_PID, axs_PID = plt.subplots(1, 3, figsize=(15, 5))
axs_PID[0].hist(PIDe_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[0].hist(PIDe_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[0].set_xlabel( particle+'0 PIDe')
axs_PID[0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[0].set_yscale('log')
plt.legend(labels)
axs_PID[1].hist(PIDmu_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[1].hist(PIDmu_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[1].set_xlabel( particle+'0 PIDmu')
axs_PID[1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[1].set_yscale('log')
plt.legend(labels)
axs_PID[2].hist(PIDpi_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[2].hist(PIDpi_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[2].set_xlabel( particle+'0 PIDpi')
axs_PID[2].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[2].set_yscale('log')
plt.legend(labels)
'''
axs_PID[3].hist(PIDk_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[3].hist(PIDk_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.4)
axs_PID[3].set_xlabel( particle+'0 PIDk')
axs_PID[3].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[3].set_yscale('log')
plt.legend(labels)
'''

'''
fig_PID_test, axs_PID_test = plt.subplots(1, 3, figsize=(15, 5))
vect_test=X_mc8[np.where(X_mc8[1]>0)]
axs_PID_test[0].hist(vect_test[1],100,range=[0,1], normed=True,alpha=0.4)
axs_PID_test[0].hist(PIDe_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.4)
axs_PID_test[0].set_xlabel( particle+'0 PIDe')
axs_PID_test[0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID_test[0].set_yscale('log')
plt.legend(labels)
axs_PID_test[1].hist(PIDmu_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.4)
axs_PID_test[1].hist(PIDmu_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.4)
axs_PID_test[1].set_xlabel( particle+'0 PIDmu')
axs_PID_test[1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID_test[1].set_yscale('log')
plt.legend(labels)
axs_PID_test[2].hist(PIDpi_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.4)
axs_PID_test[2].hist(PIDpi_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.4)
axs_PID_test[2].set_xlabel( particle+'0 PIDpi')
axs_PID_test[2].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID_test[2].set_yscale('log')
plt.legend(labels)

'''

'''
set_y_axis = True
axs_PID[1, 0].hist(PIDe_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 0].hist(PIDe_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 0].set_xlabel( particle+'0 PIDe')
axs_PID[1, 0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[1, 0].set_yscale('log')
plt.legend(labels)
axs_PID[1, 1].hist(PIDmu_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 1].hist(PIDmu_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 1].set_xlabel( particle+'0 PIDmu')
axs_PID[1, 1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[1, 1].set_yscale('log')
plt.legend(labels)
axs_PID[1, 2].hist(PIDpi_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 2].hist(PIDpi_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 2].set_xlabel( particle+'0 PIDpi')
axs_PID[1, 2].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[1, 2].set_yscale('log')
plt.legend(labels)
axs_PID[1, 3].hist(PIDk_Jpsi_mc8,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 3].hist(PIDk_Jpsi_mc9,100,range=[0,1], normed=True,alpha=0.7)
axs_PID[1, 3].set_xlabel( particle+'0 PIDk')
axs_PID[1, 3].set_ylabel('A.U.')
if (set_y_axis) :
    axs_PID[1, 3].set_yscale('log')
plt.legend(labels)
'''
    
fig_PID.subplots_adjust(hspace=0.26,left=0.08,right=0.98,top=0.98,bottom=0.15)

#plt.show()
