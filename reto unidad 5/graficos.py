import matplotlib.pyplot as plt


def grafico_palabras(contador):

    palabras = []
    frecuencias = []

    top10 = contador.most_common(10)
    for palabra, cantidad in top10:
        palabras.append(palabra)
    frecuencias.append(cantidad)
    plt.figure(figsize=(8, 5))
    plt.barh(palabras,frecuencias)
    plt.title("Frecuencia de palabras")
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabras")
    plt.savefig("outputs/frecuencia_palabras.png")
    plt.show()
def grafico_histograma(lineas):
    longitudes = []
    for linea in lineas:
        longitudes.append(len(linea))
    plt.figure(figsize=(8, 5))
    plt.hist(longitudes,bins=10)
    plt.title("Distribucion de longitud de lineas")
    plt.xlabel("Cantidad de caracteres")
    plt.ylabel("Numero de lineas")
    plt.savefig("outputs/histograma_lineas.png")
    plt.show()
def grafico_linea(datos):
    columnas = list(datos[0].keys())
    print("\nColumnas disponibles:")
    print(columnas)
    columna_x = input("Columna X: ")
    columna_y = input("Columna Y: ")
    x = []
    y = []
    for fila in datos:
        try:
            x.append(fila[columna_x])
            y.append(float(fila[columna_y]))
        except:
            pass
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title("Evolucion temporal")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.xticks(rotation=45)
    plt.savefig("outputs/linea.png")
    plt.show()
def grafico_pastel(datos):
    columnas = list(datos[0].keys())
    print(columnas)
    columna = input("Columna categorica: ")
    categorias = {}
    for fila in datos:
        valor = fila.get[columna]
        if valor in categorias:
            categorias[valor] += 1
        else:
            categorias[valor] = 1
    etiquetas = list(categorias.keys())
    valores = list(categorias.values())
    plt.figure(figsize=(8, 8))
    plt.pie(valores,labels=etiquetas,autopct="%1.1f%%")
    plt.title("Comparacion categorica")
    plt.savefig("outputs/pastel.png")
    plt.show()
def grafico_scatter(datos):
    columnas = list(datos[0].keys())
    print(columnas)
    columna_x = input("Columna numerica X: ")
    columna_y = input("Columna numerica Y: ")
    x = []
    y = []
    for fila in datos:
        try:
            x.append(float(fila[columna_x]))
            y.append(float(fila[columna_y]))
        except:
            pass
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y)
    plt.title("Correlacion de variables")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.savefig("outputs/scatter.png")

    plt.show()