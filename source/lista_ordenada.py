""" Insere um elemento na lista """
def insert(lista, elemento):
	for i, value in enumerate(lista):
		if(value > elemento):
			lista.insert(i, elemento)
			return lista
	
	lista.append(elemento)
	return lista

""" Remove um elemento na lista """
def remove(lista, elemento):
	lista.remove(elemento)
	return lista

""" Busca um elemento na lista e retorne a sua posição """
def find(lista, elemento):
	for i, value in enumerate(lista):
		if(elemento == value):
			return i
	return -1
