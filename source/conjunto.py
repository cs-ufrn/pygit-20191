""" Insere um elemento no conjunto, caso ele não exista """
def insert(conjunto, elemento):
	conjunto.append(elemento)
        return conjunto

""" Remove um elemento no conjunto, caso ele exista """
def remove(conjunto, elemento):
	conjunto.remove(elemento)
        return conjunto

""" Verifica se um elemento existe no conjunto """
def exists(conjunto, elemento):
	return elemento in conjunto

