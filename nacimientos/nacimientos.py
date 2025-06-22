import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('seaborn-v0_8-whitegrid')

folder_path= "csv"
csv_files=[]
datos_limpios=[]
años=['2020','2021','2022','2023']
meses={1: 'EN', 2: 'FE', 3: 'MA', 4: 'AB', 5: 'MY', 6: 'JN', 7: 'JL', 8: 'AG', 9: 'SE', 10: 'OC', 11: 'NO', 12: 'DIC'}
datos=['EDAD', 'ESTADOCONYUGAL', 'SOBREVIVIOPARTO', 'ESCOLARIDAD', 'EDADPADRE', 'ENTIDADFEDERATIVAPARTO', 'MUNICIPIOPARTO', 'FECHANACIMIENTO', 'SEXO']
edos={0: 'NO ESPECIFICADO', 1: 'AGUASCALIENTES', 2: 'BAJA CALIFORNIA', 3: 'BAJA CALIFORNIA SUR', 4: 'CAMPECHE', 5: 'COAHUILA DE ZARAGOZA', 6: 'COLIMA', 7: 'CHIAPAS', 8: 'CHIHUAHUA', 9: 'CIUDAD DE MÉXICO', 10: 'DURANGO', 11: 
'GUANAJUATO', 12: 'GUERRERO', 13: 'HIDALGO', 14: 'JALISCO', 15: 'MÉXICO', 16: 'MICHOACÁN DE OCAMPO', 17: 'MORELOS', 18: 'NAYARIT', 19: 'NUEVO LEÓN', 20: 'OAXACA', 21: 'PUEBLA', 22: 'QUERÉTARO', 23: 'QUINTANA ROO', 24: 'SAN LUIS POTOSÍ', 25: 'SINALOA', 26: 'SONORA', 27: 'TABASCO', 28: 'TAMAULIPAS', 29: 'TLAXCALA', 30: 'VERACRUZ DE IGNACIO DE LA LLAVE', 31: 'YUCATÁN', 32: 'ZACATECAS'}
diaMes={'Enero': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31], 'Febrero': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28,29], 'Marzo': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31], 'Abril': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 26, 27, 28, 29,30], 'Mayo': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31], 'Junio': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30], 'Julio': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30.31], 'Agosto': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31], 'Septiembre': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30], 'Octubre': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31], 'Noviembre': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30], 'Diciembre': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31]}
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        csv_files.append(os.path.join(folder_path, file))
def limpiezaCSV(file,x):
    df = pd.read_csv(filepath_or_buffer=file,usecols=datos)
    df["Anios"]=años[x]
    datos_limpios.append(df)
for x,file in enumerate(csv_files):
    limpiezaCSV(file,x)
final_df = pd.concat(datos_limpios,ignore_index=True)
def promedioMuertesEmbarazo():
    totales=(final_df.EDAD.count())
    muertesdf = final_df[final_df["SOBREVIVIOPARTO"] == 2]
    muertes=(muertesdf.EDAD.count())
    promedio = (muertes/totales)*100
    print(f"Total de nacimientos en 3 años: {totales}")
    print(f"{muertes} mujeres murieron de un total de {totales} dando un promedio de {promedio} mujeres muertas por parto")
def contMadresSolteras():
    madresSolteras=final_df.groupby(["ESTADOCONYUGAL","Anios"]).SEXO.count().reset_index()
    madresSolteras=madresSolteras.rename(columns={"SEXO":"Cantidad"})
    madresSolteras = madresSolteras[madresSolteras["ESTADOCONYUGAL"].isin([5,1])]
    df_pivot = madresSolteras.pivot(index="Anios", columns="ESTADOCONYUGAL", values="Cantidad")
    df_pivot = df_pivot.rename(columns={1:"Solteras",5:"Casadas"})
    df_pivot.plot(kind='bar', color=["skyblue", "salmon"])
    plt.title("Crecimiento de madres solteras")
    plt.xlabel("Años")
    plt.ylabel("Cantidad")
    plt.legend(title="Estado conyugal")
    plt.tight_layout()
    plt.show()
def contarMayoresMenores(df):
    menores = (df["EDAD_Num"]<18).sum()
    mayores = (df["EDAD_Num"]>18).sum()
    return pd.Series({'Menores_Edad': menores, 'Mayores_edad': mayores})
def edades():
    final_df["EDAD_Num"] = pd.to_numeric(final_df["EDAD"],errors='coerce')
    edades=final_df.groupby("EDAD_Num").SEXO.count().reset_index()
    edades=edades.rename(columns={"SEXO":"Total_embarazos", "EDAD_Num":"Edad"})
    edades=edades[edades["Edad"]<99]
    sns.barplot(edades,x="Edad",y="Total_embarazos", hue="Edad", palette="muted", legend=False)
    plt.title("Distribucion de embarazos por edad")
    plt.xlabel("Edad")
    plt.ylabel("Cantidad")
    plt.show()
def lugaresNacimiento():
    lugares=final_df.groupby("ENTIDADFEDERATIVAPARTO").SEXO.count().reset_index()
    print(lugares)
    lugares=lugares.rename(columns={"SEXO":"Total_embarazos", "ENTIDADFEDERATIVAPARTO":"Estado"})
    lugares['Estado']=pd.to_numeric(lugares['Estado'],errors="coerce")
    lugares=lugares[(lugares["Estado"]!=0) & (lugares["Estado"]<32)]
    lugares["Estado"]=lugares["Estado"].map(edos)
    lugares=lugares.sort_values(by="Total_embarazos",ascending=False)
    print("Los valores de nacimiento ordenados por estado son:")
    print(lugares)
def fechaNac():
    final_df["FECHANACIMIENTO"] = pd.to_datetime(final_df["FECHANACIMIENTO"],errors="coerce")
    final_df["Mes_nacimiento"]=final_df["FECHANACIMIENTO"].dt.month
    fechaNacimiento=final_df.groupby("Mes_nacimiento").SEXO.count().reset_index()
    fechaNacimiento["Mes_nacimiento"]=fechaNacimiento["Mes_nacimiento"].map(meses)
    fechaNacimiento=fechaNacimiento.rename(columns={"SEXO":"Nacimientos"})
    print(fechaNacimiento)
def mapaCalor():
    final_df["FECHANACIMIENTO"] = pd.to_datetime(final_df["FECHANACIMIENTO"],errors="coerce",format="%d/%m/%Y")
    final_df["FECHANACIMIENTO"]=final_df["FECHANACIMIENTO"].dt.strftime('%m-%d')
    nacimientosFecha=final_df.groupby("FECHANACIMIENTO").SEXO.count().reset_index()
    nacimientosFecha=nacimientosFecha.rename(columns={"SEXO":"Nacimientos"})
    total=nacimientosFecha["Nacimientos"].sum()
    nacimientosFecha["Promedio"]=nacimientosFecha["Nacimientos"]/total *100
    totalPromedios=nacimientosFecha["Promedio"].sum()
    promedios=nacimientosFecha["Promedio"].to_list()
    indice_inicio = 0
    promedios_por_mes={}
    for mes, dias in diaMes.items():
        num_dias = len(dias) 
        print(num_dias)
        promedios_mes = promedios[indice_inicio:indice_inicio + num_dias]
        promedios_por_mes[mes]=(promedios_mes)
        indice_inicio += num_dias
    print(promedios_por_mes)
    longitud_deseada = 31
    for mes in promedios_por_mes:
        valores = promedios_por_mes[mes]
        faltantes = longitud_deseada - len(valores)
        promedios_por_mes[mes] = valores + [0] * faltantes
    df=pd.DataFrame(promedios_por_mes)
    df=df.transpose()
    df=df.rename(columns={x:y for x,y in zip(df.columns,range(1,len(df.columns)+1))})
    print(df)
    plt.figure(figsize=(15, 6))
    sns.heatmap(df, cmap="YlOrRd", annot=False, 
                xticklabels=range(1, 32 ), yticklabels=[
                    "Ene", "Feb", "Mar", "Abr", "May", "Jun", 
                    "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"])
    plt.xlabel("Día del mes")
    plt.ylabel("Mes")
    plt.title("Promedio de nacimientos por día del año")
    plt.show()
edades()
mapaCalor()
