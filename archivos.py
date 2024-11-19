# Crear y escribir en un archivo de texto
with open('nombres.txt', 'w') as archivo:
    archivo.write("Ana\nJuan\nCarlos")

# Anexar datos
with open('nombres.txt', 'a') as archivo:
    archivo.write("\nLucía\nPedro")

# Leer el contenido
with open('nombres.txt', 'r') as archivo:
    print(archivo.read())


# Leer datos binarios y crear una copia de una imagen
with open('imagen_original.jpg', 'rb') as original:
    datos = original.read()

with open('imagen_copia.jpg', 'wb') as copia:
    copia.write(datos)


import xml.etree.ElementTree as ET

# Crear un archivo XML
raiz = ET.Element("libros")
libro = ET.SubElement(raiz, "libro", id="1")
ET.SubElement(libro, "titulo").text = "Cien Años de Soledad"
ET.SubElement(libro, "autor").text = "Gabriel García Márquez"
ET.SubElement(libro, "año").text = "1967"

arbol = ET.ElementTree(raiz)
arbol.write("biblioteca.xml")

# Leer el archivo XML
arbol = ET.parse("biblioteca.xml")
raiz = arbol.getroot()
for libro in raiz.findall("libro"):
    print(libro.find("titulo").text, libro.find("autor").text)


from openpyxl import Workbook
import pandas as pd

# Crear un archivo Excel
libro = Workbook()
hoja = libro.active
hoja.append(["Nombre", "Calificación"])
hoja.append(["Ana", 90])
hoja.append(["Juan", 85])
hoja.append(["Carlos", 88])
libro.save("calificaciones.xlsx")

# Leer datos del archivo Excel
datos = pd.read_excel("calificaciones.xlsx")
print(datos)
