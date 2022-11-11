#Porject Name: ArquiBot ("Arquitectura de Robots")       juliomoreno7217@gmail.com
#Creation date: 2022 / october / 30 / 07:42 h  

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from PanelsArea import PanelWidgets    
import time
import os
import serial
import math
from tkinter.filedialog import asksaveasfile
import numpy as np
from datetime import datetime

import matplotlib
matplotlib.use("TkAgg")         #backend
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d
import random

class ArquiBot(PanelWidgets):
    def __init__(self, Window):
        super().__init__()
        self.MainWindow = Window
        self.MainWindow_Width="1070"
        self.MainWindow_Height="650"
        self.MainWindow.geometry('{}x{}'.format(self.MainWindow_Width,self.MainWindow_Height))
        self.MainWindow.title("Interfaz Arquibot HMI")

        self.CreatePanels(self.MainWindow)

        #Graph settings:
        self.GraphFigure = Figure(figsize=(3,3),dpi=150,edgecolor='black')
        self.Graph = self.GraphFigure.add_subplot(111, projection='3d')
            
            #canvas._tkcanvas.destroy()
        self.canvas = FigureCanvasTkAgg(self.GraphFigure, self.MatplotlibGraph_LFrame)
        self.canvas.get_tk_widget().pack(side=TOP, fill = BOTH, expand=False)
        toolbar = NavigationToolbar2Tk(self.canvas, self.MatplotlibGraph_LFrame)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand=False)
        self.SetGraphProperties()
        self.PlotData()
    ##INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE##
    ##INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE####INTERACTION##ZONE##

    def SetEditableEntries(self):
        if self.ControlMode.get() == "direct":
            self.BaseAngle.configure(state='normal')
            self.VerticalPosition.configure(state ='normal')
            self.HorizontalPosition.configure(state ='normal')
            
            self.XCoord.configure(state ='disabled')
            self.YCoord.configure(state ='disabled')
            self.ZCoord.configure(state ='disabled') 
            # self.JunctionState = "normal"
            # self.CoordState = "disabled"
        else:
            self.BaseAngle.configure(state ='disabled')
            self.VerticalPosition.configure(state ='disabled')
            self.HorizontalPosition.configure(state ='disabled')
            
            self.XCoord.configure(state ='normal')
            self.YCoord.configure(state ='normal')
            self.ZCoord.configure(state ='normal')
            # self.JunctionState = "disabled"
            # self.CoordState = "normal"

    def MoveRobot(self):
        self.SendDataToArduino(self.ValidateData())
        self.ReadDataFromArduino()
        pass

    def SendDataToArduino(self,parameters=()):
        pass


    def ValidateData(self):
        
        pass


    def ReadDataFromArduino(self):
        pass


    def PlotData(self):
        self.Graph.clear()
        #self.Graph.plot(self.TimeArray,self.InputVoltageArray, color='#A5F4FA',linestyle='solid', marker='o',markersize='4', label="V_in")
        #self.Graph.plot(self.TimeArray,self.OutputVoltageArray, color='#E3FA98',linestyle='solid', marker='x',markersize='4', label="V_out")
        #self.canvas.draw_idle()


        #EndEffector Position:
        X = float(self.XCoord.get())
        Y = float(self.YCoord.get())
        Z = float(self.ZCoord.get())
        self.Graph.scatter(X, Y, Z)
        self.SetGraphProperties()
        pass

    def SetGraphProperties(self):
        font = {'family': 'Arial Rounded MT Bold',
        'color':  'white',
        'weight': 'normal',
        'size': 12,
        }
        self.Graph.set_title('Posición del Efector', fontdict = font)
        self.Graph.grid(color='#667B84')
        self.Graph.set_xlabel("Eje X [cm]",fontdict = font)
        self.Graph.set_ylabel("Eje Y [cm]",fontdict = font)
        self.Graph.set_zlabel("Eje Z [cm]",fontdict = font)
        #self.Graph.legend(["V_in","V_out"])  
        self.Graph.grid(color='#667B84')
        self.GraphFigure.patch.set_facecolor('#465162')
        self.Graph.xaxis.label.set_color('white')        #setting up X-axis label color 
        self.Graph.yaxis.label.set_color('white')        #setting up Y-axis label color 
        self.Graph.set_facecolor('#465162')              #Grah Background color
        self.Graph.tick_params(axis='x', colors='#92C2E2',labelsize=10)  #setting up X-axis tick color to red
        self.Graph.tick_params(axis='y', colors='#92C2E2',labelsize=10)  #setting up Y-axis tick color to black
        pass

if __name__ == '__main__':
    Window = Tk()
    application = ArquiBot(Window)
    Window.mainloop()
