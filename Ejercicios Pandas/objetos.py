import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import messagebox, Frame, Button

pd.__version__

class Usuario:
    def __init__(self,nombre,password):
        self.nombre=nombre
        self.password=password
        print('nom:'+self.nombre+', pas:'+self.password)