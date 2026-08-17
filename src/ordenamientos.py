"""
Módulo de Algoritmos de Ordenamiento
Autor: Felipe Larrañaga
Descripción: Implementa algoritmos de ordenamiento: burbuja, selección e inserción
"""


class Ordenamiento:
    """Clase que implementa diferentes algoritmos de ordenamiento"""

    @staticmethod
    def ordenamiento_burbuja(lista, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento de burbuja
        Parámetros:
            lista: lista a ordenar
            ascendente: bool, True para orden ascendente, False para descendente
        Retorna: lista ordenada
        """
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if ascendente:
                    if lista[j] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
                else:
                    if lista[j] < lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    @staticmethod
    def ordenamiento_seleccion(lista, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento por selección
        Parámetros:
            lista: lista a ordenar
            ascendente: bool, True para orden ascendente, False para descendente
        Retorna: lista ordenada
        """
        n = len(lista)
        for i in range(n):
            indice_min = i
            for j in range(i + 1, n):
                if ascendente:
                    if lista[j] < lista[indice_min]:
                        indice_min = j
                else:
                    if lista[j] > lista[indice_min]:
                        indice_min = j
            lista[i], lista[indice_min] = lista[indice_min], lista[i]
        return lista

    @staticmethod
    def ordenamiento_insercion(lista, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento por inserción
        Parámetros:
            lista: lista a ordenar
            ascendente: bool, True para orden ascendente, False para descendente
        Retorna: lista ordenada
        """
        for i in range(1, len(lista)):
            clave = lista[i]
            j = i - 1
            while j >= 0:
                if ascendente:
                    if lista[j] > clave:
                        lista[j + 1] = lista[j]
                        j -= 1
                    else:
                        break
                else:
                    if lista[j] < clave:
                        lista[j + 1] = lista[j]
                        j -= 1
                    else:
                        break
            lista[j + 1] = clave
        return lista
