#!/usr/bin/python
#  variaveis que podem ser acessadas por todass as funçoes do modulo; o escopo global(variavel)
dirArquivo = 'C:\\Users\\PABLO\\Desktop\\REMUNERACAO.txt';
funcionarios = [];
numeroFuncionarios = 0;
run = True;

#NOME;CARGO;ORGÃO;REMUNERAÇÃO DO MÊS;FÉRIAS E 13º SALÁRIO;PAGAMENTOS EVENTUAIS;LICENÇA PRÊMIO INDENIZADA;ABONO PERMANÊNCIA & OUTRAS INDENIZAÇÕES;REDUTOR SALARIAL;TOTAL LIQUÍDO (R$)

def iniciar(diretorio):    # essa função ira carregar o diretorio, que no caso seria o dirArquivo, com o arquivo REMUNERAÇÃO
    global numeroFuncionarios # mostrar o numero de funcionarios
    numeroFuncionarios = carregarFuncionarios(diretorio); # carregar todos os funcio;
    enviarOpcoes(True); 
    tratarOpcao();
    

def carregarFuncionarios(diretorio): # essa função ira pegar todos os funcionarios e carregara o dirarquivo
    arquivo = open(diretorio, 'r'); # vai ler todo o dirarquivo(REMUNERAÇÃO); somente
    funcionariosTotais = 0;
    for funcionariosInfo in arquivo:  # pegar todos os dados dos funcio
        funcionarios.append(funcionariosInfo.split(';'));  # a função split ira colocar as linhas em ordem
        funcionariosTotais += 1;  # contador 
    arquivo.close();  # fechar o arquivo
    
    return funcionariosTotais;  # vai retornar para um numero total de funcio

def tratarOpcao():
    while(run):    # vai tratar as opçoes escolhidas no modulo, se as informaçoes forem corretas, ele roda, senão, ele emite uma msg de erro
        resposta = input("Insira a opcao desejada: ");  
        
        if(resposta == '1'):    # 
            verQuantidadeFuncionarios();
        elif(resposta == '2'):
            verFuncionarioPeloCargo();
        elif(resposta == '3'):
            verMediaSalarial();
        elif(resposta == '4'):
            verMaiorSalario();
        elif(resposta == '5'):
            verFuncionarioPeloNome();
        elif(resposta == '6'):
            verFuncionarioPorOrgao();
        elif(resposta == '7'):
            sair();

def verQuantidadeFuncionarios():  # ver a quantidades de funcio 
    print(" ");
    print("Total de " + str(numeroFuncionarios) + " funcionarios encontrados.");
    print(" ");
    desejaContinuar(); # se a opção for NAO, vai encerrar

def verFuncionarioPeloCargo():  # caso coloque um carno inesistente, o programa mostrarar erro
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *): ");
    # vai aparecer o cargo e todos as pessoas que estao trabalhando nele
    totalFuncionariosCargo = 0;
    
    if(cargo == '*'):
        cargo = 'TODOS';
         
    for funcionariosCargos in funcionarios:   
        if(funcionariosCargos[1] == cargo or cargo == 'TODOS'):
            print("Funcionario: " + funcionariosCargos[0] + " - Cargo: " + funcionariosCargos[1]);
            totalFuncionariosCargo += 1;
            
    print("Total de " + str(totalFuncionariosCargo) + " funcionarios registrados no cargo " + cargo + ".");
    
    desejaContinuar(); # se for "não", ira encerraer..
        
def verMediaSalarial():  # aparecera o cargo expecificado
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *): ");  #   

    totalFuncionariosSalario = 0;
    totalFuncionariosCargo = 0;
    
    if(cargo == '*'):
        cargo = 'TODOS';

    for funcionariosCargos in funcionarios:
        if(funcionariosCargos[1] == cargo or cargo == 'TODOS'):
            totalFuncionariosSalario += float(funcionariosCargos[3].replace(',', '.'));  # mostrara o valor total do salario
            totalFuncionariosCargo += 1; 
    
    mediaSalarial = totalFuncionariosSalario / totalFuncionariosCargo;
    print("Total de " + str(totalFuncionariosCargo) + " funcionarios registrados no cargo " + cargo + ", obtendo uma media salarial de "+str(mediaSalarial) + " reais.");
    
    desejaContinuar(); # se for sim, ira volltar ao menu de escolhas

def verMaiorSalario():  # ira mostrar qual funcionario tem o maior salario dentro da empresa
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *): ");
   # os codigos irão pegar todas as informaçoes do funcionario, como, nome, cargo e etc e mostrar no programa
    maiorFuncionarioSalario = ['NOME', 'CARGO', 'ORGÃO', '0.0', 'FÉRIAS E 13º SALÁRIO', 'PAGAMENTOS EVENTUAIS','LICENÇA PRÊMIO INDENIZADA','ABONO PERMANÊNCIA & OUTRAS INDENIZAÇÕES','REDUTOR SALARIAL','TOTAL LIQUÍDO (R$)']
    
    if(cargo == '*'):
        cargo = 'TODOS';

    for funcionariosCargos in funcionarios:
        if(funcionariosCargos[1] == cargo or cargo == 'TODOS'):
            if(float(funcionariosCargos[3].replace(',', '.')) > float(maiorFuncionarioSalario[3].replace(',', '.'))):  # replace
                maiorFuncionarioSalario = funcionariosCargos;
    
    
    print("O maior salario e do funcionario " + maiorFuncionarioSalario[0] + "(" + maiorFuncionarioSalario[1] +  ")" +  ", recebendo uma remuneracao mensal de " + maiorFuncionarioSalario[3] + " reais.");
    
    desejaContinuar(); # se for "SIM", ira retronar ao menu, se for 'nao', o programa sera encerrado..

def verFuncionarioPeloNome():  # pesquisa por um funcionario expecifico e mostrarar todas as informaçoes possiveis dessa tal pessoa
    funcionario = input("Insira o nome do funcionario para ver as informacoes: ");

    funcionarioInfo = None; # none é algum tipo de valor nulo

    for funcionarioNome in funcionarios:
        if(funcionarioNome[0].lower() == funcionario.lower()): #O .lower() e para deixar a string toda em letra minuscula.
            funcionarioInfo = funcionarioNome;
            break;  #parar 
    
    if(funcionarioInfo != None):  
        #NOME;CARGO;ORGÃO;REMUNERAÇÃO DO MÊS;FÉRIAS E 13º SALÁRIO;PAGAMENTOS EVENTUAIS;LICENÇA PRÊMIO INDENIZADA;ABONO PERMANÊNCIA & OUTRAS INDENIZAÇÕES;REDUTOR SALARIAL;TOTAL LIQUÍDO (R$)
        print(" ");                                            # as strings carregando todas as inforçaoes do funcio para serem apresentadas
        print("Informacoes de " + funcionarioInfo[0] + ":");
        print("Cargo: " + funcionarioInfo[1]);
        print("Orgao: " + funcionarioInfo[2]);
        print("Salario: R$" + funcionarioInfo[3]);
        print("Ferias e 13º: R$" + funcionarioInfo[4]);
        print("Pgtos. eventuais: R$" + funcionarioInfo[5]);
        print("Licenca premio indenizada: R$" + funcionarioInfo[6]);
        print("Abono, permanencia e outras indenizacoes: R$" + funcionarioInfo[7]);
        print("Redutor salarial: " + funcionarioInfo[8]);
        print("Total liquido: R$" + funcionarioInfo[9]);
    else:
        print("Funcionario " + funcionario + " nao encontrado.");

    desejaContinuar();

def verFuncionarioPorOrgao():  # mostrar todos os funcionarios que trabalham naquela area em expecifico
    orgao = input("Insira o orgao que voce deseja filtrar (se quiser ver todos, insira *): ");
    
    totalFuncionariosOrgao = 0;
    
    if(orgao == '*'):
        orgao = 'TODOS';

    for funcionariosOrgao in funcionarios:
        if(funcionariosOrgao[1] == orgao or orgao == 'TODOS'):
            print("Funcionario: " + funcionariosOrgao[0] + " - Orgao: " + funcionariosOrgao[2]);
            totalFuncionariosOrgao += 1; # contador
            
    print("Total de " + str(totalFuncionariosOrgao) + " funcionarios registrados no orgao " + orgao + ".");
    
    desejaContinuar();

def enviarOpcoes(first):
    print(" ");
    if(first == True):  # serão enmviadas primeiro/ essas sao as informaçoes que aparecem logo no inicio do programa, o menu de opçoes
        print("Arquivo de funcionarios carregado por completo, voce pode prosseguir inserindo uma das opcoes abaixo.");
    print("1 - Veja a quantidade de funcionarios");
    print("2 - Veja todos os funcionarios pelo cargo");
    print("3 - Veja a média salarial dos funcionarios");
    print("4 - Veja o maior salário entre os funcionarios");
    print("5 - Veja as informacoes de um funcionario pelo nome");
    print("6 - Veja os funcionarios por orgao publico");
    print("7 - Saia do programa");
    print(" ");

def desejaContinuar():
    opcao = input("Deseja continuar usando o programa (SIM ou NAO)? ");
            
    if(opcao.lower() == 'sim'): #O .lower() e para deixar a string toda em letra minuscula.
        enviarOpcoes(False);
    else:
        sair();

def sair():
    global run;
    run = False;
    print("Voce saiu do programa.");

iniciar(dirArquivo);
    
