import pandas as pd
import os
import win32com.client
from win32com.client import Dispatch
import shutil
import time

def transmission_input():
    start_ind = 0
    end_ind = 1
    name_ind = 0
    trans_dict = {}
    trans_data = pd.read_excel('Transmission_sample.xlsx')
    trans_model = trans_data.iloc[:, 1:].iloc[4].dropna().to_list()
    gear_ratio_effi_data = trans_data.iloc[:, 1:].iloc[9:]
    gear_ratio_effi_data.columns = [
        str(ss) for ss in range(0, len(gear_ratio_effi_data.columns))]
    gear_ratio_effi_data = gear_ratio_effi_data.loc[:,
                                                    gear_ratio_effi_data.notna().any(axis=0)]
    
    for ll in range(0, len(gear_ratio_effi_data.columns)):
        if ll == end_ind:
            # print(str(trans_model[name_ind]))
            trans_dict[str(trans_model[name_ind])] = {'Gear ratio': gear_ratio_effi_data[str(start_ind)].dropna(
            ).to_list(), 'Efficiency': gear_ratio_effi_data[str(end_ind)].dropna().to_list()}
            start_ind = end_ind+1
            end_ind = end_ind+2
            name_ind += 1
    return trans_dict, trans_model

transmission_input()

