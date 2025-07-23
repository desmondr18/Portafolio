import pandas as pd
import xml.etree.ElementTree as et
import tkinter as tk
from tkinter import filedialog
import os

xml_files = []
listaD=[]
rfc=[]
nombres=[]
iva=[]
sub_total=[]
# Crear una ventana oculta
root = tk.Tk()
root.withdraw()

# Mostrar el diálogo para seleccionar carpeta
folder_path = filedialog.askdirectory(title="Selecciona una carpeta")

for file in os.listdir(folder_path):
    if file.endswith('.xml'):
        xml_files.append(os.path.join(folder_path, file))
def funcionConv(ruta):
    arbol = et.parse(ruta)
    raiz= arbol.getroot()
    for x,nodo in enumerate(raiz):
        print(nodo)
        if(x==0):
            rf = nodo.attrib.get("Rfc")
            nombre=nodo.attrib.get("Nombre")
            nombres.append(nombre)
            rfc.append(rf)
        if(x==3):
            iva.append(nodo.attrib.get("TotalImpuestosTrasladados"))
            sub_total.append(nodo.find("{http://www.sat.gob.mx/cfd/4}Traslados").find("{http://www.sat.gob.mx/cfd/4}Traslado").attrib.get("Base"))
        if(x==4):
            tmbr=nodo.find("{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital").attrib.get("UUID")
            listaD.append(tmbr)
for xml in xml_files:
    funcionConv(xml)

df=pd.DataFrame({"Numero de folio fiscal(CFDI)":listaD,"Nombre de Proveedor":nombres,"RFC Proveedor":rfc,"Subtotal":sub_total,"IVA":iva})
df.to_excel(f"{folder_path}/Facturas.xlsx")

