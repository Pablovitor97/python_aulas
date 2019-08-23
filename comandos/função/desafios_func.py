# desafios
#exercicio 96.. faça um programa que tenha uma função chamada area()
# que receba as dimensoes de um terreno retangular(largura e comprimento) e mostra a area do terreno.
def area(larg, comp):
    a = larg * comp
    print(f"a area de um terreno {larg} x {comp} e de {a}m².")
# ja é outra part
print("controle de terrenos")
print('-'* 20)
lar = float(input("largura (m): "))   # a variavel tem que ser diferente
com = float(input("comprimento (m): "))
area(lar, com)   
 
 
#exer 97..  faça um programa que tenha uma função chamada escrevea(), que
#receba um texto qualquer como parametro e mostra uma mensagem com
#tamanho adaptavel

def escreva(msg):
    tam = len(msg) + 2 # para deixar o tamanho proporcional a frase
    print('-=' * tam)
    print(f'  {msg}') # centralizar
    print('-=' * tam)

#principal
escreva("oi")
escreva("Pablo Vitorino A.")
escreva("Heterofobico")


# exercicio 98.. faça um programa que tenha uma função chamada contador()
# que receba tres parametros: inicio, fim e passo. seu programa te que
# relaizar tres contagens atraves da função criada
# a) de 1 ate 10, de 1 em 1
# b) de 10 ate 0, de 2 em 2
#c) uma conatagem personalizada
from time import sleep
def contador(inicio, fim, passo):
    print('=' * 15)  # linha, sseparadora
    print(f"contagem de {inicio} ate {fim} de {passo} em {passo}")   # vai ler
    
    if passo < 0: # inicio da part personalizada
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:# fim da part personalizada
        contad = inicio 
        while contad <= fim:     # parte: pulando de um em um
            print(f"{contad}", end=' ')
            sleep(0.5)  # contagem
            contad += passo
        print(". Acabou, caramba!")
    else:
        contad = inicio # pulando de dois em dois
        while contad >= fim:
            print(f"{contad}", end=' ')
            sleep(0.5)  # contagem
            contad -= passo
        print("fim")

# principal
contador(1, 10, 1) # pulando de um em um
contador(10, 0, 2) # pulando de dois em dois
print()
print("agora é a sua vez de personalizar")  # essa é a personalizada
ini = int(input("inicio: "))
fim = int(input("fim: "))
pas = int(input("passo: "))
contador(ini, fim, pas)

 
    
