print('-----#################### FUNÇÃO ####################-----')

# PARA QUE USAMOS A 'FUNÇÃO'?
# %%REALIZAÇÃO DE CODIGOS E MODULARIZAÇÃO..%%


   ## TIPOS DE FUNÇÕES:
        # FUNÇÕES INTERNAS E FUNÇÕES DEFINIDAS PELO USUARIO

"""def<nome_função>(argumentos)
    <instruções>"""


'''def mensagem():
    print("Pablo Vitorino A.")

mensagem()


##      
print('-----> CRIANDO FUNÇÕES EM PAYTHON COM ARGUMNETOS<-----')
## SOMAR NUMEROS

x = 30
y = 40
def soma(a,b):
    return a + b;  # return : retornat pra quem chamou a função..

r = soma(x, y)
print(r)

print('# --------------------------------------------------------------------')
 print(>>>>>"""EU ACHO QUE É FUNÇÃO SIMPLES"""<<<<<)
### intrução "RETURN":

  # def<nome_instrução>(argumentos)
    #<instrução>
    #return<valor>


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def quadrado(valores):
    quadrado = []
    for x in valores:
        quadrado.append(x/2)
    return quadrado
    
resultados = quadrado(valores)

for y in resultados:  #se eu não criasse esse, não iriaa aparecer os resultados
    print(y)

    
print('## -----------------------------------------------------------------------##')


""" FUNÇÕES >>>> ESCOPO DAS VARIAVEIS >>> """

# O ESCOPO DAS VARIAVEIS INDICA SUA VISIBILIDADE - ONDE, NO CODIGO
  #, A VARIAVEL É ACESSIVEL.

# EXISTE DOIS TIPOS:
""" ESCOPO GLOBAL
ESCOPO LOCAL """



print(' >>>>>>>>> MAIS EXEMPLOS >>>>>>>>>>')
# DECÇLARAÇÃO

def declaracao():
    nome = input('coloque um nome: ')
    idade = int(input('coloque a idade: '))
    cpf = int(input('coloque o seu CPF: '))
    
    print(nome, 'tem a idade: ', idade,' e o seu CPF:', cpf, 'n\Proximo!!!\n')
    

declaracao()
declaracao()






print(' >>>>>>>>>>>> ESCORPO GLOBAL >>>>>>>>>>>>>>>>>>>')'''



print("..........^^^..........")

# lista = []
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos *= 1
valores = [10, 2, 4, 5, 8, 9, 6]
dobra(valores)     # vai criar uma lista valores e passar la p cima que e a lista
print(valores)     # ele vai dobrar os numeros da valores

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"somando os valores {valores} temos {s}")

soma(5, 2)
soma(2, 9, 4)



    
        
   
