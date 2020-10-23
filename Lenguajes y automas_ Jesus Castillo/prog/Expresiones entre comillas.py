# encoding: utf-8
import re, os, sys
print("\n\"Expresiones encerradas entre comillas\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("Expresiones encontradas:")
for i in range(len(splitValues)):
    if(re.search("('.*')|(\".*\")*",splitValues[i])):
        if(i==0):
            print("Coincidencias encontradas:")
        try:
            print(re.search("('.*')|(\".*\")*",splitValues[i]).group())
        except AttributeError:
            print(re.search("('.*')|(\".*\")*",splitValues[i]))
            archivo.close() 