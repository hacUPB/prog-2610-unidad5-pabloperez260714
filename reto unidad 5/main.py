from explorador import explorar_directorio
from textos import menu_textos
from csv_analisis import menu_csv
def menu_principal():

    while True:
        print("\n===== EXPLORADOR CLI DE DATOS =====")
        print("1. Explorar directorio")
        print("2. Procesar Bitácoras / Textos (.txt)")
        print("3. Analizar Dataset (.csv)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta = input(
                "Ingrese la ruta "
                "(ejemplo: data): "
            )

            explorar_directorio(ruta)

        elif opcion == "2":
            archivo = input(
                "Ingrese el nombre "
                "del TXT: "
            )

            ruta = f"data/{archivo}"

            menu_textos(ruta)

        elif opcion == "3":
            archivo = input(
                "Ingrese el nombre "
                "del CSV: "
            )

            ruta = f"data/{archivo}"

            menu_csv(ruta)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


menu_principal()