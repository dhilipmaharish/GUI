import pandas as pd


def air_resistance(user_file = None):
    
    if user_file:
        air_data = pd.read_excel(user_file)
    else:
        air_data = pd.read_excel('data/Air_drag_sample.xlsx')
        # print(air_data)
    category_type = {}
    from_category_show_cab_option = {}
    from_cab_show_rear_option = {}
    from_rear_show_air_resistance_option = {}
    vehicle_category = air_data.iloc[:, 1:].iloc[4].dropna().to_list()
    cab = air_data.iloc[:,1:].iloc[6].dropna().to_list()
    rear_body = air_data.iloc[:,1:].iloc[8].dropna().to_list()
    air_resistance = air_data.iloc[:, 1:].iloc[10].dropna().to_list()
    
    for ele in range(0, len(vehicle_category)):
        
        if vehicle_category[ele] in category_type:
            category_type[vehicle_category[ele]].append(str(vehicle_category[ele]))
        else:
            category_type[vehicle_category[ele]] = [(str(vehicle_category[ele]))]
        # Cab filter
        if vehicle_category[ele] in from_category_show_cab_option:
            from_category_show_cab_option[vehicle_category[ele]].append(str(cab[ele]))
        else:
            from_category_show_cab_option[vehicle_category[ele]] = [(str(cab[ele]))]
            
        #Rear_body_filter
        if (vehicle_category[ele]+" "+cab[ele]) in from_cab_show_rear_option:
            from_cab_show_rear_option[vehicle_category[ele]+" "+cab[ele]].append(str(rear_body[ele]))
        else:
            from_cab_show_rear_option[vehicle_category[ele]+" "+cab[ele]] = [(str(rear_body[ele]))]
            
        # Air Resistance
        if (vehicle_category[ele]+" "+cab[ele]+" "+rear_body[ele]) in from_rear_show_air_resistance_option:
            from_rear_show_air_resistance_option[vehicle_category[ele]+" "+cab[ele]+" "+rear_body[ele]].append(str(air_resistance[ele]))
        else:
            from_rear_show_air_resistance_option[vehicle_category[ele]+" "+cab[ele]+" "+rear_body[ele]] = [(str(air_resistance[ele]))]
    def unique_element(filter):
        dict = {key:list(set(value)) for key,value in filter.items()}
        return dict  
          
    from_category_show_cab_option = unique_element(from_category_show_cab_option)
    from_cab_show_rear_option = unique_element(from_cab_show_rear_option)
    from_rear_show_air_resistance_option = unique_element(from_rear_show_air_resistance_option)
    print("air_resstaince", from_rear_show_air_resistance_option)
    return list(set(category_type)), from_category_show_cab_option, from_cab_show_rear_option, from_rear_show_air_resistance_option