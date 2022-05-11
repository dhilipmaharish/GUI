import pandas as pd
import os
import win32com.client
from win32com.client import Dispatch
import shutil
import time


engine_da = ''
emission_da = '' 


def engine_input():
    engine_data = pd.read_excel('Engine_Sample.xlsx')
    engine_model = engine_data.iloc[:, 2:].iloc[4].dropna().tolist()
    emission_model = engine_data.iloc[:, 2:].iloc[12].dropna().tolist()
    engine_emission_model = [str(engine_model[oo])+'_'+str(emission_model[oo])
                            for oo in range(0, len(engine_model))]
    enginespd_troque_power_data = engine_data.iloc[:, 2:].iloc[18:]
    # print(enginespd_troque_power_data)
    enginespd_troque_power_data.columns = [
        str(ss) for ss in range(0, len(enginespd_troque_power_data.columns))]

    enginespd_troque_power_data = enginespd_troque_power_data.loc[:, enginespd_troque_power_data.notna(
    ).any(axis=0)]
    enginespd_troque_power_data = enginespd_troque_power_data.loc[:, (
        enginespd_troque_power_data != 0).any(axis=0)]
    # print(enginespd_troque_power_data)
    start_ind = 0
    end_ind = 2
    name_ind = 0

    engine_dict = {}

    for ll in range(0, len(enginespd_troque_power_data.columns)):
        if ll == end_ind:
            engine_dict[str(engine_emission_model[name_ind])] = {'Engine speed': enginespd_troque_power_data[str(start_ind)].dropna().to_list(), 'Torque': enginespd_troque_power_data[str(end_ind-1)].dropna().to_list(), 'Power': enginespd_troque_power_data[str(end_ind)].dropna().to_list()
                                                                }
            start_ind = end_ind+1
            end_ind = end_ind+3
            name_ind += 1
    return engine_dict, engine_model, emission_model
