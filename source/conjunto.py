""" Verifica se um elemento existe no conjunto """
def exists(conjunto, elemento):
  return elemento in conjunto

""" Insere um elemento no conjunto, caso ele não exista """
def insert(conjunto, elemento):
  if(exists(conjunto, elemento) == False):
    conjunto.append(elemento)
    return conjunto
  else:
    return conjunto

""" Remove um elemento no conjunto, caso ele exista """
def remove(conjunto, elemento):
  if(exists(conjunto, elemento) == True):
    conjunto.remove(elemento)
    return conjunto
  else:
    return conjunto