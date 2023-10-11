import sys

cadena = sys.argv[1]
archivo = open("basededatos.txt",'a')
archivo.write(cadena+"\n")
archivo.close()
