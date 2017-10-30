
import itertools

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd 
from pandas.plotting import scatter_matrix
from sklearn import mixture
from matplotlib.colors import LogNorm

#####reading input data######

#####MC9#####
print("reading mc9 input data")
nPXD_Jpsi_mu0_mc9  = []
nPXD_Jpsi_mu1_mc9  = []
nSVD_Jpsi_mu0_mc9  = []
nSVD_Jpsi_mu1_mc9  = []
B0_Sig_VtxPval_mc9 = []
B0_Tag_VtxPval_mc9 = []
B0_Sig_VtxRes_mc9  = []
B0_Tag_VtxRes_mc9  = []
KS0_M_mc9     = []
Jpsi_M_mc9      = []
B0_mbc_mc9    = []
B0_deltae_mc9 = []
ROETracks_mc9          = []
ROEECLClusters_mc9     = []
GoodROEECLClusters_mc9 = []
ROEKLMClusters_mc9     = []
Jpsi_mu0_TrPval_mc9 = []
Jpsi_mu1_TrPval_mc9 = []
KS0_pi0_TrPval_mc9 = []
KS0_pi1_TrPval_mc9 = []
nPXD_KS0_pi0_mc9  = []
nPXD_KS0_pi1_mc9  = []
nSVD_KS0_pi0_mc9  = []
nSVD_KS0_pi1_mc9  = []
KS0_VtxPval_mc9 = []
DeltaTRes_mc9 = []
nCDC_KS0_pi0_mc9  = []
nCDC_KS0_pi1_mc9  = []
nCDC_Jpsi_mu0_mc9  = []
nCDC_Jpsi_mu1_mc9  = []







with open('mc9_1111440100.txt', 'r') as f_mc9:
    content = f_mc9.readlines()
    content = content[3:-2]
    for x in content:
        row = x.split("*")
        if(float(row[6])>5.250):
            nPXD_Jpsi_mu0_mc9.append(float(row[2]))
            nPXD_Jpsi_mu1_mc9.append(float(row[3]))
            nSVD_Jpsi_mu0_mc9.append(float(row[4]))
            nSVD_Jpsi_mu1_mc9.append(float(row[5]))    
            B0_mbc_mc9.append(float(row[6]))  
            B0_deltae_mc9.append(float(row[7])) 
            Jpsi_M_mc9.append(float(row[8]))
            KS0_M_mc9.append(float(row[9]))
            ROETracks_mc9.append(float(row[10]))      
            ROEECLClusters_mc9.append(float(row[11]))  
            GoodROEECLClusters_mc9.append(float(row[12]))
            ROEKLMClusters_mc9.append(float(row[13]))  
            B0_Sig_VtxPval_mc9.append(float(row[14])) 
            B0_Tag_VtxPval_mc9.append(float(row[15])) 
            B0_Sig_VtxRes_mc9.append(float(row[16])) 
            B0_Tag_VtxRes_mc9.append(float(row[17])) 
            Jpsi_mu0_TrPval_mc9.append(float(row[18]))
            Jpsi_mu1_TrPval_mc9.append(float(row[19]))
            KS0_pi0_TrPval_mc9.append(float(row[20]))
            KS0_pi1_TrPval_mc9.append(float(row[21]))
            nPXD_KS0_pi0_mc9.append(float(row[22])) 
            nPXD_KS0_pi1_mc9.append(float(row[23]))
            nSVD_KS0_pi0_mc9.append(float(row[24])) 
            nSVD_KS0_pi1_mc9.append(float(row[25])) 
            KS0_VtxPval_mc9.append(float(row[26]))  
            DeltaTRes_mc9.append(float(row[27]))
            nCDC_Jpsi_mu0_mc9.append(float(row[28]))  
            nCDC_Jpsi_mu1_mc9.append(float(row[29]))  
            nCDC_KS0_pi0_mc9.append(float(row[30])) 
            nCDC_KS0_pi1_mc9.append(float(row[31])) 
print("input mc9 data read")

#####MC8#####
print("reading mc8 input data")
nPXD_Jpsi_mu0_mc8  = []
nPXD_Jpsi_mu1_mc8  = []
nSVD_Jpsi_mu0_mc8  = []
nSVD_Jpsi_mu1_mc8  = []
B0_Sig_VtxPval_mc8 = []
B0_Tag_VtxPval_mc8 = []
B0_Sig_VtxRes_mc8  = []
B0_Tag_VtxRes_mc8  = []
KS0_M_mc8     = []
Jpsi_M_mc8      = []
B0_mbc_mc8    = []
B0_deltae_mc8 = []
ROETracks_mc8          = []
ROEECLClusters_mc8     = []
GoodROEECLClusters_mc8 = []
ROEKLMClusters_mc8     = []
Jpsi_mu0_TrPval_mc8 = []
Jpsi_mu1_TrPval_mc8 = []
KS0_pi0_TrPval_mc8 = []
KS0_pi1_TrPval_mc8 = []
nPXD_KS0_pi0_mc8  = []
nPXD_KS0_pi1_mc8  = []
nSVD_KS0_pi0_mc8  = []
nSVD_KS0_pi1_mc8  = []
KS0_VtxPval_mc8 = []
DeltaTRes_mc8 = []
nCDC_KS0_pi0_mc8  = []
nCDC_KS0_pi1_mc8  = []
nCDC_Jpsi_mu0_mc8  = []
nCDC_Jpsi_mu1_mc8  = []



with open('mc8_1111440100.txt', 'r') as f_mc8:
    content = f_mc8.readlines()
    content = content[3:-2]
    for x in content:
        row = x.split("*")
        if(float(row[6])>5.250):
            nPXD_Jpsi_mu0_mc8.append(float(row[2]))
            nPXD_Jpsi_mu1_mc8.append(float(row[3]))
            nSVD_Jpsi_mu0_mc8.append(float(row[4]))
            nSVD_Jpsi_mu1_mc8.append(float(row[5]))    
            B0_mbc_mc8.append(float(row[6]))  
            B0_deltae_mc8.append(float(row[7])) 
            Jpsi_M_mc8.append(float(row[8]))
            KS0_M_mc8.append(float(row[9]))
            ROETracks_mc8.append(float(row[10]))      
            ROEECLClusters_mc8.append(float(row[11]))  
            GoodROEECLClusters_mc8.append(float(row[12]))
            ROEKLMClusters_mc8.append(float(row[13])) 
            B0_Sig_VtxPval_mc8.append(float(row[14])) 
            B0_Tag_VtxPval_mc8.append(float(row[15])) 
            B0_Sig_VtxRes_mc8.append(float(row[16])) 
            B0_Tag_VtxRes_mc8.append(float(row[17]))   
            Jpsi_mu0_TrPval_mc8.append(float(row[18]))
            Jpsi_mu1_TrPval_mc8.append(float(row[19]))
            KS0_pi0_TrPval_mc8.append(float(row[20]))
            KS0_pi1_TrPval_mc8.append(float(row[21]))
            nPXD_KS0_pi0_mc8.append(float(row[22])) 
            nPXD_KS0_pi1_mc8.append(float(row[23]))
            nSVD_KS0_pi0_mc8.append(float(row[24])) 
            nSVD_KS0_pi1_mc8.append(float(row[25])) 
            KS0_VtxPval_mc8.append(float(row[26]))  
            DeltaTRes_mc8.append(float(row[27]))
            nCDC_Jpsi_mu0_mc8.append(float(row[28]))  
            nCDC_Jpsi_mu1_mc8.append(float(row[29]))  
            nCDC_KS0_pi0_mc8.append(float(row[30])) 
            nCDC_KS0_pi1_mc8.append(float(row[31])) 
print("input mc8 data read")


'''


d_inner_mc8 = {'mu0 PXD': nPXD_Jpsi_mu0_mc8,'mu1 PXD': nPXD_Jpsi_mu1_mc8, 'mu0 SVD': nSVD_Jpsi_mu0_mc8,'mu1 SVD': nSVD_Jpsi_mu1_mc8}
d_vtx_mc8 = {'Sig VtxPval': B0_Sig_VtxPval_mc8,'Tag VtxPval': B0_Tag_VtxPval_mc8,'Sig Vtx Z Res': B0_Sig_VtxRes_mc8,'Tag Vtx Z Res': B0_Tag_VtxRes_mc8}
d_kin_mc8 = {'$M_{bc}$ $[GeV/c^2]$': B0_mbc_mc8,'$\Delta E$ $[GeV]$': B0_deltae_mc8,'$M_{J/\psi}$ $[GeV/c^2]$': Jpsi_M_mc8,'$M_{K^0_S}$ $[GeV/c^2]$': KS0_M_mc8}
d_ROE_mc8 = {' ROETracks ' :  ROETracks_mc8, 'ROEECL cl': ROEECLClusters_mc8,'Good ROEECL cl' : GoodROEECLClusters_mc8, 'ROEKLM cl' : ROEKLMClusters_mc8}

df_inner_mc8 = pd.DataFrame(data=d_inner_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_inner_mc8, alpha=0.2, figsize=(6, 6))#, diagonal='kde')
df_vtx_mc8 = pd.DataFrame(data=d_vtx_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_vtx_mc8, alpha=0.2, figsize=(6, 6))#, diagonal='kde')
df_kin_mc8 = pd.DataFrame(data=d_kin_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_kin_mc8, alpha=0.2, figsize=(6, 6), diagonal='kde')
df_ROE_mc8 = pd.DataFrame(data=d_ROE_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_ROE_mc8, alpha=0.2, figsize=(6, 6))#, diagonal='kde')


d_inner_mc9 = {'pi0 PXD': nPXD_Jpsi_mu0_mc9,'pi1 PXD': nPXD_Jpsi_mu1_mc9, 'pi0 SVD': nSVD_Jpsi_mu0_mc9,'pi1 SVD': nSVD_Jpsi_mu1_mc9}
d_vtx_mc9 = {'Sig VtxPval': B0_Sig_VtxPval_mc9,'Tag VtxPval': B0_Tag_VtxPval_mc9,'Sig Vtx Z Res': B0_Sig_VtxRes_mc9,'Tag Vtx Z Res': B0_Tag_VtxRes_mc9}
d_kin_mc9 = {'$M_{bc}$ $[GeV/c^2]$': B0_mbc_mc9,'$\Delta E$ $[GeV]$': B0_deltae_mc9,'$M_{J/\psi}$ $[GeV/c^2]$': Jpsi_M_mc9,'$M_{K^0_S}$ $[GeV/c^2]$': KS0_M_mc9}
d_ROE_mc9 = {' ROETracks ' :  ROETracks_mc9, 'ROEECL cl': ROEECLClusters_mc9,'Good ROEECL cl' : GoodROEECLClusters_mc9, 'ROEKLM cl' : ROEKLMClusters_mc9}

df_inner_mc9 = pd.DataFrame(data=d_inner_mc9)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_inner_mc9, alpha=0.2, figsize=(6, 6))#, diagonal='kde')
df_vtx_mc9 = pd.DataFrame(data=d_vtx_mc9)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_vtx_mc9, alpha=0.2, figsize=(6, 6))#, diagonal='kde')
df_kin_mc9 = pd.DataFrame(data=d_kin_mc9)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_kin_mc9, alpha=0.2, figsize=(6, 6), diagonal='kde')
df_ROE_mc9 = pd.DataFrame(data=d_ROE_mc9)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_ROE_mc9, alpha=0.2, figsize=(6, 6))#, diagonal='kde')

'''


set_y_axis = False
fig_kin, axs_kin = plt.subplots(2, 2, figsize=(10, 5))
axs_kin[0, 0].hist(B0_mbc_mc8,200,range=[5.24,5.29], normed=True,alpha=0.7)
axs_kin[0, 0].hist(B0_mbc_mc9,200,range=[5.24,5.29], normed=True,alpha=0.7)
axs_kin[0, 0].set_xlabel('$M_{bc}$ [GeV/$c^2$]')
axs_kin[0, 0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[0, 0].set_yscale('log')

axs_kin[0, 1].hist(B0_deltae_mc8,200,range=[-0.25,0.25], normed=True,alpha=0.7)
axs_kin[0, 1].hist(B0_deltae_mc9,200,range=[-0.25,0.25], normed=True,alpha=0.7)
#axs_kin[0, 1].set_title('$\Delta E$')
axs_kin[0, 1].set_xlabel('$\Delta E$ [GeV]')
axs_kin[0, 1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[0, 1].set_yscale('log')

axs_kin[1, 0].hist(Jpsi_M_mc8,200,range=[2.9,3.25], normed=True,alpha=0.7)
axs_kin[1, 0].hist(Jpsi_M_mc9,200,range=[2.9,3.25], normed=True,alpha=0.7)
#axs_kin[1, 0].set_title('$M_{B}$')
axs_kin[1, 0].set_xlabel('$M_{J/\psi}$ [GeV/$c^2$]')
axs_kin[1, 0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[1, 0].set_yscale('log')

axs_kin[1, 1].hist(KS0_M_mc8,200,range=[0.46,0.54], normed=True,alpha=0.7)
axs_kin[1, 1].hist(KS0_M_mc9,200,range=[0.46,0.54], normed=True,alpha=0.7)
axs_kin[1, 1].set_xlabel('$M_{K_S^0}$ [GeV/$c^2$]')
axs_kin[1, 1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[1, 1].set_yscale('log')

labels= ["mc8","mc9"]
fig_kin.subplots_adjust(hspace=0.26,left=0.08,right=0.98,top=0.98,bottom=0.08)
plt.legend(labels)




fig_vtx, axs_vtx = plt.subplots(2, 3, figsize=(10, 5))
#---------------------------------------
axs_vtx[0, 0].hist(B0_Sig_VtxPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 0].hist(B0_Sig_VtxPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 0].set_xlabel('Sig $B$ Vtx $P_{val}$')
axs_vtx[0, 0].set_ylabel('A.U.')
axs_vtx[0, 0].set_yscale('log')
#---------------------------------------
axs_vtx[0, 1].hist(B0_Tag_VtxPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 1].hist(B0_Tag_VtxPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 1].set_xlabel('Tag $B$ Vtx $P_{val}$')
axs_vtx[0, 1].set_ylabel('A.U.')
axs_vtx[0, 1].set_yscale('log')
#---------------------------------------
axs_vtx[0, 2].hist(KS0_VtxPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 2].hist(KS0_VtxPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 2].set_xlabel('$K_S^0$ Vtx $P_{val}$')
axs_vtx[0, 2].set_ylabel('A.U.')
axs_vtx[0, 2].set_yscale('log')
#---------------------------------------
axs_vtx[1, 0].hist(B0_Sig_VtxRes_mc8,200,range=[-0.03,0.03], normed=True,alpha=0.7)
axs_vtx[1, 0].hist(B0_Sig_VtxRes_mc9,200,range=[-0.03,0.03], normed=True,alpha=0.7)
axs_vtx[1, 0].set_xlabel('Sig $Z_{true}-Z_{reco}$')
axs_vtx[1, 0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_vtx[1, 0].set_yscale('log')
#---------------------------------------
axs_vtx[1, 1].hist(B0_Tag_VtxRes_mc8,200,range=[-0.05,0.05], normed=True,alpha=0.7)
axs_vtx[1, 1].hist(B0_Tag_VtxRes_mc9,200,range=[-0.05,0.05], normed=True,alpha=0.7)
axs_vtx[1, 1].set_xlabel('Tag $Z_{true}-Z_{reco}$')
axs_vtx[1, 1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_vtx[1, 1].set_yscale('log')
#---------------------------------------
axs_vtx[1, 2].hist(DeltaTRes_mc8,200,range=[-15,15], normed=True,alpha=0.7)
axs_vtx[1, 2].hist(DeltaTRes_mc9,200,range=[-15,15], normed=True,alpha=0.7)
axs_vtx[1, 2].set_xlabel('$\Delta T_{Reco}-\Delta T_{True}$')
axs_vtx[1, 2].set_ylabel('A.U.')
if (set_y_axis) :
    axs_vtx[1, 2].set_yscale('log')
#---------------------------------------
labels= ["mc8","mc9"]
fig_vtx.subplots_adjust(hspace=0.26,left=0.08,right=0.98,top=0.98,bottom=0.08)
plt.legend(labels)



fig_inner, axs_inner = plt.subplots(2, 4, figsize=(10, 5))
axs_inner[0, 0].hist(nPXD_Jpsi_mu0_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[0, 0].hist(nPXD_Jpsi_mu0_mc9,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[0, 0].set_xlabel('nPXD $\mu$0')
axs_inner[0, 0].set_ylabel('A.U.')

axs_inner[0, 1].hist(nSVD_Jpsi_mu0_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[0, 1].hist(nSVD_Jpsi_mu0_mc9,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[0, 1].set_xlabel('nSVD $\mu$0')
axs_inner[0, 1].set_ylabel('A.U.')

axs_inner[0, 2].hist(nCDC_Jpsi_mu0_mc8,80,range=[0,80], normed=True,alpha=0.7)
axs_inner[0, 2].hist(nCDC_Jpsi_mu0_mc9,80,range=[0,80], normed=True,alpha=0.7)
axs_inner[0, 2].set_xlabel('nCDC $\mu$0')
axs_inner[0, 2].set_ylabel('A.U.')

axs_inner[0, 3].hist(Jpsi_mu0_TrPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[0, 3].hist(Jpsi_mu0_TrPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[0, 3].set_xlabel('$\mu$0 TrPval')
axs_inner[0, 3].set_ylabel('A.U.')
axs_inner[0, 3].set_yscale('log')

axs_inner[1, 0].hist(nPXD_Jpsi_mu1_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[1, 0].hist(nPXD_Jpsi_mu1_mc9,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[1, 0].set_xlabel('nPXD $\mu$1')
axs_inner[1, 0].set_ylabel('A.U.')


axs_inner[1, 1].hist(nSVD_Jpsi_mu1_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[1, 1].hist(nSVD_Jpsi_mu1_mc9,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[1, 1].set_xlabel('nSVD $\mu$1')
axs_inner[1, 1].set_ylabel('A.U.')

axs_inner[1, 2].hist(nCDC_Jpsi_mu1_mc8,80,range=[0,80], normed=True,alpha=0.7)
axs_inner[1, 2].hist(nCDC_Jpsi_mu1_mc9,80,range=[0,80], normed=True,alpha=0.7)
axs_inner[1, 2].set_xlabel('nCDC $\mu$1')
axs_inner[1, 2].set_ylabel('A.U.')

axs_inner[1, 3].hist(Jpsi_mu1_TrPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[1, 3].hist(Jpsi_mu1_TrPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[1, 3].set_xlabel('$\mu$1 TrPval')
axs_inner[1, 3].set_ylabel('A.U.')
axs_inner[1, 3].set_yscale('log')

labels= ["mc8","mc9"]
fig_inner.subplots_adjust(hspace=0.26,left=0.08,right=0.98,top=0.98,bottom=0.08)
plt.legend(labels)



fig_inner_KS0, axs_inner_KS0 = plt.subplots(2, 4, figsize=(10, 5))
axs_inner_KS0[0, 0].hist(nPXD_KS0_pi0_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner_KS0[0, 0].hist(nPXD_KS0_pi0_mc9,5,range=[0,5], normed=True,alpha=0.7)
axs_inner_KS0[0, 0].set_xlabel('nPXD pi0')
axs_inner_KS0[0, 0].set_ylabel('A.U.')
axs_inner_KS0[0, 1].hist(nSVD_KS0_pi0_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner_KS0[0, 1].hist(nSVD_KS0_pi0_mc9,12,range=[0,12], normed=True,alpha=0.7)
axs_inner_KS0[0, 1].set_xlabel('nSVD pi0')
axs_inner_KS0[0, 1].set_ylabel('A.U.')
axs_inner_KS0[0, 2].hist(nCDC_KS0_pi0_mc8,80,range=[0,80], normed=True,alpha=0.7)
axs_inner_KS0[0, 2].hist(nCDC_KS0_pi0_mc9,80,range=[0,80], normed=True,alpha=0.7)
axs_inner_KS0[0, 2].set_xlabel('nCDC pi0')
axs_inner_KS0[0, 2].set_ylabel('A.U.')
axs_inner_KS0[0, 3].hist(KS0_pi0_TrPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_inner_KS0[0, 3].hist(KS0_pi0_TrPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_inner_KS0[0, 3].set_xlabel('pi0 TrPval')
axs_inner_KS0[0, 3].set_ylabel('A.U.')
axs_inner_KS0[0, 3].set_yscale('log')

axs_inner_KS0[1, 0].hist(nPXD_KS0_pi1_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner_KS0[1, 0].hist(nPXD_KS0_pi1_mc9,5,range=[0,5], normed=True,alpha=0.7)
axs_inner_KS0[1, 0].set_xlabel('nPXD pi1')
axs_inner_KS0[1, 0].set_ylabel('A.U.')
axs_inner_KS0[1, 1].hist(nSVD_KS0_pi1_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner_KS0[1, 1].hist(nSVD_KS0_pi1_mc9,12,range=[0,12], normed=True,alpha=0.7)
axs_inner_KS0[1, 1].set_xlabel('nSVD pi1')
axs_inner_KS0[1, 1].set_ylabel('A.U.')
axs_inner_KS0[1, 2].hist(nCDC_KS0_pi1_mc8,80,range=[0,80], normed=True,alpha=0.7)
axs_inner_KS0[1, 2].hist(nCDC_KS0_pi1_mc9,80,range=[0,80], normed=True,alpha=0.7)
axs_inner_KS0[1, 2].set_xlabel('nCDC pi1')
axs_inner_KS0[1, 2].set_ylabel('A.U.')
axs_inner_KS0[1, 3].hist(KS0_pi1_TrPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_inner_KS0[1, 3].hist(KS0_pi1_TrPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_inner_KS0[1, 3].set_xlabel('pi1 TrPval')
axs_inner_KS0[1, 3].set_ylabel('A.U.')
axs_inner_KS0[1, 3].set_yscale('log')

labels= ["mc8","mc9"]
fig_inner_KS0.subplots_adjust(hspace=0.26,left=0.08,right=0.98,top=0.98,bottom=0.08)
plt.legend(labels)




fig_ROE, axs_ROE = plt.subplots(2, 2, figsize=(10, 5))
axs_ROE[0, 0].hist(ROETracks_mc8,20,range=[0,20], normed=True,alpha=0.7)
axs_ROE[0, 0].hist(ROETracks_mc9,20,range=[0,20], normed=True,alpha=0.7)
#axs_ROE[0, 0].set_title('ROE Tracks')
axs_ROE[0, 0].set_xlabel('n ROE Tracks')
axs_ROE[0, 0].set_ylabel('A.U.')
axs_ROE[0, 1].hist(ROEECLClusters_mc8,150,range=[0,150], normed=True,alpha=0.7)
axs_ROE[0, 1].hist(ROEECLClusters_mc9,150,range=[0,150], normed=True,alpha=0.7)
#axs_ROE[0, 1].set_title('ROE Clusters ')
axs_ROE[0, 1].set_xlabel('n ROE Clusters')
axs_ROE[0, 1].set_ylabel('A.U.')
axs_ROE[1, 0].hist(GoodROEECLClusters_mc8,20,range=[0,20], normed=True,alpha=0.7)
axs_ROE[1, 0].hist(GoodROEECLClusters_mc9,20,range=[0,20], normed=True,alpha=0.7)
#axs_ROE[1, 0].set_title('ROE Good Quality')
axs_ROE[1, 0].set_xlabel('n ROE Good Quality ECL Clusters')
axs_ROE[1, 0].set_ylabel('A.U.')
axs_ROE[1, 1].hist(ROEKLMClusters_mc8,20,range=[0,20], normed=True,alpha=0.7)
axs_ROE[1, 1].hist(ROEKLMClusters_mc9,20,range=[0,20], normed=True,alpha=0.7)
#axs_ROE[1, 1].set_title('ROE EKL Clusters ')
axs_ROE[1, 1].set_xlabel(' n ROE EKL Clusters')
axs_ROE[1, 1].set_ylabel('A.U.')


labels= ["mc8","mc9"]
fig_ROE.subplots_adjust(hspace=0.26,left=0.08,right=0.98,top=0.98,bottom=0.08)
plt.legend(labels)





fig_2D_Tracking, axs_2D_Tracking = plt.subplots(2, 2, figsize=(10, 10))
axs_2D_Tracking[0,0].hist2d(nPXD_Jpsi_mu0_mc9, nSVD_Jpsi_mu0_mc9, range=([0,4],[0,12]), bins=(4,12), norm=LogNorm())
#axs_2D_Tracking[0,0].colorbar()
axs_2D_Tracking[0,1].hist2d(nPXD_KS0_pi0_mc9, nSVD_KS0_pi0_mc9, range=([0,4],[0,12]), bins=(4,12), norm=LogNorm())
#axs_2D_Tracking[0,1].colorbar()
axs_2D_Tracking[1,0].hist2d(nPXD_Jpsi_mu0_mc9, nCDC_Jpsi_mu0_mc9, range=([0,4],[0,150]), bins=(4,150), norm=LogNorm())
#axs_2D_Tracking[1,0].colorbar()
axs_2D_Tracking[1,1].hist2d(nPXD_KS0_pi0_mc9, nCDC_KS0_pi0_mc9, range=([0,4],[0,150]), bins=(4,150), norm=LogNorm())
#axs_2D_Tracking[1,1].colorbar()

plt.colorbar()
plt.show()
