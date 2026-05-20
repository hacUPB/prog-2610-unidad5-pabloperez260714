from explorador import (
    explorar_directorio
)

from textos import (
    menu_textos
)

from csv_analisis import (
    menu_csv
)


def menu_principal():

    while True:

        print(
            "\n menu principal"
        )

        print(
            "1. Explorar directorio"
        )

        print(
            "2. Procesar textos"
        )

        print(
            "3. Analizar csv"
        )

        print(
            "4. Salir"
        )

        opcion = input(
            "Seleccione una opcion: "
        )

        if opcion == "1":

            ruta = "data"

            explorar_directorio(
                ruta
            )

        elif opcion == "2":

            archivo = input(
                "Ingrese el nombre del txt: "
            )

            ruta = f"data/{archivo}"

            menu_textos(
                ruta
            )

        elif opcion == "3":

            archivo = input(
                "Ingrese el nombre del csv: "
            )

            ruta = f"data/{archivo}"

            menu_csv(
                ruta
            )

        elif opcion == "4":

            print(
                "Saliendo..."
            )

            break

        else:

            print(
                "Opcion invalida"
            )


menu_principal()