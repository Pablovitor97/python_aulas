######### LER OS DADOS DE UMA PESSOA ################


dados = {'nome': [], 'telefone': [], 'idade': []}


op = True;
while op:
    op_string = input("Deseja continuar? sim ou nao "); 
    if (op_string == "sim"):
        dados['nome'].append(input("digite o nome: "));
        dados['telefone'].append(input("digite o num de tel: "));
        dados['idade'].append(input("digite a sua idade"));
    else:
        op = False;
                      
arq = open('wiwi.txt', 'a')
for ab in dados['nome']:
    for cd in dados['telefone']:
        for ef in dados ['idade']:
            arq.write(ab + ';' +cd+ ';' +ef+ '\n');
arq.close()
                      
################# LENDO OS DADOS DESSE ARQUIVO #####################
arq = open('wiwi.txt', 'r')
for ab in arq:
    print(ab);
    for cd in arq:
        print(cd);
        for ef in arq:
            print(ef);
arq.close()
