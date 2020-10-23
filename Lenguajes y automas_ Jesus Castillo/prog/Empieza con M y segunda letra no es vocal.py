# encoding: utf-8
import re
print("\n\"Las palabras que inicien con \"M\" donde la segunda letra NO sea una vocal\".")
archivo = open("texto.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues = linea.split(" ")
print("Expresiones Encontradas:")
for i in range(len(splitValues)):
    if(re.search("^[Mm]([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]).*",splitValues[i])):
        if(i==0):
            print("Coincidencias Encontradas:")
        try:
            print(re.search("^[Mm]([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]).*",splitValues[i]).group())
        except AttributeError:
            print(re.search("^[Mm]([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]).*",splitValues[i]))
            archivo.close()