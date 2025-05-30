#funciones usadas para los calculos y generar las graficas necesarias

#   librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


#   funcion de Difusion:
#D(T) con D(T)=D_0 exp(-Q/RT)
def diffusion(T,D_0,Q):
    R=8.314 #J/K.mol
    D=D_0*np.exp((-Q*1000)/(R*T))
    return D

#Diffusion distance
#funcion para la distancia x=sqrt(Dt)
def distance(D,t):
    x=np.sqrt(D*t)
    return x


#   funciones para graficar
#funcion pra graficar todos los datos en una sola
def plot(dataframe, x_axis, y_axis, x_label, y_label, type):
    for system, data in dataframe.items():
        plt.plot(data[x_axis], data[y_axis], label=system)
    
    plt.xlabel(f'{x_label}')
    plt.ylabel(f'{y_label}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.show()
    filename = f"reporte/graficas/{y_axis}_{type}.pdf"
    plt.savefig(filename)
    plt.close()


#para graficar (si lo hago asi seria cada sistema por separado)
def plot2(dataframe, x_axis, y_axis, x_label, y_label):
    for system, data in dataframe.items():
        plt.figure()
        plt.plot(data[x_axis], data[y_axis], label=system)
        
        plt.xlabel(f'{x_label}')
        plt.ylabel(f'{y_label}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        #plt.show()
        #para guardar la imagen
        filename = f"reporte/graficas/{system}_{y_axis}.pdf"
        plt.savefig(filename)
        plt.close()