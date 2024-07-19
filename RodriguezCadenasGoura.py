import random
import math
import statistics
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores_con_sueldo=[]

def asignarsueldos():
    for i in trabajadores:
        sueldo= random.randint(300000,2500000)
        trabajadores_con_sueldo.append({"Nombre":i ,"Sueldo":sueldo})
    print("Asignacion exitosa")

def clasificarsueldos():
    try:
        if len(trabajadores_con_sueldo)<10:
            print("Debes asignar los sueldos primero en el paso 1")
        else:

            sueldomenor=[]
            sueldomedio=[]
            sueldomayor=[]
            for i in trabajadores_con_sueldo:
                if int(i["Sueldo"])>2000000:
                    sueldomayor.append(i)
                elif int(i["Sueldo"])>800000 and int(i["Sueldo"])<2000000:
                    sueldomedio.append(i)
                elif int(i["Sueldo"])<800000:
                    sueldomenor.append(i)

            print(f"Sueldos menores a 800.000 son TOTAL  {len(sueldomenor)}")
            print("Nombre del Empleado     Sueldo")
            for i in sueldomenor: 
            
                print(f"{i["Nombre"]}      {i["Sueldo"]}") 
            
            
            print(f"Sueldos entre 800.000 y 2.000.000 son TOTAL  {len(sueldomedio)}")
            print("Nombre del Empleado     Sueldo")
            for i in sueldomedio: 
            
                print(f"{i["Nombre"]}      {i["Sueldo"]}")   

            print(f"Sueldos mayores a  2.000.000 son TOTAL  {len(sueldomayor)}")
            print("Nombre del Empleado     Sueldo")
            for i in sueldomayor: 
            
                print(f"{i["Nombre"]}      {i["Sueldo"]}")                                  
    except Exception as e:
        print(f" Se genero un error de tipo {e}")
        print("Asegurese de haber asignado los sueldos en opcion 1")
def verestadisticas():
    try:
        todoslossueldo=[]
        for i in trabajadores_con_sueldo:
            todoslossueldo.append(i["Sueldo"])

        mayor= max(todoslossueldo)
        menor=min(todoslossueldo)
        promedio=statistics.mean(todoslossueldo)
        promediogeo=statistics.geometric_mean(todoslossueldo)
        print(f"El sueldo mas alto es  {mayor}")
        print(f"El sueldo mas bajo es  {menor}")
        print(f"El Sueldo promedio es {promedio}")
        print(f"El sueldo Promedio geometrico es  {promediogeo}")
    except Exception as e:
        print(f" Se genero un error de tipo {e}")
        print("Asegurese de haber asignado los sueldos en opcion 1")

def reportedesueldos():
    try:
        if len(trabajadores_con_sueldo)<10:
            print("Debes asignar los sueldos primero en el paso 1")
        else:    
            listareporte=[]
            print("Nombre empleado   Sueldo Base   Descuento Salud   Descuento AFP   Sueldo Líquido")
            for i in trabajadores_con_sueldo:
                afp= float(i["Sueldo"])*0.12
                salud= float(i["Sueldo"])* 0.07
                liquido= float(i["Sueldo"])-afp-salud
                print(f"{i["Nombre"]}   {i["Sueldo"]}   {afp}   {salud}   {liquido}")
                listareporte.append({
                    "Nombre":i["Nombre"],
                    "Sueldo": i["Sueldo"],
                    "Descuento Afp":afp,
                    "Descuento Salud":salud,
                    "Sueldo Liquido":liquido

                })
            with open ("Reporte.csv","w",newline="")as archivocsv:
                reporte=csv.writer(archivocsv)
                reporte.writerow(listareporte)    
    except Exception as e:
        print(f" Se genero un error de tipo {e}")
        print("Asegurese de haber asignado los sueldos en opcion 1")
        
def salir():
    print("Finalizando programa....")
    print("Desarrollado por Goura Rodriguez")
    print("Rut 25.750.591-k")
    exit()

def main():
    while True:
        try:    
            menu=int(input("""
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadísticas.
    4. Reporte de sueldos
    5. Salir del programa
                        """))  
            if menu ==1:
                asignarsueldos()
            elif menu==2:
                clasificarsueldos()
            elif menu ==3:
                verestadisticas()
            elif menu ==4:
                reportedesueldos()
            elif menu ==5:
                salir()
            else:
                print("Escoja una opcion valida")
        except Exception as E:
            print(" la opcion debe de ser un numero")

main()            
