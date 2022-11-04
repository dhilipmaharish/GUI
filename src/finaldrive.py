import pandas as pd
import os
import win32com.client
from win32com.client import Dispatch
import shutil
import time


def final_drive_input():
    f_drive_data = pd.read_excel('data/Final_Drive_Sample.xlsx')
    from_type = {}
    from_type_select_axel_option_show = {}
    from_axel_select_gear_ratio_option_show = {}
    from_gear_ratio_select_efficiency_option_show = {}
    type_f = f_drive_data.iloc[:, 1:].iloc[5].dropna().to_list()
    type_f = [str(gg).replace('\n', ' ') for gg in type_f]
    axel_layout = f_drive_data.iloc[:, 1:].iloc[6].dropna().to_list()
    gear_ratio_f = f_drive_data.iloc[:, 1:].iloc[7].dropna().to_list()
    efficiency_f = f_drive_data.iloc[:, 1:].iloc[9].dropna().to_list()


    # from_axel_select_gear_ratio_option_show={}
    # for jj in range(0, len(type_f)):
    
    for type, layout in zip(type_f, axel_layout):
        if type in from_type:
            from_type[type].append(layout)
        else:
            from_type[type] = [layout]
            
        
    from_type = {key : list(set(value)) for key, value in from_type.items()} 
    for jj in range(0, len(type_f)):
        if str(type_f[jj])+' '+str(axel_layout[jj]) in from_axel_select_gear_ratio_option_show.keys():
            from_axel_select_gear_ratio_option_show[str(
                type_f[jj])+' '+str(axel_layout[jj])].append(str(gear_ratio_f[jj]))
        else:
            from_axel_select_gear_ratio_option_show[str(
                type_f[jj])+' '+str(axel_layout[jj])] = [str(gear_ratio_f[jj])]
    
    for jj in range(0, len(type_f)):
        if str(type_f[jj])+' '+str(axel_layout[jj])+' '+str(gear_ratio_f[jj]) in from_gear_ratio_select_efficiency_option_show.keys():
            from_gear_ratio_select_efficiency_option_show[str(
                type_f[jj])+' '+str(axel_layout[jj])+' '+str(gear_ratio_f[jj])].append(str(efficiency_f[jj]))
        else:
            from_gear_ratio_select_efficiency_option_show[str(
                type_f[jj])+' '+str(axel_layout[jj])+' '+str(gear_ratio_f[jj])] = [str(efficiency_f[jj])]
    main_list = [type_f, axel_layout]  # ,gear_ratio_f,efficiency_f]
    # ,from_axel_select_gear_ratio_option_show,from_gear_ratio_select_efficiency_option_show]
    dict_list = [from_type_select_axel_option_show]
    
    for ll in range(0, len(main_list)):
        if ll != 1:
            for kk in range(0, len(main_list[ll])):
                if str(main_list[ll][kk]) in dict_list[ll].keys():
                    dict_list[ll][str(main_list[ll][kk])].append(
                        str(main_list[ll+1][kk]))
                else:
                    dict_list[ll][str(main_list[ll][kk])] = [
                        str(main_list[ll+1][kk])]
    return list(set(type_f)), from_type, from_axel_select_gear_ratio_option_show, from_gear_ratio_select_efficiency_option_show

final_drive_input()