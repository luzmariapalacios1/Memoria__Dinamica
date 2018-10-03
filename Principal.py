__author__='LuzMari Palacios'

from Memoria_Dinamica import *
lista = []
tiendadecosmetico = ['labial', 'corrector', 'sombras', 'prochas', 'liniador']
precios = [50, 60, 50, 55, 30]

listas = MemoriaDinamica(tiendadecosmetico)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.recorrerArreglo()
listas.imprimirLista()
listas.agregarelementoarray('luminador')
listas.imprimirLista()
listas.eliminarElemento('sombras')
listas.imprimirLista()
lista2 = MemoriaDinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(20)
lista2.imprimirLista()