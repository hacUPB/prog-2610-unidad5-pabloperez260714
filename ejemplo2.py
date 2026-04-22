fp = open("texto.txt", "r")
datos_1 = fp.read(5)
print("Primera lectura:", datos_1)

datos_2 = fp.read(5)
print("Segunda lectura:", datos_2)
fp.close()