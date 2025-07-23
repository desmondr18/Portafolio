# Portafolio de Proyectos - Desmond Rodríguez

Este repositorio contiene una colección de proyectos orientados al análisis de datos, automatización de procesos administrativos y visualización interactiva de información. Está compuesto por herramientas desarrolladas en Python, con interfaz gráfica o ejecución directa, y pensadas para usuarios técnicos y no técnicos.

---

## Proyectos Incluidos

### 📄 `facturas/`

Herramienta que permite seleccionar una carpeta con archivos `.xml` de facturas CFDI (Comprobante Fiscal Digital por Internet). Extrae la información fiscal relevante como:

- RFC emisor y receptor
- Fecha de emisión
- Conceptos facturados
- Totales (subtotal, IVA, total)

El resultado se muestra en pantalla y puede exportarse. Incluye ejecutable listo para uso sin necesidad de instalar dependencias.

### 📅 `tarifa/`

Proyecto de web scraping que obtiene las **tarifas DAC** (Doméstico de Alto Consumo) directamente desde el portal oficial de la CFE. El programa:

- Extrae los datos hasta el mes más reciente
- Organiza la información en tablas
- Exporta los resultados a un archivo Excel (`.xlsx`)

Este proyecto también está disponible como ejecutable.

### 📆 `nacimientos/`

Análisis exploratorio de datos de embarazos en México entre 2020 y 2023. El script carga varios archivos CSV y genera:

- Gráficas por edad de la madre
- Estadísticas de mortalidad materna
- Comparación de madres solteras vs casadas
- Gráfica por estados
- Mapa de calor por fecha de nacimiento

Utiliza `pandas`, `matplotlib`, `seaborn` y `rich`. Puedes consultar el README específico dentro de esta carpeta.

### 📊 `powerBi/`

Contiene visualizaciones desarrolladas en Power BI para presentación de datos. Incluye reportes interactivos con filtros, segmentaciones y métricas diseñadas para análisis visual y toma de decisiones.

---

## Tecnologías usadas

- Python 3
- pandas, matplotlib, seaborn, rich
- Web scraping con `requests` y `BeautifulSoup`
- GUI con `tkinter` (facturas)
- Power BI (dashboards interactivos)

---

## Ejecución

Para los scripts en Python:

```bash
pip install -r requirements.txt
python script.py
```

Para los ejecutables, basta con hacer doble clic sobre el `.exe` correspondiente.

---

## Autor

Desmond Rodríguez\
[GitHub: desmondr18](https://github.com/desmondr18)

---

## Licencia

Este portafolio se comparte bajo licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

