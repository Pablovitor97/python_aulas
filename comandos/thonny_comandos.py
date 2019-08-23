print("olá, Mundo");

nomes = input("digite um nome que quiser: ")
if nomes == "Pablo":
    print("que nome lindo")
"fim"

nome = open("ttestes.txt",'w'); # adicionei/criei coisas nele
nome.write("miau\n");
nome.write("criando \n");
nome.close()

nome = open('ttestes.txt','r');
for linha in nome:
    linha = linha.rstrip()
    print(linha)
nome.close()
