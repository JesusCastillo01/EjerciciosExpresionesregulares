# encoding: utf-8
import re
print("\n\"Detección de códigos postales\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("coincidencias encontradas:")
for i in range(len(splitValues)):
    if(re.search("[0-9]{5}",splitValues[i])):
        if(i==0):
            print("coincidencias encontradas:")
        try:
            print(re.search("[0-9]{5}",splitValues[i]).group())
        except AttributeError:
            print(re.search("[0-9]{5}",splitValues[i]))
            archivo.close()