import pandas as pd


def air_resistance_input():
    air_data = pd.read_excel('data/Air_drag_sample.xlsx')
    # print(air_data)
    air_resistance = air_data.iloc[:, 1:].iloc[10].dropna().to_list()
    return air_resistance

