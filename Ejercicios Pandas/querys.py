from tkinter import *
import tkinter as tk
from tkinter import messagebox, Frame, Button
import pandas as pd
import csv
pd.__version__

df_archivo_2=pd.read_csv("Sacramentorealestatetransactions.csv")

class Menu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master,width=1200,height=1200, bg='black')
        self.master = master
        self.pack()
        self.botones()

    def botones(self):
        self.uno_button=tk.Button(self,text="Viviendas en Sacramento, excepto las que tengan solo un baño y una habitación.",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_1)
        self.uno_button.pack(padx=15, pady=10)

        self.dos_button=tk.Button(self,text="Viviendas en Rancho Cordova y Antelope que cuesten menos de 150 000",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_2)
        self.dos_button.pack(padx=15, pady=10)

        self.tres_button=tk.Button(self,text="Viviendas que no tienen ni habitaciones ni baños",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_3)
        self.tres_button.pack(padx=15, pady=10)

        self.cua_button=tk.Button(self,text="Residencias en una latitud menor a 38.5 en Sloughhouse",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_4)
        self.cua_button.pack(padx=15, pady=10)

        self.cin_button=tk.Button(self,text="Viviendas vendidas el 19 de Mayo en la ciudad Lincoln",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_5)
        self.cin_button.pack(padx=15, pady=10)

        self.seis_button=tk.Button(self,text="Condos con dimensiones mayores a 1 000",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_6)
        self.seis_button.pack(padx=15, pady=10)

        self.sie_button=tk.Button(self,text="Vivienda multi familia con el código postal #95603",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_7)
        self.sie_button.pack(padx=15, pady=10)

        self.ocho_button=tk.Button(self,text="Viviendas con dimensiones menores a 1000, solo una cama y con un precio menor a 100 000",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_8)
        self.ocho_button.pack(padx=15, pady=10)

        self.nue_button=tk.Button(self,text="Viviendas vendidas el 16 de Mayo con un precio menor a 5 000",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_9)
        self.nue_button.pack(padx=15, pady=10)

        self.diez_button=tk.Button(self,text="Viviendas con 5 o más habitaciones y mínimo 2 baños",font=(20), bg='#036362', foreground='#A8E8FF',command=self.query_10)
        self.diez_button.pack(padx=15, pady=10)

        self.quit = tk.Button(self, text="Salir", background='#9C0720', fg="white", font=(20), command=self.master.destroy)
        self.quit.pack(side="bottom", padx=15, pady=15)

    def query_1(self):
        city="SACRAMENTO"
        beds=3
        baths=1
        result = df_archivo_2.query("city==@city and beds!=@beds and baths!=@baths")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Viviendas en Sacramento, excepto las que tengan solo un baño y una habitación.")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font=(20))
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_2(self):
        city1="RANCHO CORDOVA"
        city2="ANTELOPE"
        price=150000
        result = df_archivo_2.query("city==@city1 and price<@price or city==@city2 and price<@price")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Viviendas en Rancho Cordova y Antelope que cuesten menos de 150 000")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_3(self):
        beds=0
        baths=0
        result = df_archivo_2.query("beds==@beds and baths==@baths")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Viviendas que no tienen ni habitaciones ni baños")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_4(self):
        city="SLOUGHHOUSE"
        latitude = 38.5
        result = df_archivo_2.query("city==@city and latitude<@latitude")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Residencias en una latitud menor a 38.5 en Sloughhouse")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_5(self):
        sale_date = 'Mon May 19 00:00:00 EDT 2008'
        city="LINCOLN"
        result = df_archivo_2.query("city==@city and sale_date==@sale_date")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Viviendas vendidas el 19 de Mayo en la ciudad Lincoln")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_6(self):
        sq__ft=1000
        type="Condo"
        result = df_archivo_2.query("sq__ft>@sq__ft and type==@type")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Condos con dimensiones mayores a 1 000")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_7(self):
        zip=95603
        type="Multi-Family"
        result = df_archivo_2.query("type==@type and zip==@zip")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Vivienda multi familia con el código postal #95603")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_8(self):
        sq__ft=1000
        beds=1
        price=100000
        result = df_archivo_2.query("sq__ft<@sq__ft and beds==@beds and price<@price")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Viviendas con dimensiones menores a 1000, solo una cama y con un precio menor a 100 000")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_9(self):
        sale_date="Fri May 16 00:00:00 EDT 2008"
        price=5000
        result = df_archivo_2.query("sale_date==@sale_date and price<@price")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Viviendas vendidas el 16 de Mayo")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

    def query_10(self):
        beds=5
        baths=2
        result = df_archivo_2.query("beds>=@beds and baths>=@baths")
        
        ventana_result = tk.Toplevel()
        ventana_result.title("Viviendas con 5 o más habitaciones y mínimo 2 baños")
        
        frame_result = tk.Text(ventana_result, width=120, height=25, bg='black', foreground='white', font='20')
        frame_result.pack(padx=10, pady=10)
        
        frame_result.insert(tk.END, result)

if __name__=="__main__":
        root = tk.Tk()
        app = Menu(root)
        #app.wm_title('Menú')
        app.mainloop()
