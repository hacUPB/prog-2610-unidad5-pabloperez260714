from collections import Counter


def leer_texto(ruta):

    try:

        with open(
            ruta,
            "r",
            encoding="utf-8"
        ) as archivo:

            lineas = archivo.readlines()

        return lineas

    except FileNotFoundError:

        print(
            "Archivo TXT no encontrado."
        )

        return []


def resumen_texto(lineas):

    texto = "".join(lineas)

    total_lineas = len(lineas)

    total_palabras = len(
        texto.split()
    )

    caracteres_con_espacios = len(
        texto
    )

    caracteres_sin_espacios = len(
        texto.replace(
            " ",
            ""
        )
    )

    conectores = [
        "de", "la", "el",
        "y", "en", "a",
        "que", "los",
        "las", "un",
        "una"
    ]

    palabras = texto.lower().split()

    palabras_filtradas = []

    for palabra in palabras:

        palabra = palabra.strip(
            ".,;:!?()[]{}"
        )

        if palabra not in conectores:

            palabras_filtradas.append(
                palabra
            )

    contador = Counter(
        palabras_filtradas
    )

    print(
        "\n===== RESUMEN DEL TEXTO ====="
    )

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
        "\nTop 5 palabras más frecuentes:"
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

    errores = 0

    for linea in lineas:

        if (
            "ERROR"
            in linea.upper()
            or "404"
            in linea
        ):

            errores += 1

    print(
        "\nErrores encontrados:",
        errores
    )


def menu_textos(ruta):

    lineas = leer_texto(
        ruta
    )

    if len(lineas) == 0:
        return

    resumen_texto(
        lineas
    )

    extraer_patrones(
        lineas
    )