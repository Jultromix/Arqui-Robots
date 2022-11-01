#Porject Name: ArquiBot ("Arquitectura de Robots")       juliomoreno7217@gmail.com
#Creation date: 2022 / october / 30 / 07:42 h  

from tkinter import *
from tkinter import ttk
from tkinter import Tk
import time
import os
from tkinter.tix import ComboBox

class PanelWidgets:
    def __init__(self):
        pass

    def CreatePanels(self,ParentName):
        self.CreateFrames(ParentName)
        self.CreateLabelFrames(ParentName)
        self.CreateLabels()
        self.CreateSpinBox()
        self.CreateComboboxes()
        self.CreateSliders()
        self.CreateRadiobuttons()
        self.CreateButtons()
        

    def CreateButtons(self):
        #-------Buttons in Controls Label Frame ---------#

        self.MoveButton= Button(self.Settings_LFrame, text="Mover", anchor='c', font=('Arial Rounded MT Bold', 9))
        self.MoveButton.grid(row=3, column=0, padx=10, ipadx =30)

        self.HomeButton= Button(self.Settings_LFrame, text="Casa", anchor='c', font=('Arial Rounded MT Bold', 9))
        self.HomeButton.grid(row=3, column=1, padx=10, pady=8, ipadx =30)
        
        
    def CreateComboboxes(self):
        #-------Comboboxes in Controls Label Frame--------------#
        self.SerialPort = ttk.Combobox(self.Settings_LFrame,width=6, value=['com1','com2','com3','com4','com5','com6'])
        self.SerialPort.set('com3')
        self.SerialPort.grid(row=0, column=1, padx=4, ipadx =30, columnspan=2)

        self.Badurate = ttk.Combobox(self.Settings_LFrame,width=6, value=['14400','19200','38400','57600','115200'])
        self.Badurate.set('9600')
        self.Badurate.grid(row=1, column=1, padx=4, ipadx =30, columnspan=2)

    def CreateFrames(self, ParentName):
        self.LFramesContaineer = ttk.Frame(ParentName, width='1200', height='600')
        self.LFramesContaineer.grid(row=0,column=0)
        pass


    def CreateLabels(self):
        #-------Labels in EndEffector Label Frame-------#

        self.X_Label=Label(self.EndEffector_LFrame, text = 'Posición X:  ', anchor='w', font=('Arial Rounded MT Bold', 9))
        self.X_Label.grid(row=0, column=0, ipadx=1, ipady=5, pady=5)

        self.Y_Label=Label(self.EndEffector_LFrame, text = 'Posición Y:  ', anchor='w', font=('Arial Rounded MT Bold', 9))
        self.Y_Label.grid(row=1, column=0, ipadx=1, ipady=5, pady=5)

        self.Z_Label=Label(self.EndEffector_LFrame, text = 'Posición Z:  ', anchor='w', font=('Arial Rounded MT Bold', 9))
        self.Z_Label.grid(row=2, column=0, ipadx=1, ipady=5, pady=5)


        #-------Labels in Joints Label Frame-------#
        self.BaseAngle_Label=Label(self.Joints_LFrame, text = 'Rotativa:  ', anchor='e', font=('Arial Rounded MT Bold', 9))
        self.BaseAngle_Label.grid(row=0, column=0, ipadx=1, ipady=5, pady=5)

        self.Vertical_Label=Label(self.Joints_LFrame, text = 'Prismática "Z":  ', anchor='e', font=('Arial Rounded MT Bold', 9))
        self.Vertical_Label.grid(row=1, column=0, ipadx=1, ipady=5, pady=5)

        self.Horizontal_Label=Label(self.Joints_LFrame, text = 'Prismática "XY":  ', anchor='e', font=('Arial Rounded MT Bold', 9))
        self.Horizontal_Label.grid(row=2, column=0, ipadx=1, ipady=5, pady=5)

        #-------Labels in Settings Label Frame-------#
        self.SerialPort_Label=Label(self.Settings_LFrame, text = 'Puerto:  ', anchor='e', font=('Arial Rounded MT Bold', 9))
        self.SerialPort_Label.grid(row=0, column=0, ipadx=1, ipady=5, pady=5)
        
        self.Baudrate_Label=Label(self.Settings_LFrame, text = 'Baudaje:  ', anchor='e', font=('Arial Rounded MT Bold', 9))
        self.Baudrate_Label.grid(row=1, column=0, ipadx=1, ipady=5, pady=5)
        
        self.Cinematic_Label=Label(self.Settings_LFrame, text = 'Tipo de Cinemática:  ', anchor='e', font=('Arial Rounded MT Bold', 9))
        self.Cinematic_Label.grid(row=2, column=0, ipadx=1, ipady=5, pady=5)

        pass

    def CreateLabelFrames(self,ParentName):
        self.EndEffector_LFrame = LabelFrame(self.LFramesContaineer, width=480, height= 610, text="Efector Final", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.EndEffector_LFrame.grid(row=1, column=0, padx = 7, pady=10, ipadx=20,ipady=1)

        self.Joints_LFrame = LabelFrame(self.LFramesContaineer, width=480, height= 610, text="Articulaciones", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.Joints_LFrame.grid(row=2, column=0, padx = 7, pady=10, ipadx=20,ipady=1)
        pass

        self.Settings_LFrame = LabelFrame(self.LFramesContaineer, width=480, height= 610, text="Configuración", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.Settings_LFrame.grid(row=0, column=0, padx = 7, pady=10, ipadx=20,ipady=1)
        pass

        self.MatplotlibGraph_LFrame = LabelFrame(ParentName, width=100, height= 90, text="Área de trabajo: ", 
        font=('Arial Rounded MT Bold', 10), labelanchor= "n", relief="solid")
        self.MatplotlibGraph_LFrame.grid(row=0, column=1, padx = 40, pady=15, ipadx=20,ipady=5)
    def CreateRadiobuttons(self):
        #-------Radiobuttons in Settings Label Frame----------#
        self.ControlMode = StringVar()
        self.ControlMode.set("inverse")

        self.DirectMode = Radiobutton(self.Settings_LFrame, text='Directa', value='direct', variable=self.ControlMode)
        self.DirectMode.grid(row=2, column=1 )

        self.InverseMode = Radiobutton(self.Settings_LFrame, text='Inversa', value='inverse', variable=self.ControlMode)
        self.InverseMode.grid(row=2, column=2)
        pass
        
    def CreateSliders(self):
        pass

    def CreateSpinBox(self):
        #-------SpinBoxes in EndEffector Label Frame-------#
        self.InitialPos = StringVar()
        self.InitialPos.set("0")
        self.XCoord = Spinbox(self.EndEffector_LFrame,width=7, from_=0.0, to=1800.0, textvariable= "0")
        self.XCoord.grid(row=0, column=1, ipadx=0,ipady=0, padx=4)

        self.YCoord = Spinbox(self.EndEffector_LFrame,width=7, from_=0.0, to=1800.0, textvariable= "0")
        self.YCoord.grid(row=1, column=1, ipadx=0,ipady=0, padx=4)

        self.ZCoord = Spinbox(self.EndEffector_LFrame,width=7, from_=0.0, to=1800.0, textvariable= "0")
        self.ZCoord.grid(row=2, column=1, ipadx=0,ipady=0, padx=4)

        #-------SpinBoxes in Joints Label Frame-------#
        self.InitialPos = StringVar()
        self.InitialPos.set("0")
        self.BaseAngle = Spinbox(self.Joints_LFrame,width=7, from_=0.0, to=1800.0, textvariable= self.InitialPos)
        self.BaseAngle.grid(row=0, column=1, ipadx=0,ipady=0, padx=8)

        self.VerticalPosition = Spinbox(self.Joints_LFrame,width=7, from_=0.0, to=1800.0, textvariable= self.InitialPos)
        self.VerticalPosition.grid(row=1, column=1, ipadx=0,ipady=0, padx=8)

        self.HorizonalPosition = Spinbox(self.Joints_LFrame,width=7, from_=0.0, to=1800.0, textvariable= self.InitialPos)
        self.HorizonalPosition.grid(row=2, column=1, ipadx=0,ipady=0, padx=8)
        