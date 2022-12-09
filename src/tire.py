import pandas as pd
import os
import win32com.client
from win32com.client import Dispatch
import shutil
import time


def tire_input(user_file = None):
    
    if user_file : 
        tire_data = pd.read_excel(user_file)
    else:
        tire_data = pd.read_excel('data/Tire_Sample.xlsx')

    # print(tire_data)
    tire_size = {}
    from_size_select_standard_option_show = {}
    from_standard_select_application_option_show = {}
    from_application_select_radius_option_show={}
    from_radius_option_select_rrc_option_show = {}

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
    
    for ele in range(0, len(size_t)):
        # Standard option Filter
        if size_t[ele] in from_size_select_standard_option_show:
            from_size_select_standard_option_show[size_t[ele]].append(str(standard[ele]))
        else:
            from_size_select_standard_option_show[size_t[ele]] = [str(standard[ele])]
        
        #Application option Filter
        if str(size_t[ele])+' '+str(standard[ele]) in  from_standard_select_application_option_show.keys():
            from_standard_select_application_option_show[str(size_t[ele])+' '+str(standard[ele])].append(str(application[ele]))
        else:
            from_standard_select_application_option_show[str(size_t[ele])+' '+str(standard[ele])] = [str(application[ele])]
        
        # Radius option filter
        if str(size_t[ele])+' '+str(standard[ele])+' '+str(application[ele]) in from_application_select_radius_option_show.keys():
            from_application_select_radius_option_show[str(size_t[ele])+' '+str(standard[ele])+' '+str(application[ele])].append(str(dynamic_radius[ele]))
        else:
            from_application_select_radius_option_show[str(size_t[ele])+' '+str(standard[ele])+' '+str(application[ele])] = [str(dynamic_radius[ele])]
        
        # RRC option filter
        if str(size_t[ele])+' '+str(standard[ele])+' '+str(application[ele])+' '+str(dynamic_radius[ele]) in from_radius_option_select_rrc_option_show.keys():
            from_radius_option_select_rrc_option_show[str(size_t[ele])+' '+str(standard[ele])+' '+str(application[ele])+' '+str(dynamic_radius[ele])].append(str(rrc_t[ele]))
        else:
            from_radius_option_select_rrc_option_show[str(size_t[ele])+' '+str(standard[ele])+' '+str(application[ele])+' '+str(dynamic_radius[ele])] = [str(rrc_t[ele])]
        
        # Pattern, standard and remark details
        tire_description_dict[size_t[ele]] = {"Pattern" : pattern[ele], "Standard" : standard[ele], "remark": remark[ele]} 
        def unique_element(filter):
            dict = {key:list(set(value)) for key,value in filter.items()}
            return dict  
        from_size_select_standard_option_show = unique_element(from_size_select_standard_option_show)
        from_standard_select_application_option_show = unique_element(from_standard_select_application_option_show)
        from_application_select_radius_option_show = unique_element(from_application_select_radius_option_show)
        from_radius_option_select_rrc_option_show = unique_element(from_radius_option_select_rrc_option_show)
    return list(set(size_t)),from_size_select_standard_option_show,from_standard_select_application_option_show,from_application_select_radius_option_show,from_radius_option_select_rrc_option_show,tire_description_dict




