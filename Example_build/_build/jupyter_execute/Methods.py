#!/usr/bin/env python
# coding: utf-8

# # Methods 
# - With the Help of Brooke Heaven National Labratory and with special thanks to Denis Leshchev, he's demonstrations have been extremly helpful in understanding how to perform fingerprinting analysis of CNPs. Block code from Denis Leshchev will be presented, following the extraction of the data, cleaning and normalization processes used. Then we will deviate and from Denis's MCR fitting method to perform our own fitting using Linear Combination.

# # Extraction and Averaging of Spots
# - Here Denis has averaged multiple xanes spectrums for the same sample taken at diffrent spots. He then goes on to extract the data and store the avergaed spectrums into a dictionary over an interval of energy where the XANES region is located. Note, Denis has even included a dataframe in the dictionary, specifiying if the spectrum is a Standard/Reference or a sample.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from os import listdir
from os.path import isfile, join

from larch import Group
from larch.io import read_ascii
from larch.xafs import pre_edge, autobk

from pymcr.mcr import McrAR
from pymcr.regressors import OLS, NNLS
from pymcr.constraints import (ConstraintNonneg, ConstraintNorm, ConstraintCompressBelow,
                               ConstraintCutBelow, ConstraintCutAbove, ConstraintCompressAbove)

ph1_working_dir = r'/users/kieranmacdonald/Documents/GitHub/ResearchModel/XANES_DataGenerating/DatFiles_Phase_One'
ph2_working_dir = r'/users/kieranmacdonald/Documents/GitHub/ResearchModel/XANES_DataGenerating/DatFiles_Phase_Two'
ph3_working_dir = r'/users/kieranmacdonald/Documents/GitHub/ResearchModel/XANES_DataGenerating/DatFiles_Phase_Three'

data_directory = "/Users/kieranmacdonald/Documents/GitHub/ResearchModel/data"

df = pd.read_excel(data_directory + "/" + 'toLuminda.xlsx',engine='openpyxl')

#%% Read, average, de-glitch the data for all phases

def average_mus(mypath, onlyfiles_dat, energy, idx_un, idx_all):
    mus_averaged = np.zeros((energy.size, idx_un.size))
    mus_t_averaged = np.zeros((energy.size, idx_un.size))
    mus_all = np.zeros((energy.size, idx_all.size))
    mus_all_t = np.zeros((energy.size, idx_all.size))
    kk = 0
    
    
    for jj, each_idx in enumerate(idx_un):
        selection = (each_idx == idx_all)
        select_files = onlyfiles_dat[selection]
        n_curves = select_files.size
        _mu = np.zeros(energy.size)
        _mu_t = np.zeros(energy.size)
#        norm = select_files.size
        for f in select_files:
            _d =  np.genfromtxt(mypath + '/' + f)
            if kk != 580: # remove crazy outolier
                this_mu = np.interp(energy, _d[:, 0], _d[:, 4] / _d[:, 1])
                this_mu_t = np.interp(energy, _d[:, 0], -np.log(_d[:, 2] / _d[:, 1]))
                _mu += this_mu
                _mu_t += this_mu_t
                mus_all[:, kk] = this_mu.copy()
                mus_all_t[:, kk] = this_mu_t.copy()
            
            kk += 1
       
        mus_averaged[:, jj] = _mu #/ n_curves
        mus_t_averaged[:, jj] = _mu_t / n_curves
        
    return mus_averaged, mus_t_averaged

def extract_data_dict_ph1(mypath):
    onlyfiles_dat = np.array([f for f in listdir(mypath) if isfile(join(mypath, f)) and 
                                               f.endswith('.dat')])
    onlyfiles_dat = onlyfiles_dat[1:-1]
    
    _d = np.genfromtxt(mypath + '/' + onlyfiles_dat[0])
    energy = _d[1:-1, 0]
#    
    keys = np.array([i[:5] for i in onlyfiles_dat])
    unique_keys = np.unique(keys)
    mus_averaged, mus_t_averaged = average_mus(mypath, onlyfiles_dat, energy, unique_keys, keys)
    
    isGood = mus_averaged[30, :] > 0.5
    #print(isGood)
    mus_averaged = mus_averaged[:, isGood]
    mus_t_averaged = mus_t_averaged[:, isGood]
    unique_keys = unique_keys[isGood]
    
    mask = energy<6000
    mus_averaged = mus_averaged[mask]
    mus_t_averaged = mus_t_averaged[mask]
    energy = energy[mask]
    
    isSample = []
    for i, un_key in enumerate(unique_keys):
        if un_key.startswith('Ce'):
            isSample.append(False)
        else:
            isSample.append(True)
    isSample = np.array(isSample)
    isRef = ~isSample
    
    
    df = pd.DataFrame({'sample_name' : unique_keys, 'isSample': isSample, 'isRef' : isRef})
    
    data_dict = {'energy' : energy - 0.6,
                 'data' : mus_averaged,
                 'data_t':mus_t_averaged,
                 'sample_table' : df }
    return data_dict


# # Normalization
# - 
