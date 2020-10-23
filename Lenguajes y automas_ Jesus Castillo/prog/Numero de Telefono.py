# encoding: utf-8
import re
print("\n\"Detección de números de teléfono en México\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("Expresiones encontradas:")
for i in range(len(splitValues)):
    if(re.search("(^9[0-9]{9})",splitValues[i])):
        if(i==0):
            print("Expresiones encontradas:")
        try:
            print(re.search("(^9[0-9]{9})",splitValues[i]).group())
        except AttributeError:
            print(re.search("(^9[0-9]{9})",splitValues[i]))
            archivo.close()