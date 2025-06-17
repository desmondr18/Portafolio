from playwright.async_api import async_playwright
import time
import pandas as pd
import asyncio
import datetime
import tkinter as tk
from tkinter import filedialog
import os
# Crear una ventana oculta
root = tk.Tk()
root.withdraw()
# Mostrar el diálogo para seleccionar carpeta
folder_path = filedialog.askdirectory(title="Selecciona una carpeta para guardar el archivo")

años =[]
meses=["ENERO","FEBRERO","MARZO", "ABRIL", "MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
for i in range(2018,2026):
    años.append(f"{i}")
semaphore = asyncio.Semaphore(3)
async def procesar_mes(p,mes,año):
        async with semaphore:        
            browser = await p.chromium.launch(headless=True) 
            context = await browser.new_context()
            page = await browser.new_page()
                    
            await page.goto("https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Tarifas/TarifaDAC.aspx")  
            print(f"Procesando: {mes},{año}")
            añosInt = int(año)
            if añosInt > 2024:
                await page.select_option("#ContentPlaceHolder1_Fecha_ddAnio", año)
                await page.select_option("#ContentPlaceHolder1_Fecha1_ddMes", mes)
            else:
                await page.select_option("#ContentPlaceHolder1_Fecha_ddAnio", año)
                await page.select_option("#ContentPlaceHolder1_MesVerano3_ddMesConsulta", mes)
            try:
                await page.wait_for_selector("#TarifaDacV.table", state="visible", timeout=10000)
            except:
                print(f"No se logro para {año},{mes}")
            tabla1 = await page.query_selector("#TarifaDacFV.table")
            filas1 = await tabla1.query_selector_all("tr")
                
            tabla2 = await page.query_selector("#TarifaDacV.table")
            filas2 = await tabla2.query_selector_all("tr")        
            resultsTabla1=[]
            resultsTabla2=[]
            
            for i, fila in enumerate(filas1):            
                celdas = await fila.query_selector_all("td, th")
                
                if(i>1):
                    resultsTabla1.append(año)
                    resultsTabla1.append(mes)
                    for y,celda in enumerate(celdas):
                        datos_celdas = await celda.inner_text() if fila else ""
                        
                        resultsTabla1.append(datos_celdas)
            
            for i, fila in enumerate(filas2):            
                celdas = await fila.query_selector_all("td, th")
                  
                if(i>1):
                    resultsTabla2.append(año)
                    resultsTabla2.append(mes)  
                    for y,celda in enumerate(celdas):
                        datos_celdas = await celda.inner_text() if fila else ""
                                        
                        resultsTabla2.append(datos_celdas)
            results = []
            results.append(resultsTabla1)
            results.append(resultsTabla2)
            await browser.close()
            return results


async def main():
    async with async_playwright() as p:
            tasks=[]
            for r in años:
                añosInt = int(r)
                if añosInt == datetime.datetime.today().year:
                    for i in range(datetime.datetime.today().month):
                        tasks.append(procesar_mes(p,meses[i],r))
                else:
                    for q in meses:
                        tasks.append(procesar_mes(p, q,r))
            results= await asyncio.gather(*tasks)
    reorganized_data1 =[]
    reorganized_data2 =[]
    for res in (results):
        for x,elements in enumerate(res):
            if x ==0:
                for i in range(0, len(elements), 6):
                    reorganized_data1.append(elements[i:i+6])
            else:
                for i in range(0, len(elements), 5):
                    reorganized_data2.append(elements[i:i+5])
    df1=pd.DataFrame(reorganized_data1,columns=['Año','Mes','Lugar','Cargo_Fijo','Cargo_Temp_Ver','Cargo_Temp_FVer'])
    df1.to_excel(f"{folder_path}/Tabla_1.xlsx")
    df2=pd.DataFrame(reorganized_data2,columns=['Año','Mes','Lugar','Cargo_Fijo','Costo Energia'])
    df2.to_excel(f"{folder_path}/Tabla_2.xlsx")
asyncio.run(main())

