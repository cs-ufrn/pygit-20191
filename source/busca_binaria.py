""" Retorna a posição do elemento na lista """
def busca_binaria(lista, elemento):
	try:
		lista_v = list(lista)
	except ValueError:
		print("The arg lista can not be parse to a type list")
	
	l=0
	r=len(lista_v)-1

	while(r >= l):	
		middle = r+l//2
		if(lista_v[middle] == elemento):
			return middle
		elif(lista_v[middle] < elemento):
			l = middle +1
		else:
			r = middle - 1
	return -1
