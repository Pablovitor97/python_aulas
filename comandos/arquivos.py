#1/urs/bin/python

'''manipulador = open('outros.txt', 'r')
print("\nMetodo read():\n")
print(manipulador.read())

manipulador.seek(0)  # volta para o inicio do arquivo

print("\nMetodo readline():\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print("\nMetodo readlinos():\n")
print(manipulador.readlines())

manipulador.close()'''


################################## OUTRO TIPO ###################################



'''print('teste de abertura de arquivos em python')
print('tentando abrir um arquivo de texto armazenado no pc:\n')

manipulador = open('outros.txt','r')
for linha in manipulador:
      linha = linha.rstrip()
      print(linha)
manipulador.close()'''


#################################################################################
      ##NUMERO DE LINHAS##
'''print("\nContando as linhas do arquivo de texto analisado: \n")
contador = 0
arq = open('outros.txt','r')
for linha in arq:
           contador = contador + 1
print("numero de linhas no arquivo: ", contador)
arq.close()'''





##################################################################################
   ##### ENCONTRAR UMA PALAVRA DENTRO DA FRASE ####

'''print("\nRetornando somente as linhas com a palavra Python\n")
arq = open('outros.txt','r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if 'python' in linha:
        contador = contador + 1
        print(linha)
print("\nForma retornadas", contador, "linhas")
arq.close()'''


###############################################################################
### EU VOU DIGITAR A PALVRA NO MEIUO DA ESECUÇÃO

print("\nRetornando somente as linhas que conteem a palavra pesquisada pelo usuario\n")
palavra = input('digite a palavra de busca: ')
arq = open('outros.txt','r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if palavra in linha:
        contador = contador + 1
        print(linha)
print("\nForam retornadas", contador, 'linhas')
op = True    # criei outro dentro dele... 
lista = []
while op:
    op_string = input("deseja continuar: sim ou nao ")
    if (op_string == 'sim'):
        lista.append(input('nome das pessoas: '))
    else:
        op_string = 'nao'
        op = False;
   
arq.close()

#####################################################################################






















