from src.transmission import transmission_input
from src.engine import engine_input
from src.finaldrive import final_drive_input
from src.tire import tire_input
from src.air_resistence import air_resistance_input
import json

trans_dict,trans_dict_len, trans_drop = transmission_input()
engine_dict, engine_drop, emission_drop, emission_filter_dict = engine_input()
axel_drop,axle_type, from_axel_select_gear_ratio_option_show, from_gear_ratio_select_efficiency_option_show = final_drive_input()
tyre_size_drop,application_drop, radius_drop, rrc_drop, tire_description_dict = tire_input()
air_drop = air_resistance_input()

# unique option on axle details
axle_type = {key:list(set(value)) for key,value in axle_type.items()}
from_axel_select_gear_ratio_option_show = {key:list(set(value)) for key,value in from_axel_select_gear_ratio_option_show.items()}
from_gear_ratio_select_efficiency_option_show = {key:list(set(value)) for key,value in from_gear_ratio_select_efficiency_option_show.items()}

# unique option on tyre details
application_drop = {key:list(set(value)) for key,value in application_drop.items()}
radius_drop = {key:list(set(value)) for key,value in radius_drop.items()}
rrc_drop = {key:list(set(value)) for key,value in rrc_drop.items()}

inputdata = {
    "engine_drop" : engine_drop,
    "trans_drop" : trans_drop,
    "axel_drop" : axel_drop,
    "axleObject" : axle_type,
    "axleRatioObject" : from_axel_select_gear_ratio_option_show,
    "axelefficiencyObject" : from_gear_ratio_select_efficiency_option_show,
    "tyre_size_drop" : tyre_size_drop,
    "applicationObject" : application_drop,
    "radiusObject" : radius_drop,
    "rrcObject" : rrc_drop,
    "air_drop" : air_drop,
    "trans_dict_len" : trans_dict_len,
    "tire_description_dict" : tire_description_dict,
    "emission_filter" : emission_filter_dict
    
}

table_data = {
    "row1": ['Max Velocity', 'km/h', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    "row2": ['@rpm', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    "row3": ['Climb ability', '%', '-', '-', '-', '-','-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    "row4" : ['@km/h', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 
'-', '-', '-', '-', '-']}
input_json = json.dumps(inputdata)

