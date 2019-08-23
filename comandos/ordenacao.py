print("----------SELECTSORT----------") # é encontar exatamente quem é o menor elennto
import random
import time

def selection_sort(v): 
    i = 0 # contador
    while i < len(v) - 1:  # porq menos um? porq o i não vai percorrer ate a ultima casa do vetor, vai ate a penultima, indica o menor elennto 
        menor = i # ele sempre quer saber qual o menor elemnto
        j = i + 1
        # embusca do menor elemento
        while j < len(v): # essa verifica o menor, confirma
            if v[j] < v[menor]:
                menor = j
                
            j += 1
         #verifica se precisda realizar a troca;  so precia realizar a trocam se o menor estiver na oposiição diferente do i   
        if menor != i: # a gente faz a troca
            temp = v[i] # variavel temporaria
            v[i] = v[menor]
            v[menor] = temp
            
        i +=1
         
vetor = list(range(0,109))
random.shuffle(vetor) # dembaralhar o vetor, SE TIRAR ISSO, FICA ORDENADO
antes = time.time()
selection_sort(vetor)
depois = time.time()
total = (depois-antes)*1000

print(vetor)  # se tirar isso, aparece o total de ordem
print("o tempo total para ordenar: %0.2f ms" % total) # variavel total tem essa informacao



print('-='*20)



print("----------MergeSort----------") # vetor desordenado
# tenho dois subvetores desorganizados, esse programa vai intercalando ele
# e colocando na posição correta

import random # 1isso
import time
def mergesort(v, p, r): # v = vetor, p = posição inicial q = meio r = fim
    # condição de parada. apartir do momento em que p < f for falso(condição de existencia)
    if p < r:
        q = (p + r) // 2 # p + r é a posição do elemmto do meio
        mergesort(v, p, q) # a posição final mudou, agora é Q # quebrando o vetor em subvetor 1,(metade da esquerda)
        mergesort(v, q + 1, r) # quebrando o vetor em subvetor 2(metade da direita)
        intercalar(v, p, q, r)  # intercalar é observar os elementos de 2 vetores e inter calando, quem é o menor
        
def intercalar(v, p, q, r):
    temp = v.copy() # copia do nosso vetor real
    i = p # contador do subvetor 1
    j = q + 1 # contador do subvetor 2
    k = p # contador do vetor real
    
# momento em que a intercalação sera realizada    
    while k <= r:
        if i > q:
            # entra quando nao tiver mais elementos no vetor 1
            v[k] = temp[j]
            j += 1
        elif j > r:
            # entrara quando nao tiver mais elementos no subvetor 2
            v[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            # neste caso, retira o elemento do sub vetor 1
            v[k] = temp[i]
            i += 1
        else:
            # nesse caso, retira o elemento do sub vetor 2
            v[k] = temp[i]
            j += 1
        
        k += 1
        
vetor = list(range(0, 2000))#1
random.shuffle(vetor)#1
antes = time.time()
mergesort(vetor, 0, len(vetor) - 1)
depois = time.time()
total = (depois-antes)*1000

print(vetor)#1 ate aqui, faz com que o resultado da função fique desorganizada

print("o tempo total foi: %0.2f ms" %total)

