from src.transmission import transmission_input
from src.engine import engine_input
from src.finaldrive import final_drive_input
from src.tire import tire_input
from src.air_resistence import air_resistance
import json

trans_dict,trans_dict_len, trans_drop = transmission_input()
engine_dict, emission_drop, engine_filter_dict = engine_input()
axel_drop,axle_type, from_axel_select_gear_ratio_option_show, from_gear_ratio_select_efficiency_option_show = final_drive_input()
tyre_size_drop,standard_drop,application_drop, radius_drop, rrc_drop, tire_description_dict = tire_input()
vehicle_category_drop, cab_drop, rear_body_drop, air_resistance_drop = air_resistance()



# unique option on axle details
axle_type = {key:list(set(value)) for key,value in axle_type.items()}
from_axel_select_gear_ratio_option_show = {key:list(set(value)) for key,value in from_axel_select_gear_ratio_option_show.items()}
from_gear_ratio_select_efficiency_option_show = {key:list(set(value)) for key,value in from_gear_ratio_select_efficiency_option_show.items()}

# unique option on tyre details
standard_drop = {key:list(set(value)) for key, value in standard_drop.items()}
application_drop = {key:list(set(value)) for key,value in application_drop.items()}
radius_drop = {key:list(set(value)) for key,value in radius_drop.items()}
rrc_drop = {key:list(set(value)) for key,value in rrc_drop.items()}

# unique option on air resistance details
cab_drop = {key:list(set(value)) for key, value in cab_drop.items()}
rear_body_drop = {key:list(set(value)) for key, value in rear_body_drop.items()}
air_resistance_drop = {key:list(set(value)) for key, value in air_resistance_drop.items()}

inputdata = {
    "emission_object" : emission_drop,
    "engine_object" : engine_filter_dict,
    "transsmission_object" : trans_drop,
    "no_gears_object" : trans_dict_len, 
    "final_drive_object" : axel_drop,
    "layout_object" : axle_type,
    "ratio_object" : from_axel_select_gear_ratio_option_show,
    "efficiency_object" : from_gear_ratio_select_efficiency_option_show,
    "tyre_size_object" : tyre_size_drop,
    "standard_object" : standard_drop,
    "application_object" : application_drop,
    "radius_object" : radius_drop,
    "rrc_object" : rrc_drop,
    "tire_description_dict_object" : tire_description_dict,
    "category_object" : vehicle_category_drop,
    "cab_object" : cab_drop,
    "rear_body_object" : rear_body_drop,
    "air_resistance_object" : air_resistance_drop   
}


driving_resistance_cell = {'driving_resistance1':9,'driving_resistance2':10,'driving_resistance3':11,'driving_resistance4':12,
                            'driving_resistance5':13,'driving_resistance6':14,'driving_resistance7':15,'driving_resistance8':16,
                            'driving_resistance9':17,'driving_resistance10':18,'driving_resistance11':19,'driving_resistance12':20,
                            'driving_resistance13':21,'driving_resistance14':22,'driving_resistance15':23,'driving_resistance16':24,
                            'driving_resistance17':25,'driving_resistance18':26,'driving_resistance19':27,'driving_resistance20':28,
                            'driving_resistance21':29,'driving_resistance22':30
                           }


gear_for_torque_dict = {"1":  9, "2":  10, "3":  11, "4":  12, "5":  13, "6":  14, "7":  15, "8":  16, "9":  17, "10":  18, "11":  19, 
                        "12":  20, "13":  21, "14":  22, "15":  23, "16":  24, "17":  25, "18":  26, "19":  27, "20":  28
                        }

input_json = json.dumps(inputdata)

