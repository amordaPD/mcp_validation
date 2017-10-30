
import itertools

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd 
from pandas.plotting import scatter_matrix
from sklearn import mixture

#####reading input data######

#####MC9#####
print("reading mc9 input data")
nPXD_pi0_mc9  = []
nPXD_pi1_mc9  = []
nSVD_pi0_mc9  = []
nSVD_pi1_mc9  = []
B0_Sig_VtxPval_mc9 = []
B0_Tag_VtxPval_mc9 = []
B0_Sig_VtxRes_mc9  = []
B0_Tag_VtxRes_mc9  = []
KS0_M_mc9     = []
Etap_M_mc9      = []
B0_mbc_mc9    = []
B0_deltae_mc9 = []
ROETracks_mc9          = []
ROEECLClusters_mc9     = []
GoodROEECLClusters_mc9 = []
ROEKLMClusters_mc9     = []
Eta_M_mc9     = []
etap_pi0_TrPval_mc9 = []
etap_pi1_TrPval_mc9 = []
K_S0_VtxPvalue_mc9 = []
B0_M_mc9 = []
DeltaTRes_mc9 = []

with open('mc9_1110048100.txt', 'r') as f_mc9:
    next(f_mc9)
    content = f_mc9.readlines()
    for x in content:
        row = x.split("*")
        nPXD_pi0_mc9.append(float(row[2]))
        nPXD_pi1_mc9.append(float(row[3]))
        nSVD_pi0_mc9.append(float(row[4]))
        nSVD_pi1_mc9.append(float(row[5]))    
        B0_mbc_mc9.append(float(row[6]))  
        B0_deltae_mc9.append(float(row[7])) 
        Etap_M_mc9.append(float(row[8]))
        KS0_M_mc9.append(float(row[9]))
        ROETracks_mc9.append(float(row[10]))      
        ROEECLClusters_mc9.append(float(row[11]))  
        GoodROEECLClusters_mc9.append(float(row[12]))
        ROEKLMClusters_mc9.append(float(row[13]))  
        B0_Sig_VtxPval_mc9.append(float(row[14])) 
        B0_Tag_VtxPval_mc9.append(float(row[15])) 
        B0_Sig_VtxRes_mc9.append(float(row[16])) 
        B0_Tag_VtxRes_mc9.append(float(row[17])) 
        Eta_M_mc9.append(float(row[18]))    
        etap_pi0_TrPval_mc9.append(float(row[19])) 
        etap_pi1_TrPval_mc9.append(float(row[20])) 
        K_S0_VtxPvalue_mc9.append(float(row[21]))
        B0_M_mc9.append(float(row[22])) 
        DeltaTRes_mc9.append(float(row[23]))
print("input mc9 data read")

#####MC8#####
print("reading mc8 input data")
nPXD_pi0_mc8  = []
nPXD_pi1_mc8  = []
nSVD_pi0_mc8  = []
nSVD_pi1_mc8  = []
B0_Sig_VtxPval_mc8 = []
B0_Tag_VtxPval_mc8 = []
B0_Sig_VtxRes_mc8  = []
B0_Tag_VtxRes_mc8  = []
KS0_M_mc8     = []
Etap_M_mc8      = []
B0_mbc_mc8    = []
B0_deltae_mc8 = []
ROETracks_mc8          = []
ROEECLClusters_mc8     = []
GoodROEECLClusters_mc8 = []
ROEKLMClusters_mc8     = []
Eta_M_mc8     = []
etap_pi0_TrPval_mc8 = []
etap_pi1_TrPval_mc8 = []
K_S0_VtxPvalue_mc8 = []
B0_M_mc8 = []
DeltaTRes_mc8 = []


with open('mc8_1110048100.txt', 'r') as f_mc8:
    next(f_mc8)
    content = f_mc8.readlines()
    for x in content:
        row = x.split("*")
        nPXD_pi0_mc8.append(float(row[2]))
        nPXD_pi1_mc8.append(float(row[3]))
        nSVD_pi0_mc8.append(float(row[4]))
        nSVD_pi1_mc8.append(float(row[5]))    
        B0_mbc_mc8.append(float(row[6]))  
        B0_deltae_mc8.append(float(row[7])) 
        Etap_M_mc8.append(float(row[8]))
        KS0_M_mc8.append(float(row[9]))
        ROETracks_mc8.append(float(row[10]))      
        ROEECLClusters_mc8.append(float(row[11]))  
        GoodROEECLClusters_mc8.append(float(row[12]))
        ROEKLMClusters_mc8.append(float(row[13])) 
        B0_Sig_VtxPval_mc8.append(float(row[14])) 
        B0_Tag_VtxPval_mc8.append(float(row[15])) 
        B0_Sig_VtxRes_mc8.append(float(row[16])) 
        B0_Tag_VtxRes_mc8.append(float(row[17]))   
        Eta_M_mc8.append(float(row[18]))    
        etap_pi0_TrPval_mc8.append(float(row[19])) 
        etap_pi1_TrPval_mc8.append(float(row[20])) 
        K_S0_VtxPvalue_mc8.append(float(row[21]))
        B0_M_mc8.append(float(row[22])) 
        DeltaTRes_mc8.append(float(row[23])) 
print("input mc8 data read")


'''


d_inner_mc8 = {'pi0 PXD': nPXD_pi0_mc8,'pi1 PXD': nPXD_pi1_mc8, 'pi0 SVD': nSVD_pi0_mc8,'pi1 SVD': nSVD_pi1_mc8}
d_vtx_mc8 = {'Sig VtxPval': B0_Sig_VtxPval_mc8,'Tag VtxPval': B0_Tag_VtxPval_mc8,'Sig Vtx Z Res': B0_Sig_VtxRes_mc8,'Tag Vtx Z Res': B0_Tag_VtxRes_mc8}
d_kin_mc8 = {'B mbc': B0_mbc_mc8,'B deltae': B0_deltae_mc8,'B M': Etap_M_mc8,'KS0 M': KS0_M_mc8}
d_ROE_mc8 = {' ROETracks ' :  ROETracks_mc8, 'ROEECL cl': ROEECLClusters_mc8,'Good ROEECL cl' : GoodROEECLClusters_mc8, 'ROEKLM cl' : ROEKLMClusters_mc8}

df_inner_mc8 = pd.DataFrame(data=d_inner_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_inner_mc8, alpha=0.2, figsize=(6, 6))#, diagonal='kde')
df_vtx_mc8 = pd.DataFrame(data=d_vtx_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_vtx_mc8, alpha=0.2, figsize=(6, 6))#, diagonal='kde')
df_kin_mc8 = pd.DataFrame(data=d_kin_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_kin_mc8, alpha=0.2, figsize=(6, 6), diagonal='kde')
df_ROE_mc8 = pd.DataFrame(data=d_ROE_mc8)#, columns=['pi0 PXD', 'pi1 PXD', 'pi0 SVD', 'pi1 SVD'])
scatter_matrix(df_ROE_mc8, alpha=0.2, figsize=(6, 6))#, diagonal='kde')


d_inner_mc9 = {'pi0 PXD': nPXD_pi0_mc9,'pi1 PXD': nPXD_pi1_mc9, 'pi0 SVD': nSVD_pi0_mc9,'pi1 SVD': nSVD_pi1_mc9}
d_vtx_mc9 = {'Sig VtxPval': B0_Sig_VtxPval_mc9,'Tag VtxPval': B0_Tag_VtxPval_mc9,'Sig Vtx Z Res': B0_Sig_VtxRes_mc9,'Tag Vtx Z Res': B0_Tag_VtxRes_mc9}
d_kin_mc9 = {'B mbc': B0_mbc_mc9,'B deltae': B0_deltae_mc9,'eta\' M': Etap_M_mc9,'KS0 M': KS0_M_mc9}
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
fig_kin, axs_kin = plt.subplots(2, 3, figsize=(5, 5))
axs_kin[0, 0].hist(B0_mbc_mc8,200,range=[5.25,5.29], normed=True,alpha=0.7)
axs_kin[0, 0].hist(B0_mbc_mc9,200,range=[5.25,5.29], normed=True,alpha=0.7)
axs_kin[0, 0].set_xlabel('$M_{bc}$ [GeV/$c^2$]')
axs_kin[0, 0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[0, 0].set_yscale('log')

axs_kin[0, 1].hist(B0_deltae_mc8,200,range=[-0.8,0.4], normed=True,alpha=0.7)
axs_kin[0, 1].hist(B0_deltae_mc9,200,range=[-0.8,0.4], normed=True,alpha=0.7)
axs_kin[0, 1].set_xlabel('$\Delta E$ [GeV]')
axs_kin[0, 1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[0, 1].set_yscale('log')

axs_kin[0, 2].hist(B0_M_mc8,200,range=[4.5,5.7], normed=True,alpha=0.7)
axs_kin[0, 2].hist(B0_M_mc9,200,range=[4.5,5.7], normed=True,alpha=0.7)
axs_kin[0, 2].set_xlabel('$M_{B^0}$ [GeV/$c^2$]')
axs_kin[0, 2].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[0, 2].set_yscale('log')

axs_kin[1, 0].hist(Etap_M_mc8,200,range=[0.75,1.18], normed=True,alpha=0.7)
axs_kin[1, 0].hist(Etap_M_mc9,200,range=[0.75,1.18], normed=True,alpha=0.7)
axs_kin[1, 0].set_xlabel('$M_{\eta^\prime}$ [GeV/$c^2$]')
axs_kin[1, 0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[1, 0].set_yscale('log')

axs_kin[1, 1].hist(Eta_M_mc8,200,range=[0.4,0.7], normed=True,alpha=0.7)
axs_kin[1, 1].hist(Eta_M_mc9,200,range=[0.4,0.7], normed=True,alpha=0.7)
axs_kin[1, 1].set_xlabel('$M_{\eta^\prime}$ [GeV/$c^2$]')
axs_kin[1, 1].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[1, 1].set_yscale('log')
    
axs_kin[1, 2].hist(KS0_M_mc8,200,range=[0.46,0.53], normed=True,alpha=0.7)
axs_kin[1, 2].hist(KS0_M_mc9,200,range=[0.46,0.53], normed=True,alpha=0.7)
axs_kin[1, 2].set_xlabel('$M_{K_S^0}$ [GeV/$c^2$]')
axs_kin[1, 2].set_ylabel('A.U.')
if (set_y_axis) :
    axs_kin[1, 2].set_yscale('log')



labels= ["mc8","mc9"]
plt.legend(labels)




fig_vtx, axs_vtx = plt.subplots(2, 3, figsize=(5, 5))
#---------------------------------------
axs_vtx[0, 0].hist(B0_Sig_VtxPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 0].hist(B0_Sig_VtxPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 0].set_xlabel('Sig Vtx $P_{val}$')
axs_vtx[0, 0].set_ylabel('A.U.')
axs_vtx[0, 0].set_yscale('log')
#---------------------------------------
axs_vtx[0, 1].hist(B0_Tag_VtxPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 1].hist(B0_Tag_VtxPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 1].set_xlabel('Tag Vtx $P_{val}$')
axs_vtx[0, 1].set_ylabel('A.U.')
axs_vtx[0, 1].set_yscale('log')
#---------------------------------------
axs_vtx[0, 2].hist(K_S0_VtxPvalue_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 2].hist(K_S0_VtxPvalue_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_vtx[0, 2].set_xlabel('$K^0_S$ Vtx $P_{val}$')
axs_vtx[0, 2].set_ylabel('A.U.')
axs_vtx[0, 2].set_yscale('log')
#---------------------------------------
axs_vtx[1, 0].hist(B0_Sig_VtxRes_mc8,200,range=[-0.1,0.1], normed=True,alpha=0.7)
axs_vtx[1, 0].hist(B0_Sig_VtxRes_mc9,200,range=[-0.1,0.1], normed=True,alpha=0.7)
axs_vtx[1, 0].set_xlabel('Sig $Z_{true}-Z_{reco}$')
axs_vtx[1, 0].set_ylabel('A.U.')
if (set_y_axis) :
    axs_vtx[1, 0].set_yscale('log')
#---------------------------------------
axs_vtx[1, 1].hist(B0_Tag_VtxRes_mc8,200,range=[-0.1,0.1], normed=True,alpha=0.7)
axs_vtx[1, 1].hist(B0_Tag_VtxRes_mc9,200,range=[-0.1,0.1], normed=True,alpha=0.7)
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
plt.legend(labels)



fig_inner, axs_inner = plt.subplots(2, 3, figsize=(5, 5))
axs_inner[0, 0].hist(nPXD_pi0_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[0, 0].hist(nPXD_pi0_mc9,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[0, 0].set_xlabel('nPXD pi0')
axs_inner[0, 0].set_ylabel('A.U.')

axs_inner[0, 1].hist(nSVD_pi0_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[0, 1].hist(nSVD_pi0_mc9,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[0, 1].set_xlabel('nSVD pi0')
axs_inner[0, 1].set_ylabel('A.U.')

axs_inner[0, 2].hist(etap_pi0_TrPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[0, 2].hist(etap_pi0_TrPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[0, 2].set_xlabel('pi0 Track PVal')
axs_inner[0, 2].set_ylabel('A.U.')
axs_inner[0, 2].set_yscale('log')

axs_inner[1, 0].hist(nPXD_pi1_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[1, 0].hist(nPXD_pi1_mc9,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[1, 0].set_xlabel('nPXD pi1')
axs_inner[1, 0].set_ylabel('A.U.')

axs_inner[1, 1].hist(nSVD_pi1_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[1, 1].hist(nSVD_pi1_mc9,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[1, 1].set_xlabel('nSVD pi1')
axs_inner[1, 1].set_ylabel('A.U.')


axs_inner[1, 2].hist(etap_pi1_TrPval_mc8,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[1, 2].hist(etap_pi1_TrPval_mc9,200,range=[0,1], normed=True,alpha=0.7)
axs_inner[1, 2].set_xlabel('pi1 Track PVal')
axs_inner[1, 2].set_ylabel('A.U.')
axs_inner[1, 2].set_yscale('log')

etap_pi0_TrPval_mc8

labels= ["mc8","mc9"]
plt.legend(labels)

fig_ROE, axs_ROE = plt.subplots(2, 2, figsize=(5, 5))
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
plt.legend(labels)

plt.show()

'''
fig_inner_sc_8, axs_inner_sc_8 = plt.subplots(4, 4, figsize=(5, 5))
axs_inner_sc_8[0, 0].hist(nPXD_pi0_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner_sc_8[0, 0].hist(nPXD_pi0_mc9,5,range=[0,5], normed=True,alpha=0.7)
#axs_inner[0, 0].set_title('nPXD pi0')
axs_inner[0, 0].set_xlabel('nPXD pi0')
axs_inner[0, 0].set_ylabel('A.U.')
axs_inner[0, 1].hist(nPXD_pi1_mc8,5,range=[0,5], normed=True,alpha=0.7)
axs_inner[0, 1].hist(nPXD_pi1_mc9,5,range=[0,5], normed=True,alpha=0.7)
#axs_inner[0, 1].set_title('nPXD pi1')
axs_inner[0, 1].set_xlabel('nPXD pi1')
axs_inner[0, 1].set_ylabel('A.U.')
axs_inner[1, 0].hist(nSVD_pi0_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[1, 0].hist(nSVD_pi0_mc9,12,range=[0,12], normed=True,alpha=0.7)
#axs_inner[1, 0].set_title('nSVD pi0')
axs_inner[1, 0].set_xlabel('nSVD pi0')
axs_inner[1, 0].set_ylabel('A.U.')
axs_inner[1, 1].hist(nSVD_pi1_mc8,12,range=[0,12], normed=True,alpha=0.7)
axs_inner[1, 1].hist(nSVD_pi1_mc9,12,range=[0,12], normed=True,alpha=0.7)
#axs_inner[1, 1].set_title('nSVD pi1')
axs_inner[1, 1].set_xlabel('nSVD pi1')
axs_inner[1, 1].set_ylabel('A.U.')

labels= ["mc8","mc9"]
plt.legend(labels)
'''
