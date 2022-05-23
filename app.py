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
from src.transmission import transmission_input
from src.engine import engine_input
from src.finaldrive import final_drive_input
from src.tire import tire_input
from src.air_resistence import air_resistance_input
# from .src.air_resistence import
import webbrowser
from threading import Timer
app = Flask(__name__, template_folder='templates', static_url_path='/static')

trans_dict, trans_drop = transmission_input()
engine_dict, engine_drop, emission_drop = engine_input()
axel_drop, axel_layout_drop, ratio_drop, efficiency_drop = final_drive_input()
tyre_size_drop, radius_drop, rrc_drop = tire_input()
air_drop = air_resistance_input()

app.secret_key = "27eduCBA09"

@app.route("/")
def display():
    return render_template("index.html", engine_drop=engine_drop, emission_drop=emission_drop, trans_drop=trans_drop, axel_drop=axel_drop, tyre_size_drop=tyre_size_drop, air_drop=air_drop)

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
    image = image.resize((300, 200), Image.ANTIALIAS)
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
        torquecut_da = request.form.get("Torque_cut").upper()
        torquecut_da = torquecut_da.split(',')
        A_da = request.form.get("Torque_cut_A")
        B_da = request.form.get("Torque_cut_B")
        C_da = request.form.get("Torque_cut_C")
        D_da = request.form.get("Torque_cut_D")
        file_path = request.form.get("file_path")
        chan_val = 1
        chan_val = + 1
       
        # excel = Dispatch('Excel.Application', pythoncom.CoInitialize())
        try:
            shutil.copyfile('data\Longitudinal_simulation_sample.xlsx',
                        f'{file_path}' + f'\{vehicle_name}'+'.xlsx')
            excel = win32com.client.Dispatch(
                'Excel.Application', pythoncom.CoInitialize())
            wb = excel.Workbooks.Open(rf"{file_path}" + f'\{vehicle_name}'+'.xlsx')
            sheet = wb.Worksheets('Longitudinal')
        except:
            return render_template("Error_page.html")
        inertia = 0
        trans_row, engine_row, torque_row1, torque_row2 = 9, 49, 9, 69 
        
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

        if torquecut_da:
            for pqe in torquecut_da:
                sheet.Cells(torque_row1, 7).Value = pqe
                sheet.Cells(torque_row2, 6).Value = pqe
                torque_row1 = torque_row1+1
                torque_row2 = torque_row2+1
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
        wb.Save()
        wb.Close()
        excel.Quit()
    return render_template("index.html", result_text="Success!! Excel Generated")

def main():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1, webbrowser.open_new('http://127.0.0.1:5050/')).start();
    app.run(debug=True, port=(5050))

if __name__ == "__main__":
    main()