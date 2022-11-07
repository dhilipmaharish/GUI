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
from src.input_varible import trans_dict, engine_dict,input_json, table_data
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
    return render_template("index.html",inputdata  = inputdata ,table_data=table_data)

@app.route("/", methods=['POST'])   
def graph():
    engine = request.form.get('engine')
    emission = request.form.get('emission')
    session["engine"] = engine
    session["emission"] = emission
    f = plt.figure(figsize=(6, 5), dpi=500)
    a = f.add_subplot(111)
    x1 = engine_dict[str(engine)+'_'+str(emission)]['Engine speed']
    y1 = engine_dict[str(engine)+'_'+str(emission)]['Torque']
    a.plot(x1, y1, label="Torque")
    x2 = engine_dict[str(engine)+'_'+str(emission)]['Engine speed']
    y2 = engine_dict[str(engine)+'_'+str(emission)]['Power']
    a.plot(x2, y2, label="Power")
    a.legend()
    plt.xlabel("Engine speed(RPM)")
    plt.ylabel("Engine torque(Nm)")
    plt.savefig("static\output.jpg", dpi=800)
    image = Image.open(".\static\output.jpg")
    image = image.resize((500, 200), Image.ANTIALIAS)
    image.save(fp="static\graph.png")
    image_path = "static\graph.png"
    return engine, emission


@app.route("/output", methods=["GET", "POST"])
def output_page(): 
    global engine_dict
    if request.method == "POST":       
        vehicle_name = request.form.get("vehicle_name")
        vehicle_weight = request.form.get("vehicle_weight")
        engine = session.get("engine", None)
        emission = session.get("emission", None)
        transmission = request.form.get("transmission_type")
        axel = request.form.get("axel_type")
        axel_layout = request.form.get("axle_layout_type")
        ratio = request.form.get("ratio_type")
        efficiency = request.form.get("efficiency_type")
        tyre_size = request.form.get("tyre_type")
        print(tyre_size)
        radius = request.form.get("radius_type")
        rrc = request.form.get("rrc_type")
        air_resistance = request.form.get("air_resistance_type")
        A_da = request.form.get("Torque_cut_A")
        B_da = request.form.get("Torque_cut_B")
        C_da = request.form.get("Torque_cut_C")
        D_da = request.form.get("Torque_cut_D")
        Gear_A = request.form.get("Gear_A").split(",")
        Gear_B = request.form.get("Gear_B").split(",")
        Gear_C = request.form.get("Gear_C").split(",")
        Gear_D = request.form.get("Gear_D").split(",")
        Gear_value = {"A":Gear_A, "B":Gear_B, "C":Gear_C, "D":Gear_D}
        file_path = request.form.get("file_path")
        chan_val = 1
        chan_val = + 1
       
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
            sheet.Cells(43,5).Value = emission
            
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
            
        gear_for_torque_dict = {
            "1":  9, 
            "2":  10, 
            "3":  11, 
            "4":  12, 
            "5":  13, 
            "6":  14, 
            "7":  15, 
            "8":  16, 
            "9":  17, 
            "10":  18, 
            "11":  19, 
            "12":  20, 
            "13":  21, 
            "14":  22, 
            "15":  23, 
            "16":  24, 
            "17":  25, 
            "18":  26, 
            "19":  27, 
            "20":  28
    }

        for gear in Gear_value:
            print(Gear_value)
            print(Gear_value[gear])
            if "" not in Gear_value[gear]:
                for value in Gear_value[gear]:
                    print(value)
                    print(gear)
                    sheet.Cells(gear_for_torque_dict[value], 7).Value = gear
                    
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
            "row1" : ["Max Velocity", "km/h"] + list(round(i, 3) for i in df.iloc[65, 10:30].tolist() if i!="-"),
            "row2" : ["@rpm"] + list(round(i, 3) for i in df.iloc[66, 10:30].tolist() if i!="-"),
            "row3" : ["Climb ability", "%"] + list(round(i, 3) for i in df.iloc[67, 10:30].tolist() if i!="-"),
            "row4" : ["@km/h"] + list(round(i, 3) for i in df.iloc[68, 10:30].tolist() if i!="-")
        }
        #df_styled = new_table.style.background_gradient()
        #dfi.export(df_styled, "mytable.png")
        
    return render_template("output.html", inputdata = inputdata ,result_text = "Success!! Excel Generated", table_data = table_data, table_len = table_len)

def main():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1, webbrowser.open_new('http://127.0.0.1:5050/')).start();
    app.run(debug=True, port=(5050))

if __name__ == "__main__":
    main()