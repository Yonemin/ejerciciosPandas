from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import subprocess
pd.__version__
from objetos import Usuario

df_archivo_1=pd.read_csv("users.csv")
df_archivo_1["user"] = df_archivo_1["user"].astype(str).str.strip()
df_archivo_1["contrasena"] = df_archivo_1["contra"].astype(str).str.strip()

class inicioSesion:

    def __init__(self, root):
        self.root=root
        self.root.title("Bienvenido")
        self.root.geometry('250x300')
        root.configure(background='black')
        
        #self.espacio_label=tk.Label(root,background='lightblue',text=" ")
        #self.espacio_label.pack()

        self.nombre_label=tk.Label(root,background='black', foreground='#FF5A5F',text="Username",font=(30))
        self.nombre_label.pack(padx=10, pady=10)
        self.nombre_entry=tk.Entry(root,font=(30))
        self.nombre_entry.pack(padx=10, pady=10)

        self.password_label=tk.Label(root,background='black', foreground='#FF5A5F',text="Contraseña",font=(30))
        self.password_label.pack(padx=10, pady=10)
        self.password_entry=tk.Entry(root,font=(30), show="●")
        self.password_entry.pack(padx=10, pady=10)
        
        self.is_button=tk.Button(root,text="Iniciar sesión",font=(20),bg='#036362', foreground='#A8E8FF',command=self.permitirAcceso)
        self.is_button.pack(padx=12, pady=12)

    def permitirAcceso(self):
        nombre=self.nombre_entry.get().strip()
        password=self.password_entry.get().strip()

        if ((df_archivo_1["user"]==nombre) & (df_archivo_1["contrasena"]==password)).any():
            self.consultas()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def consultas(self):
        self.root.destroy()
        subprocess.Popen(["python", "querys.py"])

if __name__=="__main__":
        root=tk.Tk()
        inicioSesion = inicioSesion(root)
        root.mainloop()