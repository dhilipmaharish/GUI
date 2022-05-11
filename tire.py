import pandas as pd
import os
import win32com.client
from win32com.client import Dispatch
import shutil
import time


def tire_input():
    tire_data = pd.read_excel('Tire_Sample.xlsx')

    # print(tire_data)
    from_size_select_application_option_show = {}
    # from_application_select_dynamic_ratio_option_show={}
    from_dynamic_ratio_select_rrc_option_show = {}

    size_t = tire_data.iloc[:, 1:].iloc[4].dropna().to_list()

    # application_t=tire_data.iloc[:,1:].iloc[7].dropna().to_list()
    application_tire = ['double']
    partern = tire_data.iloc[:, 1:].iloc[5].dropna().to_list()
    standard = tire_data.iloc[:, 1:].iloc[6].dropna().to_list()
    dynamic_ratio_t = tire_data.iloc[:, 1:].iloc[8].dropna().to_list()
    rrc_t = tire_data.iloc[:, 1:].iloc[9].dropna().to_list()
    remark = tire_data.iloc[:, 1:].iloc[10].dropna().to_list()

    main_list_tire = [size_t, dynamic_ratio_t]  # ,rrc_t]
    # ,from_dynamic_ratio_select_rrc_option_show]
    dict_list_tire = [from_size_select_application_option_show]

    for ll in range(0, len(main_list_tire)):
        if ll != 1:
            for kk in range(0, len(main_list_tire[ll])):
                if str(main_list_tire[ll][kk]) in dict_list_tire[ll].keys():
                    dict_list_tire[ll][str(main_list_tire[ll][kk])].append(
                        str(main_list_tire[ll+1][kk]))
                else:
                    dict_list_tire[ll][str(main_list_tire[ll][kk])] = [
                        str(main_list_tire[ll+1][kk])]


    for jj in range(0, len(size_t)):
        if str(size_t[jj])+' '+str(dynamic_ratio_t[jj]) in from_dynamic_ratio_select_rrc_option_show.keys():
            # print(from_axel_select_gear_ratio_option_show)
            from_dynamic_ratio_select_rrc_option_show[str(
                size_t[jj])+' '+str(dynamic_ratio_t[jj])].append(str(rrc_t[jj]))
        else:
            from_dynamic_ratio_select_rrc_option_show[str(
                size_t[jj])+' '+str(dynamic_ratio_t[jj])] = [str(rrc_t[jj])]
    # print(from_dynamic_ratio_select_rrc_option_show)

    return set(size_t), dynamic_ratio_t, rrc_t

