from explorador import (
    explorar_directorio
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
            print(
                "Procesar TXT"
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