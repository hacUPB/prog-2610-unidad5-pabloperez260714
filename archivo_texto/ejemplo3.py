'''
1. leer el nuevo archivo
2. leer todo el archivo en forma de lista
3. imprimir la primera letra de cada linea
'''
fp = open(".\\archivo_texto\\word.txt", "r", encoding="utf-8") #el doble back slash es para poder ubir el archivo

lista = fp.readlines()
fp.close
print(lista)
for linea in lista:
    print(lista[0])
    