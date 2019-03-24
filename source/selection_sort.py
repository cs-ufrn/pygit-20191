""" Retorna uma lista ordenada, utilizando o algoritmo selection sort """
def selection_sort(alist):
   for preencherLocal in range(len(alist)-1,0,-1):   #for que inicia do último elemento da lista e volta até o primeiro
       posicaoDeMaximo=0				  #Max =0 é o indice do primeiro elemento, considerado máximo
       for local in range(1,preencherLocal+1):	  # for que vai do segundo elemento até o elemento seguinte de fillslot
           if alist[local]>alist[posicaoDeMaximo]:  #condicional para dizer qual elemento é o maior
               posicaoDeMaximo = local		     #caso atendido, o índice do máximo é atualizado
       alist[posicaoDeMaximo],alist[preencherLocal] = alist[preencherLocal], alist[posicaoDeMaximo]	#após encontrado, posições são trocadas: elemento máximo com a maior posição determinada pelo fillslot (será a maior posição não ordenada)

