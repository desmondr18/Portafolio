dic=[]
ent=["EN","FE","MA","AB","MY","JN","JL","AG","SE","OC","NO","DIC"]
for i in range(12):
    dic.append(i+1)
diccionario={}
for clave,valor in zip(dic,ent):
    diccionario[clave]=valor
#print(diccionario)


diaMes={}
dia1=[]
dia2=[]
dia3=[]


for i in range(30):
    dia1.append(i+1)
for i in range(27):
    dia3.append(i+1)
for i in range(29):
    dia2.append(i+1)
diaMes["Enero"]=dia1
diaMes["Febrero"]=dia3
diaMes["Marzo"]=dia1
diaMes["Abril"]=dia2

diaMes["Mayo"]=dia1
diaMes["Junio"]=dia2

diaMes["Julio"]=dia1
diaMes["Agosto"]=dia1
diaMes["Septiembre"]=dia2

diaMes["Octubre"]=dia1
diaMes["Noviembre"]=dia2

diaMes["Diciembre"]=dia1



print(diaMes)