import csv

from graficos import (
    grafico_linea,
    grafico_pastel,
    grafico_scatter
)


def leer_csv(ruta):

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
                datos.append(
                    fila
                )

        return datos

    except FileNotFoundError:

        print(
            "Archivo csv no encontrado."
        )

        return []


def vista_previa(datos):

    print(
        "\n===== primeras 10 filas ====="
    )

    for fila in datos[:10]:
        print(fila)

    print(
        "\n===== ultimas 5 filas ====="
    )

    for fila in datos[-5:]:
        print(fila)


def estadisticas(datos, columna):

    numeros = []

    for fila in datos:

        valor = fila.get(
            columna,
            ""
        )

        if valor != "":

            try:

                numeros.append(
                    float(valor)
                )

            except ValueError:
                pass

    if len(numeros) == 0:

        print(
            "No hay datos numericos."
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
        "\n===== estadisticas ====="
    )

    print(
        "Registros validos:",
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
        "Maximo:",
        max(numeros)
    )

    print(
        "Minimo:",
        min(numeros)
    )


def menu_csv(ruta):

    datos = leer_csv(
        ruta
    )

    if len(datos) == 0:
        return

    vista_previa(
        datos
    )

    print(
        "\nColumnas disponibles:"
    )

    columnas = list(
        datos[0].keys()
    )

    print(columnas)

    columna = input(
        "\nIngrese columna numerica: "
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