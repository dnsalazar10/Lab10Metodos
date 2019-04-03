import pandas as pd

name=['fecha1','fecha2','hora','number','transacciones']
archivo = pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2008.txt",sep=';',names=name)
print(archivo)

archivo['new']=archivo['fecha1'].astype(str).str[0:10]
