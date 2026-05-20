from explorador import (
    explorar_directorio
)

from textos import (
    menu_textos
)


def menu_principal():

    while True:

        print(
            "\n===== MENU PRINCIPAL ====="
        )

        print(
            "1. Explorar directorio"
        )

        print(
            "2. Procesar Bitácoras / Textos (.txt)"
        )

        print(
            "3. Analizar Dataset (.csv)"
        )

        print(
            "4. Salir"
        )

        opcion = input(
            "Seleccione una opción: "
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

            print(
                "Analizar CSV"
            )

        elif opcion == "4":

            print(
                "Saliendo..."
            )

            break

        else:

            print(
                "Opción inválida"
            )


menu_principal()