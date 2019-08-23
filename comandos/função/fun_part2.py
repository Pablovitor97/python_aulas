'''def mostralinha():
    print('--------------------')

mostralinha()
print('SISTEMA DE ALUNOS')
mostralinha()

mostralinha()
print('CADASTRO DE FUNCIONARIOS')
mostralinha()

mostralinha()
print('ERRO DE SISTEMA')
mostralinha()


# >>>>>>>>>>>>>>>>>>>>>>>>> "mais simplificado" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def lin():
    print('>'*50)   #<-------------------------------------¬

# Programa principal
lin()  # toda vez qye uso "lin()", ele vai colocar uma linha;
print(" Pablo vitorino ")
print(" aprenda Python ")
lin()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# FAZENDO QEU O COMANDO SEJA RECONHECIDO

def mensagem(txt):   # ROTINA.. COISAS QUE ACONTECEM CONSTANTEMENTE..
    print(">.<"*10)
    print(txt)
    print(">.<"*10)

# programa principal
mensagem(" PABLO VITORINO A. ")  
mensagem(" APRENDENDO A PROGRAMAR ")   # SE EU COLOCAR OUTRA PALAVRA AAQUI ELE VAI RODAR SEM PROBLEMAS
mensagem(" FUNÇÃO ")


""" ------------------------------------------------------"""
# PASSANDO PARAMETROS
print("-"*50)
###############
def soma(a, b):  # A SOMA ESTA RECEBENDO DOIS PARAMETROS, CASO EU QUISER COLOCAR UM NUMERO LA EM BAIXO, VAI DAR ERRO, PORQ ERA P SER DOIS E NÃO 1
    s = a + b
    print(s)
                # sempre deixe um espaço

#programa principal
soma(5, 6)
soma(6, 8)
soma(9, 2)

print('-'*20)

# >>>>>>>

def soma(a, b):
    print(f'A = {a} e B = {a}')  # O "F" É DE FORMAT!!
    s = a + b
    print(f'A soma de A + B = {s}')

# programa principal
soma(4, 6)
soma(a=5, b=10)
soma(b=3, a=9) # eu posso mudar a ordem


print('-'*20)

## EMPACOTADOR
## O " * " É O SIMBOLOD E DESEMPACOTAR
""" DEF CONTADOR(*NUM)"""

def contador(*num):
    print(num)

contador(1, 2, 3)
contador(4, 5)
contador(6, 7, 8, 9, 10)  # ele vai criar uam tupla..'''





# lista: []
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos *= 1

        
valores = [10, 2, 4, 5, 8, 9, 6]
dobra(valores)     # vai criar uma lista valores e passar la p cima(lista)
print(valores)     # ele vai dobrar os numeros da valores



 




