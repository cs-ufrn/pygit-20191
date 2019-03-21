
""" Insere um elemento no início do deque """
def push_front(deque, elemento):
	deque.insert(0, elemento)
	return deque
""" Insere um elemento ao final do deque """
def push_back(deque, elemento):
	deque.append(elemento)
	return deque

""" Retorna o elemento do início do deque """
def front(deque):
	return deque[0]

""" Retorna o elemento do final do deque """
def back(deque):
	return deque[-1]

""" Remove um elemento do início do deque """
def pop_front(deque):
	del deque[0]
	return deque
""" Remove um elemento do final do deque """
def pop_back(deque):
	deque.pop()
	return deque
