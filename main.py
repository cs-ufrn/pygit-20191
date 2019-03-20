"""
Testes das bibliotecas implementadas pelos candidatos.
"""

from source import deque, conjunto, busca_binaria, lower_bound, upper_bound, insertion_sort, selection_sort, merge, lista_ordenada, funcional, funcional_zip

# Issue 1
print("#1: DEQUE")
print(deque.push_front([1,2], 3) == [3, 1, 2])
print(deque.push_back([1,2], 3) == [1, 2, 3])
print(deque.front([2,5,1,20]) == 2)
print(deque.back([2,5,1,100]) == 100)
print(deque.pop_front([2,5,1,100]) == [5, 1, 100])
print(deque.pop_back([2,5,1,100]) == [2, 5, 1])

# Issue 2
print("#2: CONJUNTO")
print(conjunto.insert([1, 2], 3) == [1, 2, 3])
print(conjunto.insert([1, 2, 3], 3) == [1, 2, 3])
print(conjunto.remove([1, 2, 3], 2) == [1, 3])
print(conjunto.exists([3, 2, 1], 2) == True)
print(conjunto.exists([3, 2, 1], 10) == False)
print(conjunto.exists([], 10) == False)

# Issue 3
print("#3: BUSCA BINÁRIA")
print(busca_binaria.busca_binaria([1, 2, 3, 5], 2) == 1)
print(busca_binaria.busca_binaria([1, 2, 3, 5], 0) == -1)
print(busca_binaria.busca_binaria([1, 2, 3, 5], 6) == -1)
print(busca_binaria.busca_binaria([1, 2, 3, 5], 1) == 0)
print(busca_binaria.busca_binaria([1, 2, 3, 5], 5) == 3)

# Issue 4
print("#4: LOWER BOUND")
print(lower_bound.lower_bound([1, 2, 3, 5], 6) == 3)
print(lower_bound.lower_bound([1, 2, 3, 5], 2) == 1)
print(lower_bound.lower_bound([1, 2, 3, 5], 0) == -1)
print(lower_bound.lower_bound([1, 2, 3, 5], 2) == 1)

# Issue 5
print("#5: UPPER BOUND")
print(upper_bound.upper_bound([1, 2, 3, 5], 6) == -1)
print(upper_bound.upper_bound([1, 2, 3, 5], 1) == 1)
print(upper_bound.upper_bound([1, 2, 3, 5], 4) == 3)
print(upper_bound.upper_bound([1, 2, 3, 5], 2) == 2)

# Issue 6
print("#6: INSERTION")
print(insertion_sort.insertion_sort([4, 3, 2, 1]) == [1, 2, 3, 4])
print(insertion_sort.insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4])
print(insertion_sort.insertion_sort([2, 1, 3, 4]) == [1, 2, 3, 4])

# Issue 7
print("#7: SELECTION")
print(selection_sort.selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4])
print(selection_sort.selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4])
print(selection_sort.selection_sort([2, 1, 3, 4]) == [1, 2, 3, 4])

# Issue 8
print("#8: MERGE")
print(merge.merge([1, 2, 3], [8, 9, 10]) == [1, 2, 3, 8, 9, 10])
print(merge.merge([1, 2, 3], [1, 2]) == [1, 1, 2, 2, 3])
print(merge.merge([1], [1, 2]) == [1, 1, 2])
print(merge.merge([],[]) == [])

# Issue 9
print("#9: LISTAS ORDENADAS")
print(lista_ordenada.insert([1, 2, 3], 4) == [1, 2, 3, 4])
print(lista_ordenada.remove([1, 2, 3], 2) == [1, 3])
print(lista_ordenada.find([1, 2, 3], 2) == 1)
print(lista_ordenada.find([1, 2, 3], 4) == -1)

# Issue 10
print("#10: PYTHON FUNCIONAL (TAKE, MAP, FILTER)")
print(funcional.take([4, 2, 3, 1], 2) == [4, 2])
print(funcional.map([1, 2, 3, 4], lambda x: x + 1) == [2, 3, 4, 5])
print(funcional.filter([1, 2, 3, 4], lambda x: x > 3) == [4])

# Issue 11
print("#11: PYTHON FUNCIONAL (ZIP, UNZIP, ZIPWITH)")
print(funcional_zip.zip([1, 2, 3, 4], [5, 6, 7, 8]) == [(1, 5), (2, 6), (3, 7), (4, 8)])
print(funcional_zip.unzip([(1, 5), (2, 6), (3, 7), (4, 8)]) == ([1, 2, 3, 4],[5, 6, 7, 8]))
print(funcional_zip.zipwith([1, 2, 3, 4], [5, 6, 7, 8], lambda x, y : x + y) == [6, 8, 10, 12])
