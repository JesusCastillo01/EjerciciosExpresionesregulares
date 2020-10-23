# encoding: utf-8
import re
print("\n\"Detección de correos electrónicos\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("coincidencias encontradas:")
for i in range(len(splitValues)):
    if(re.search("^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$",splitValues[i])):
        if(i==0):
            print("Coincidencias encontradas:")
        try:
            print(re.search("^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$",splitValues[i]).group())
        except AttributeError:
            print(re.search("^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$",splitValues[i]))
            archivo.close()