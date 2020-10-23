# encoding: utf-8
import re
print("\n\"Detección de URL's\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("coincidencias encontradas:")
for i in range(len(splitValues)):
    if(re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$",splitValues[i])):
        if(i==0):
            print("coincidencias encontradas:")
        try:
            print(re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$",splitValues[i]).group())
        except AttributeError:
            print(re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$",splitValues[i]))
            archivo.close()