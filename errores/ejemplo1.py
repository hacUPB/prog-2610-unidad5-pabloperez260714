try:     # el try se intentar ejecutar una parte de codigo que puede dar error
    valor = int(input("ingrese un valor numerico:"))
except ValueError:   ## el except funciona como prueba para salir del try
    print("el valor ingresado no es un numero")
else: 
    resultado = valor / 10
    print(f"Resultado ={resultado}")
finally: 
    print("proceso ejecutado")
    