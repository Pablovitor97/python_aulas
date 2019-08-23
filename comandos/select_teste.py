print("refazendo")

import random
import time
def select_sort(v):
    i = 0 #contador
    while i < len(v) - 1: # porq o i vai percorrer ate a ultima casa do vetor
        menor = i # porq ele sempre vai querer ver o ultio elemento
        j = i - 1
        #embusca do menor elemento
        while j < len(v): # verifica o menor e confirma
            if v[j] < v[menor]:
                menor = j
                
            j += 1
            # verificar se precisa realizar a troca, so precisara realizar isso se o menor estiver na posição diferente do i
        if menor != i: # a gente faz a troca
            temp = v[i] # variavel temporaria
            v[i] = v[menor]
            v[menor] = temp
            
            
        i += 1
        
vetor =  list(range(0, 110))
random.shuffle(vetor) # desarrumar o vetor, se tirar isso ira ficr arrumado
antes = time.time()
select_sort(vetor)
depois = time.time()
total = (antes-depois)* 1000

print(vetor) # se tirar isso, vai aparecer o total de ordem
print('+='*20)
print("o tempo total para orderdar é: %0.2f ms" %total) # variavel total tem essa informação

            
            
            
            
                