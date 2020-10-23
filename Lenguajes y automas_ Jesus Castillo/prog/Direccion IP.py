# encoding: utf-8
import re
print("\n\"Detección de direcciones IP\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues =linea.split(" ")
print("coincidencias encontradas:")
for i in range(len(splitValues)):
    if(re.search(".*(\d+\.\d+\.\d+).*",splitValues[i])):
        if(i==0):
            print("coincidencias encontradas:")
        try:
            print(re.search(".*(\d+\.\d+\.\d+).*",splitValues[i]).group())
        except AttributeError:
            print(re.search(".*(\d+\.\d+\.\d+).*",splitValues[i]))
            archivo.close()