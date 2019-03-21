""" Retorna uma lista contendo os ks primeiros elementos da lista """
def take(lista, k):
	listaks = []

	if k <= len(lista):
		listaks = lista[:k]
	else:
		listaks = lista[:]
	return listaks

""" Retorna uma lista contendo o resultado da aplicação da função 'f' em cada elemento da lista """
def map(lista, f):
	listaf = []
	
	for index in lista:
		listaf.append(f(index))

	return listaf

""" Retorna os elementos da lista que satisfaçam a função f """
def filter(lista, f):
	listaS = []
	
	for index in lista:
		if f(index) == True:
			listaS.append(index)

	return listaS
