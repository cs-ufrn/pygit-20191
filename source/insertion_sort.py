""" Retorna uma lista ordenada, utilizando o algoritmo insertion sort """
def insertion_sort(lista):
	for j in range(1,len(lista)):
		elemento = lista[j]
		i = j-1
		while (i>=0 and lista[i] > elemento):
			lista[i+1] = lista[i]
			i = i-1
		lista[i+1] = elemento
	return lista
