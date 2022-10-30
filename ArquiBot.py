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
import numpy 


class ArquiBot(PanelWidgets):
    def __init__(self, Window):
        super().__init__()
        self.MainWindow = Window
        self.MainWindow_Width="1070"
        self.MainWindow_Height="650"
        self.MainWindow.geometry('{}x{}'.format(self.MainWindow_Width,self.MainWindow_Height))
        self.MainWindow.title("Interfaz Arquibot HMI")

        self.CreatePanels(self.MainWindow)

if __name__ == '__main__':
    Window = Tk()
    application = ArquiBot(Window)
    Window.mainloop()
