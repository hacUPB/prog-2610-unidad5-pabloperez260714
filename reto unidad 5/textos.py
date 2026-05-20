from collections import Counter
from graficos import (
    grafico_palabras,
    histograma_lineas
)


def leer_texto(ruta):
    """
    Lee un archivo txt y devuelve sus líneas
    """

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        return lineas

    except FileNotFoundError:
        print("Error: archivo TXT no encontrado.")
        return []


def resumen_estadistico(lineas):
    """
    Calcula estadísticas del texto
    """

    texto = "".join(lineas)

    total_lineas = len(lineas)
    total_palabras = len(texto.split())
    caracteres_con_espacios = len(texto)
    caracteres_sin_espacios = len(
        texto.replace(" ", "")
    )

    conectores = [
        "de", "la", "el", "y",
        "a", "en", "que", "los",
        "las", "un", "una",
        "por", "con"
    ]

    palabras = texto.lower().split()

    palabras_filtradas = []

    for palabra in palabras:

        palabra = palabra.strip(
            ".,;:!?()[]{}\"'"
        )

        if palabra not in conectores:
            palabras_filtradas.append(
                palabra
            )

    contador = Counter(
        palabras_filtradas
    )

    print("\n===== RESUMEN DEL TEXTO =====")

    print(
        "Cantidad de líneas:",
        total_lineas
    )

    print(
        "Cantidad de palabras:",
        total_palabras
    )

    print(
        "Caracteres con espacios:",
        caracteres_con_espacios
    )

    print(
        "Caracteres sin espacios:",
        caracteres_sin_espacios
    )

    print(
        "\nTop 5 palabras más repetidas:"
    )

    top5 = contador.most_common(5)

    for palabra, cantidad in top5:
        print(
            palabra,
            "-",
            cantidad
        )

    return contador


def extraer_patrones(lineas):
    """
    Busca ERROR o 404
    """

    errores = 0

    for linea in lineas:

        if (
            "ERROR" in linea.upper()
            or "404" in linea
        ):
            errores += 1

    print(
        "\nCantidad de errores encontrados:",
        errores
    )


def menu_textos(ruta):
    """
    Función principal TXT
    """

    lineas = leer_texto(ruta)

    if len(lineas) == 0:
        return

    contador = resumen_estadistico(
        lineas
    )

    extraer_patrones(lineas)

    grafico_palabras(contador)

    longitudes = []

    for linea in lineas:
        longitudes.append(
            len(linea)
        )

    histograma_lineas(
        longitudes
    )