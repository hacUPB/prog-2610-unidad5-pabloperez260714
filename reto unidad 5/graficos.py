import matplotlib.pyplot as plt


def grafico_palabras(contador):

    palabras = []
    frecuencias = []

    top10 = contador.most_common(10)

    for palabra, cantidad in top10:

        palabras.append(
            palabra
        )

        frecuencias.append(
            cantidad
        )

    plt.figure(figsize=(8, 5))

    plt.barh(
        palabras,
        frecuencias
    )

    plt.title(
        "Frecuencia de palabras"
    )

    plt.xlabel(
        "Frecuencia"
    )

    plt.ylabel(
        "Palabras"
    )

    plt.savefig(
        "outputs/frecuencia_palabras.png"
    )

    plt.show()


def grafico_histograma(lineas):

    longitudes = []

    for linea in lineas:

        longitudes.append(
            len(linea)
        )

    plt.figure(figsize=(8, 5))

    plt.hist(
        longitudes,
        bins=10
    )

    plt.title(
        "Distribucion de longitud de lineas"
    )

    plt.xlabel(
        "Cantidad de caracteres"
    )

    plt.ylabel(
        "Numero de lineas"
    )

    plt.savefig(
        "outputs/histograma_lineas.png"
    )

    plt.show()