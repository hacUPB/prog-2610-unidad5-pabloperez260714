import csv
from graficos import (
    grafico_linea,
    grafico_pastel,
    grafico_scatter
)


def leer_csv(ruta):
    """
    Lee un archivo CSV
    """

    datos = []

    try:
        with open(
            ruta,
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(
                archivo
            )

            for fila in lector:
                datos.append(fila)

        return datos

    except FileNotFoundError:
        print(
            "Error: archivo CSV no encontrado."
        )
        return []


def vista_previa(datos):
    """
    Muestra primeras 10
    y últimas 5 filas
    """

    print(
        "\n===== PRIMERAS 10 FILAS ====="
    )

    for fila in datos[:10]:
        print(fila)

    print(
        "\n===== ÚLTIMAS 5 FILAS ====="
    )

    for fila in datos[-5:]:
        print(fila)


def estadisticas(datos, columna):
    """
    Calcula estadísticas
    descriptivas
    """

    numeros = []

    for fila in datos:

        valor = fila[columna]

        if valor != "":

            try:
                numeros.append(
                    float(valor)
                )

            except ValueError:
                pass

    if len(numeros) == 0:
        print(
            "No hay datos numéricos."
        )
        return

    numeros.sort()

    promedio = (
        sum(numeros)
        / len(numeros)
    )

    n = len(numeros)

    if n % 2 == 0:

        mediana = (
            numeros[n // 2 - 1]
            + numeros[n // 2]
        ) / 2

    else:
        mediana = numeros[
            n // 2
        ]

    print(
        "\n===== ESTADÍSTICAS ====="
    )

    print(
        "Registros válidos:",
        len(numeros)
    )

    print(
        "Promedio:",
        promedio
    )

    print(
        "Mediana:",
        mediana
    )

    print(
        "Máximo:",
        max(numeros)
    )

    print(
        "Mínimo:",
        min(numeros)
    )


def menu_csv(ruta):
    """
    Menú principal CSV
    """

    datos = leer_csv(ruta)

    if len(datos) == 0:
        return

    vista_previa(datos)

    print(
        "\nColumnas disponibles:"
    )

    print(
        list(
            datos[0].keys()
        )
    )

    columna = input(
        "\nIngrese una "
        "columna numérica: "
    )

    estadisticas(
        datos,
        columna
    )

    grafico_linea(
        datos
    )

    grafico_pastel(
        datos
    )

    grafico_scatter(
        datos
    )