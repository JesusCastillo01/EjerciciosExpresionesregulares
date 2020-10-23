# encoding: utf-8
import re
print("\n\"Las palabras que tengan una longitud de 7 letras o más\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
for i in range(len(splitValues)):
    if(re.search("\D[\w]{7,}",splitValues[i])):
        if(i==0):
            print("Coincidencias Encontradas:")
        try:
            print(re.search("\D[\w]{7,}",splitValues[i]).group())
        except AttributeError:
            print(re.search("\D[\w]{7,}",splitValues[i]))
            archivo.close()