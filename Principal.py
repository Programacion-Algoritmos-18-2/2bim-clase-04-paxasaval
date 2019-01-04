from archivos.MiArchivo import *
from modelado.Mimodelo import *

f = ReadFichero() # iniciamos el lector del fichero con nombre f
f2= WriteFichero() # iniciamos la escritura del fichero con nnombre f2

lista = f.obtener_informacion() # agregamos al informacion del fichero al arreglo lista
lista = [l.split("|") for l in lista] #  por cada posicion del arreglo lista realizamos un split con el carater especial "|"
lista_equipos = []

for o in lista: # recorremos cada posicion de la lista bajo el nombre de o (recuerde que o es el arreglo del split "|")
    e = Equipo(o[0], o[1], o[2], o[3]) # tTomamos la informacion de cada posicion del arreglo o y la ingresamos en el constructor de ALUMNO
    lista_equipos.append(e)
f.cerrar_archivo() # cerramso el fichero  de lectura

opcion = input("Escriba(Nombre) para ordenar la lista por el nombre del equipo o (Campeonatos) para ordenar por el numero de campeonatos obtenido: ")
operacion = Operaciones(lista_equipos) # creamos una nueva variable con la clase-objeto Operaciones dandodel de entrada la lista de equipos
lista_equipos = operacion.ordenar(opcion) # Imprimimos la lsita ordenada mediante el metodo ordenar
for o in lista_equipos: # Recorresmos la lsita equipos ya ordenada
    f2.agregar_informacion(o) # Agregamos la informacion al segundo fichero
f2.cerrar_archivo() # cerramos el fichero de escritura