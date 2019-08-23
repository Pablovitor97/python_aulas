#####  CRIANDO E ESCREVENDO EM ARQUIVOS NO PYTHON (MODO 'W') #####

arquivo = open('ttestes.txt','w');
arquivo.write("Olá, esse é um teste\n");
arquivo.write("criando um arquivo de texto com python\n");
arquivo.write("substituindo e criando outro arquivo, mesmo qeu ele ja exista ou não\n");
arquivo.write("que coisa em\n");
arquivo.close()

## LENDO O ARQUIVO

arquivo = open('ttestes.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()

# o "write" escreve adiciona as linhas com os textos
# 'w' ele cria e substitui os testos existente/ cria ate uma pasta, caso ela nao existir
# e cria as coisas que colocamos dentro dela
# sempre coloque o " ARQUIVO = OPEN('NOME DO ARQUIVO','R'), PORQ O ARQUIVO TEM QUE SER LIDO

#########################################

### (MODO 'A') ACRESCENTAR ALGO NO ARQUIVO E ELE SO VAI CRIAR UM NOVO ARQUIVO SE ELE NAO EXISTIR

print("\n")
texto = input('digite uma frase para acrescentar no arquivo: \n')
arquivo = open('ttestes.txt','a')   
arquivo.write(texto + "\n")
print("operação concluida no arquivo " + arquivo.name + "usando modo de ascesso \n")
arquivo.close()

print("\nTexto alterado.\n")
arquivo = open('ttestes.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()

###############################################











