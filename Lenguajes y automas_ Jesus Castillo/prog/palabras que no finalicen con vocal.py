# encoding: utf-8
import re
print("\n\"Expresiones que NO finalicen con una vocal\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
for i in range(len(splitValues)):
    if(re.search(".*([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z])+$",splitValues[i])):
        if(i==0):
            print("Expresiones encontradas:")
        try:
            print(re.search(".*([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z])+$",splitValues[i]).group())
        except AttributeError:
            print(re.search(".*([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z])+$",splitValues[i]))
            archivo.close()