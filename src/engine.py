import pandas as pd
import os
import win32com.client
from win32com.client import Dispatch
import shutil
import time

def engine_input(user_file = None):
    
    if user_file:
        engine_data = pd.read_excel(user_file)
    else:
        engine_data = pd.read_excel('data/Engine_Sample.xlsx')
    engine_model = engine_data.iloc[:, 2:].iloc[4].dropna().tolist()
    emission_model = engine_data.iloc[:, 2:].iloc[13].dropna().tolist()
    power_torque_model = engine_data.iloc[:,2:].iloc[5].dropna().tolist()
    engine_emission_power_model = [str(engine_model[oo])+'_'+str(emission_model[oo])+'_'+str(power_torque_model[oo])
                            for oo in range(0, len(engine_model))]
    enginespd_troque_power_data = engine_data.iloc[:, 2:].iloc[19:]
    # print(enginespd_troque_power_data)
    enginespd_troque_power_data.columns = [
        str(ss) for ss in range(0, len(enginespd_troque_power_data.columns))]

    enginespd_troque_power_data = enginespd_troque_power_data.loc[:, enginespd_troque_power_data.notna(
    ).any(axis=0)]
    enginespd_troque_power_data = enginespd_troque_power_data.loc[:, (
        enginespd_troque_power_data != 0).any(axis=0)]
    start_ind = 0
    end_ind = 2
    name_ind = 0

    engine_dict = {}
    engine_filter_dict = {}
    power_torque_filter_dict = {}
    for ll in range(0, len(enginespd_troque_power_data.columns)):
        if ll == end_ind:
            engine_dict[str(engine_emission_power_model[name_ind])] = {'Engine speed': enginespd_troque_power_data[str(start_ind)].dropna().to_list(), 'Torque': enginespd_troque_power_data[str(end_ind-1)].dropna().to_list(), 'Power': enginespd_troque_power_data[str(end_ind)].dropna().to_list()
                                                                           }
            start_ind = end_ind+1
            end_ind = end_ind+3
            name_ind += 1     
    for engine, emission, power_torque in zip(engine_model, emission_model, power_torque_model):
        if emission in engine_filter_dict:
            engine_filter_dict[emission].append(engine)
        else:
            engine_filter_dict[emission] = [engine]
        if emission + ' ' + engine in power_torque_filter_dict:
            power_torque_filter_dict[emission + ' ' + engine].append(power_torque)
        else:
            power_torque_filter_dict[emission+' '+engine] = [power_torque]
    print(power_torque_filter_dict)
    def unique_element(filter):
        dict = {key:list(set(value)) for key,value in filter.items()}
        return dict
    
    engine_filter_dict = unique_element(engine_filter_dict) 
    power_torque_filter_dict = unique_element(power_torque_filter_dict)
    return engine_dict,list(set(emission_model)), engine_filter_dict, power_torque_filter_dict


#engine_dict,emission_model, engine_filter_dict = engine_input()
print(engine_input())

