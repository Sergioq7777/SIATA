"""
--- Analisis de datos:


Problematica:
-Crear un sistema de informacion que permita concer la ubicacion de sus rcuersos: 
  (paquetes , vehiculos y personal operativo) en tiempo real.


RF01:
1-Listar las ubicaciones con su numero de casos asociados para un dia especifico.
2-Listar las ubicaciones con su numero de casos asociados para un rango de fecha.
3-Listar las ubicaciones con su numero de casos asociados en un dia especifico para un pais en especifico.
4-Listar el numero de casos totales para un dia especifico en un pais especifico.
5-Exportar la solucion punto uno en KML
"""

#proceso para instalar libreria para facilitar lectura de datos: pip install pandas.
import csv

def buscador(num, index):
    with open("COVID_21Jan_12Mar.csv") as archivo:
        datos = csv.reader(archivo,delimiter=",")
        next(datos)
        
        num = str(num)
        for line in datos:
            country = line[2]
            date = line[5]
            date = date.split("/")
            if num==date[index]:
                print(f"""
                date: {line[5]}
                confirmed: {line[6]}
                recovered: {line[7]}
                death: {line[8]}
                """)
                break
            elif num == line[2]:
                print(f"""
                country: {line[2]}
                date: {line[5]}
                confirmed: {line[6]}
                recovered: {line[7]}
                death: {line[8]}
                """)


def mes_dia_año():
    opt = int(input("""
    1-Buscar por mes.
    2-Buscar por dia.
    3-Buscar por año.
    4-Buscar por pais.
    type:
    """))
    if opt == 1:
        opt_dos = int(input("Ingrese Numero del mes: "))
        buscador(opt_dos,0)
    elif opt == 2:
        opt_dos = int(input("Ingrese Numero del dia: "))
        buscador(opt_dos,1)
    elif opt == 3:
        opt_dos = int(input("Ingrese ultimos dos digitos del año: "))
        buscador(opt_dos,2)
    elif opt == 4:
        opt_dos = str(input("Ingrese el pais: "))
        buscador(opt_dos,0)




mes_dia_año()