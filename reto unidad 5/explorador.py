import os


def explorar_directorio(ruta):

    try:

        ruta_completa = os.path.join(
            os.path.dirname(__file__),
            ruta
        )

        archivos = os.listdir(
            ruta_completa
        )

        archivos_txt = []
        archivos_csv = []

        for archivo in archivos:

            if archivo.endswith(".txt"):
                archivos_txt.append(
                    archivo
                )

            elif archivo.endswith(".csv"):
                archivos_csv.append(
                    archivo
                )

        print(
            "\n archivos txt"
        )

        for txt in archivos_txt:
            print(txt)

        print(
            "\n archivos csv"
        )

        for csv in archivos_csv:
            print(csv)

    except FileNotFoundError:

        print(
            "La carpeta no existe."
        )