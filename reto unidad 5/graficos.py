import matplotlib.pyplot as plt
from collections import Counter


def grafico_linea(datos):
    """
    Gráfico de línea
    """

    columnas = list(
        datos[0].keys()
    )

    print(
        "\nColumnas disponibles:"
    )

    print(columnas)

    columna_x = input(
        "Seleccione columna X: "
    )

    columna_y = input(
        "Seleccione columna Y: "
    )

    x = []
    y = []

    for fila in datos:

        try:
            x.append(
                fila[columna_x]
            )

            y.append(
                float(
                    fila[columna_y]
                )
            )

        except:
            pass

    plt.figure(figsize=(10, 5))

    plt.plot(x, y)

    plt.title(
        "Evolución Temporal"
    )

    plt.xlabel(
        columna_x
    )

    plt.ylabel(
        columna_y
    )

    plt.xticks(rotation=45)

    plt.savefig(
        "outputs/tendencia.png"
    )

    plt.show()


def grafico_pastel(datos):
    """
    Gráfico de pastel
    """

    columnas = list(
        datos[0].keys()
    )

    print(
        "\nColumnas disponibles:"
    )

    print(columnas)

    columna = input(
        "Seleccione columna categórica: "
    )

    categorias = []

    for fila in datos:
        categorias.append(
            fila[columna]
        )

    conteo = Counter(
        categorias
    )

    etiquetas = list(
        conteo.keys()
    )

    valores = list(
        conteo.values()
    )

    plt.figure(figsize=(8, 8))

    plt.pie(
        valores,
        labels=etiquetas,
        autopct="%1.1f%%"
    )

    plt.title(
        "Comparación Categórica"
    )

    plt.savefig(
        "outputs/pastel.png"
    )

    plt.show()


def grafico_scatter(datos):
    """
    Gráfico scatter
    """

    columnas = list(
        datos[0].keys()
    )

    print(
        "\nColumnas disponibles:"
    )

    print(columnas)

    columna_x = input(
        "Seleccione columna numérica X: "
    )

    columna_y = input(
        "Seleccione columna numérica Y: "
    )

    x = []
    y = []

    for fila in datos:

        try:
            x.append(
                float(
                    fila[columna_x]
                )
            )

            y.append(
                float(
                    fila[columna_y]
                )
            )

        except:
            pass

    plt.figure(figsize=(8, 5))

    plt.scatter(x, y)

    plt.title(
        "Correlación de Variables"
    )

    plt.xlabel(
        columna_x
    )

    plt.ylabel(
        columna_y
    )

    plt.savefig(
        "outputs/correlacion.png"
    )

    plt.show()