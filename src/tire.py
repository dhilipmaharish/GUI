import pandas as pd
import os
import win32com.client
from win32com.client import Dispatch
import shutil
import time


def tire_input():
    tire_data = pd.read_excel('data/Tire_Sample.xlsx')

    # print(tire_data)
    tire_size = {}
    from_size_select_application_option_show = {}
    from_application_select_dynamic_ratio_option_show={}
    from_dynamic_ratio_select_rrc_option_show = {}

    size_t = tire_data.iloc[:, 1:].iloc[4].dropna().to_list()
    tire_description_dict = {}
    # application_t=tire_data.iloc[:,1:].iloc[7].dropna().to_list()
    pattern = tire_data.iloc[:, 1:].iloc[5].dropna().to_list()
    standard = tire_data.iloc[:, 1:].iloc[6].dropna().to_list()
    dynamic_radius = tire_data.iloc[:, 1:].iloc[8].dropna().to_list()
    application = tire_data.iloc[:, 1:].iloc[7].dropna().to_list()
    rrc_t = tire_data.iloc[:, 1:].iloc[9].dropna().to_list()
    remark = tire_data.iloc[:, 1:].iloc[10].dropna().to_list()
    # ,from_dynamic_ratio_select_rrc_option_show]
    dict_list_tire = [from_size_select_application_option_show]
    
    for ele in range(0, len(size_t)):
        # Application option Filter
        if size_t[ele] in from_size_select_application_option_show:
            from_size_select_application_option_show[size_t[ele]].append(application[ele])
        else:
            from_size_select_application_option_show[size_t[ele]] = [application[ele]]
        
        
        # Radius option filter
        if str(size_t[ele])+' '+str(application[ele]) in from_application_select_dynamic_ratio_option_show.keys():
            from_application_select_dynamic_ratio_option_show[str(size_t[ele])+' '+str(application[ele])].append(str(dynamic_radius[ele]))
        else:
            from_application_select_dynamic_ratio_option_show[str(size_t[ele])+' '+str(application[ele])] = [str(dynamic_radius[ele])]
        
        # RRC option filter
        if str(size_t[ele])+' '+str(application[ele])+' '+str(dynamic_radius[ele]) in from_dynamic_ratio_select_rrc_option_show.keys():
            from_dynamic_ratio_select_rrc_option_show[str(size_t[ele])+' '+str(application[ele])+' '+str(dynamic_radius[ele])].append(str(rrc_t[ele]))
        else:
            from_dynamic_ratio_select_rrc_option_show[str(size_t[ele])+' '+str(application[ele])+' '+str(dynamic_radius[ele])] = [str(rrc_t[ele])]
        
        # Pattern, standard and remark details
        tire_description_dict[size_t[ele]] = {"Pattern" : pattern[ele], "Standard" : standard[ele], "remark": remark[ele]} 
        
    return list(set(size_t)),from_size_select_application_option_show,from_application_select_dynamic_ratio_option_show,from_dynamic_ratio_select_rrc_option_show, tire_description_dict


size_t,from_size_select_application_option_show,from_application_select_dynamic_ratio_option_show,from_dynamic_ratio_select_rrc_option_show, tire_description_dict = tire_input()

