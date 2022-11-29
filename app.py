from flask import Flask, request, render_template, url_for, redirect, session
import win32com.client
from win32com.client import Dispatch
import shutil
import time
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib.figure import Figure
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import pandas as pd
import pythoncom
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import logging
from src.input_variable import trans_dict, engine_dict,input_json,driving_resistance_cell, gear_for_torque_dict
# from .src.air_resistence import
import webbrowser
from threading import Timer
app = Flask(__name__, template_folder='templates', static_url_path='/static')
import json
import dataframe_image as dfi


# jsoninput = json.loads(inputjson)
app.secret_key = "27eduCBA09"

inputdata = json.loads(input_json)

@app.route("/")
def display():
    return render_template("index.html",inputdata  = inputdata)

@app.route("/", methods=['POST'])   
def graph():
    engine = request.form.get('engine')
    emission = request.form.get('emission')
    session["engine"] = engine
    session["emission"] = emission
    x1 = engine_dict[str(engine)+'_'+str(emission)]['Engine speed']
    y1 = engine_dict[str(engine)+'_'+str(emission)]['Torque']
    x2 = engine_dict[str(engine)+'_'+str(emission)]['Engine speed']
    y2 = engine_dict[str(engine)+'_'+str(emission)]['Power']
    col1 = 'steelblue'
    col2 = 'red'
    fig, ax = plt.subplots()
    ax.plot(x1, y1, color=col1)
    ax.set_xlabel("Engine speed[rpm]", fontsize=14)
    ax.set_ylabel("Torque[Nm]", color=col1, fontsize=16)
    ax2 = ax.twinx()
    ax2.plot(x2, y2, color=col2)
    ax2.set_ylabel("Power[kW]", color=col2, fontsize=20)
    plt.xlim(500, 5000)
    plt.ylim(0,160)
    plt.savefig("static\output.jpg", dpi=800)
    image = Image.open(".\static\output.jpg")
    image = image.resize((300, 200), Image.ANTIALIAS)
    image.save(fp="static\graph.png")
    image_path = "static\graph.png"
    return engine, emission


@app.route("/output", methods=["GET", "POST"])
def output_page(): 
    global engine_dict
    if request.method == "POST": 
        input_form = {}      
        input_form["vehicle_name"] = vehicle_name = request.form.get("vehicle_name")
        input_form["vehicle_weight"] = vehicle_weight = request.form.get("vehicle_weight")
        input_form["engine"] = engine = session.get("engine", None)
        input_form["emission"] = emission = session.get("emission", None)
        input_form["transmission"] = transmission = request.form.get("transmission_type")
        input_form["axel"] = axel = request.form.get("axel_type")
        input_form["axel_layout"] = axel_layout = request.form.get("axle_layout_type")
        input_form["ratio"] = ratio = request.form.get("ratio_type")
        input_form["efficiency"] = efficiency = request.form.get("efficiency_type")
        input_form["tyre_size"] = tyre_size = request.form.get("tyre_type")
        input_form["standard"] = standard = request.form.get("standard_type")
        input_form["application"] = application = request.form.get("application_type")
        input_form["radius"] = radius = request.form.get("radius_type")
        input_form["rrc"] = rrc = request.form.get("rrc_type")
        input_form["category"] = request.form.get("category")
        input_form["cab"] = request.form.get("cab")
        input_form["rear_body"] = request.form.get("rear_body")
        input_form["air_resistance"] = air_resistance = request.form.get("air_resistance_type")
        input_form["A_da"] = A_da = request.form.get("Torque_cut_A")
        input_form["B_da"] = B_da = request.form.get("Torque_cut_B")
        input_form["C_da"] = C_da = request.form.get("Torque_cut_C")
        input_form["D_da"] = D_da = request.form.get("Torque_cut_D")
        Gear_A = request.form.get("Gear_A").split(",")
        Gear_B = request.form.get("Gear_B").split(",")
        Gear_C = request.form.get("Gear_C").split(",")
        Gear_D = request.form.get("Gear_D").split(",")
        input_form["Gear_A"] = ",".join(Gear_A)
        input_form["Gear_B"] = ",".join(Gear_B)
        input_form["Gear_C"] =",".join(Gear_C)
        input_form["Gear_D"] = ",".join(Gear_D)
        input_form["colorRadio"] = request.form.get("colorRadio")
        input_form["gear_display"] = request.form.get("gear_display")
        input_form["pattern"] = request.form.get("pattern")
        input_form["remark"] = request.form.get("remark")
        driving_resistance_dict = {}
        for drive_res in range(1, 23):
            driving_resistance_dict["driving_resistance"+str(drive_res)] = request.form.get("driving_resistance_{}".format(drive_res))
        input_form["starting_value"] = starting_value = request.form.get("starting_value")
        input_form["step_size"] = step_size = request.form.get("step_size")
        Gear_value = {"A":Gear_A, "B":Gear_B, "C":Gear_C, "D":Gear_D}
        input_form["file_path"] = file_path = request.form.get("file_path")
        print(file_path)
        chan_val = 1
        chan_val = + 1
        input_form.update(driving_resistance_dict)
        # excel = Dispatch('Excel.Application', pythoncom.CoInitialize())
        try:
            shutil.copyfile('data\Longitudinal_simulation_sample.xlsx',
                        f'{file_path}' + f'\{vehicle_name}'+'.xlsx')
            excel = win32com.client.Dispatch(
                'Excel.Application', pythoncom.CoInitialize())
            output_filepath = rf"{file_path}" + f'\{vehicle_name}'+'.xlsx'
            wb = excel.Workbooks.Open(output_filepath)
            sheet = wb.Worksheets('Longitudinal')
        except:
            return render_template("Error_page.html")
        inertia = 0
        trans_row, engine_row, torque_row2 = 9, 49, 69 
        
        if vehicle_name:
            sheet.Cells(2, 5).Value = vehicle_name
        if transmission:
            # print(trans_dict[str(trans_da)])
            sheet.Cells(7, 5).Value = transmission
            inertia = len(trans_dict[str(transmission)]['Gear ratio'])
            for ii in range(0, len(trans_dict[str(transmission)]['Gear ratio'])):
                sheet.Cells(trans_row, 5).Value = trans_dict[str(
                    transmission)]['Gear ratio'][ii]
                sheet.Cells(trans_row, 6).Value = trans_dict[str(
                    transmission)]['Efficiency'][ii]
                trans_row = trans_row+1

        if engine and emission:
            for ii in range(0, len(engine_dict[str(engine)+'_'+str(emission)]['Engine speed'])):
                sheet.Cells(engine_row, 5).Value = engine_dict[str(
                    engine)+'_'+str(emission)]['Engine speed'][ii]
                sheet.Cells(engine_row,  6).Value = engine_dict[str(
                    engine)+'_'+str(emission)]['Torque'][ii]
                sheet.Cells(engine_row,  7).Value = engine_dict[str(
                    engine)+'_'+str(emission)]['Power'][ii]   
                engine_row = engine_row+1
            sheet.Cells(42,5).Value = engine
            #sheet.Cells(43,5).Value = emission
            
        if axel:
            # print(axel)
            sheet.Cells(29, 5).Value = axel

        if ratio:
            sheet.Cells(30, 5).Value = float(ratio)

        if efficiency:
            sheet.Cells(31, 5).Value = float(efficiency)

        if tyre_size:
            sheet.Cells(32, 5).Value = tyre_size

        if radius:
            sheet.Cells(33, 5).Value = float(int(radius)/1000)

        if inertia:
            sheet.Cells(34, 5).Value = int(inertia)

        if rrc:
            sheet.Cells(36, 5).Value = float(rrc)

        if air_resistance:
            sheet.Cells(38, 5).Value = float(air_resistance)

        if vehicle_weight:
            sheet.Cells(6, 5).Value = int(vehicle_weight)

        if A_da:
            sheet.Cells(69, 6).value = int(A_da)
            sheet.Cells(76, 6).value = int(A_da)
        if B_da:
            sheet.Cells(70, 6).value = int(B_da)
            sheet.Cells(101, 6).value = int(B_da)
        if C_da:
            sheet.Cells(71, 6).value = int(C_da)
            sheet.Cells(126, 6).value = int(C_da)
        if D_da:
            sheet.Cells(72, 6).value = int(D_da)
            sheet.Cells(151, 6).value = int(D_da)
            
        for key in driving_resistance_dict:
            if driving_resistance_dict[key]:
                sheet.Cells(driving_resistance_cell[key], 11).Value = driving_resistance_dict[key] +"%"
        
        
        if starting_value:
            starting = int(starting_value)
        else:
            starting = 0
        if step_size:
            step = int(step_size)
        else:
            step = 2  
        for cell in range(9, 31):
            sheet.Cells(cell, 11).Value = str(starting) + "%"
            starting += step
            

        for gear in Gear_value:
            if "" not in Gear_value[gear]:
                for value in Gear_value[gear]:
                    try:
                        sheet.Cells(gear_for_torque_dict[value], 7).Value = gear
                    except:
                        pass
                    
            else:
                pass
        
        wb.Save()
        wb.Close()
        excel.Quit()
        os.startfile(output_filepath)
        df = pd.read_excel(output_filepath)
        df = df.drop("Unnamed: 9", axis=1)
        n = len(list(round(i, 3) for i in df.iloc[65, 10:30].tolist() if i!="-"))
        table_len = list(range(1, n+1))
        new_table = pd.DataFrame(columns = ["Values", "units"] + list(range(1,21)))
        new_table.loc[0] = df.iloc[65, 8:30].tolist()
        new_table.loc[1] = df.iloc[66, 8:30].tolist()
        new_table.loc[2] = df.iloc[67, 8:30].tolist()
        new_table.loc[3] = df.iloc[68, 8:30].tolist()
        
        table_data = {
            "row1" : ["Max Velocity at no slope", "km/h"] + list(round(i, 3) for i in df.iloc[65, 10:30].tolist() if i!="-"),
            "row2" : ["@rpm"] + list(round(i, 3) for i in df.iloc[66, 10:30].tolist() if i!="-"),
            "row3" : ["Climb ability", "%"] + list(str(round(i*100, 3))+"%" for i in df.iloc[67, 10:30].tolist() if i!="-"),
            "row4" : ["@km/h"] + list(round(i, 3) for i in df.iloc[68, 10:30].tolist() if i!="-")
        }
        
    return render_template("output.html", input_form = input_form, inputdata = inputdata ,result_text = "Success!! Excel Generated", table_data = table_data, table_len = table_len)

def main():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1, webbrowser.open_new('http://127.0.0.1:5050/')).start();
    app.run(debug=True, port=(5050))

if __name__ == "__main__":
    main()