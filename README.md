# Proyecto: Análisis de Datos de Embarazo en México

Este proyecto realiza un análisis exploratorio de datos sobre nacimientos y embarazos en México durante los años 2020, 2021, 2022 y 2023. Se procesan archivos CSV oficiales que contienen información como edad de la madre, estado conyugal, entidad federativa del parto, entre otros.

El objetivo principal es generar visualizaciones, estadísticas y reportes que permitan identificar patrones, tendencias y problemáticas como la mortalidad materna o el crecimiento de embarazos en menores de edad.

---

## Contenido

- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Funciones](#funciones)
- [Ejemplo de Ejecución](#ejemplo-de-ejecución)

---

## Instalación

Clona este repositorio y asegúrate de colocar los archivos CSV en la carpeta `csv/`:

```bash
git clone https://github.com/desmondr18/Portafolio.git
cd nacimientos
mkdir csv
# Coloca tus archivos CSV aquí
```

Instala las dependencias necesarias:

```bash
pip install pandas matplotlib seaborn rich
```

---

## Estructura del Proyecto

```
proyecto-embarazos/
├── csv/                # Archivos CSV de entrada
├── main.py            # Script principal
├── README.md          # Documentación del proyecto
```

---

## Dependencias

- `pandas`
- `matplotlib`
- `seaborn`
- `rich`

---

## Funciones

### `promedioMuertesEmbarazo()`

Calcula el total de nacimientos, muertes maternas y porcentaje de mortalidad por parto. Muestra los resultados en una tabla con formato amigable usando `rich`.

### `contMadresSolteras()`

Compara el número de madres solteras y casadas por año. Visualiza los datos en una gráfica de barras.

### `contarMayoresMenores(df)`

Devuelve un resumen con el número de embarazos en menores y mayores de edad a partir de la columna `EDAD_Num`.

### `edades()`

Grafica la distribución de embarazos por edad materna. Muestra la cantidad de embarazos para cada edad hasta 98 años.

### `lugaresNacimiento()`

Cuenta los embarazos por entidad federativa del parto. Genera una gráfica ordenada por cantidad.

### `fechaNac()`

Cuenta los nacimientos por mes a partir de la fecha. Muestra una tabla con el total por mes.

### `mapaCalor()`

Genera un mapa de calor con el promedio de nacimientos por cada día del año. Ideal para detectar patrones estacionales.

### `limpiezaCSV(file, x)`

Carga columnas relevantes de un CSV y añade el año correspondiente a los datos para consolidarlos posteriormente.

---

## Ejemplo de Ejecución

```python
# Cargar y limpiar CSV
for x, file in enumerate(csv_files):
    limpiezaCSV(file, x)
final_df = pd.concat(datos_limpios, ignore_index=True)

# Llamar funciones de análisis
promedioMuertesEmbarazo()
contMadresSolteras()
edades()
lugaresNacimiento()
mapaCalor()
```

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes modificar, compartir y usar el código libremente.

