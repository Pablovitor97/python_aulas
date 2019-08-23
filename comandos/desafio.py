#!/usr/bin/python

dirArquivo = 'C:\\Users\\User\\Desktop\\Desafio\\REMUNERACAO.txt';
funcionarios = [];
numeroFuncionarios = 0;
run = True;

#NOME;CARGO;ORGÃO;REMUNERAÇÃO DO MÊS;FÉRIAS E 13º SALÁRIO;PAGAMENTOS EVENTUAIS;LICENÇA PRÊMIO INDENIZADA;ABONO PERMANÊNCIA & OUTRAS INDENIZAÇÕES;REDUTOR SALARIAL;TOTAL LIQUÍDO (R$)

def iniciar(diretorio):
    global numeroFuncionarios #Para conseguir alterar a variavel que esta definida no escopo do codigo.
    numeroFuncionarios = carregarFuncionarios(diretorio);
    enviarOpcoes(True);
    tratarOpcao();
    

def carregarFuncionarios(diretorio):
    arquivo = open(diretorio, 'r');
    funcionariosTotais = 0;
    for funcionariosInfo in arquivo:
        funcionarios.append(funcionariosInfo.split(';'));
        funcionariosTotais += 1;
    arquivo.close();
    
    return funcionariosTotais;

def tratarOpcao():
    while(run):
        resposta = input("Insira a opcao desejada: ");
        
        if(resposta == '1'):
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

def verQuantidadeFuncionarios():
    print(" ");
    print("Total de " + str(numeroFuncionarios) + " funcionarios encontrados.");
    print(" ");
    desejaContinuar();

def verFuncionarioPeloCargo():
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *): ");
    
    totalFuncionariosCargo = 0;
    
    if(cargo == '*'):
        cargo = 'TODOS';

    for funcionariosCargos in funcionarios:
        if(funcionariosCargos[1] == cargo or cargo == 'TODOS'):
            print("Funcionario: " + funcionariosCargos[0] + " - Cargo: " + funcionariosCargos[1]);
            totalFuncionariosCargo += 1;
            
    print("Total de " + str(totalFuncionariosCargo) + " funcionarios registrados no cargo " + cargo + ".");
    
    desejaContinuar();
        
def verMediaSalarial():
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *): ");
    
    totalFuncionariosSalario = 0;
    totalFuncionariosCargo = 0;
    
    if(cargo == '*'):
        cargo = 'TODOS';

    for funcionariosCargos in funcionarios:
        if(funcionariosCargos[1] == cargo or cargo == 'TODOS'):
            totalFuncionariosSalario += float(funcionariosCargos[3].replace(',', '.'));
            totalFuncionariosCargo += 1;
    
    mediaSalarial = totalFuncionariosSalario / totalFuncionariosCargo;
    print("Total de " + str(totalFuncionariosCargo) + " funcionarios registrados no cargo " + cargo + ", obtendo uma media salarial de "+str(mediaSalarial) + " reais.");
    
    desejaContinuar();

def verMaiorSalario():
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *): ");
    
    maiorFuncionarioSalario = ['NOME', 'CARGO', 'ORGÃO', '0.0', 'FÉRIAS E 13º SALÁRIO', 'PAGAMENTOS EVENTUAIS','LICENÇA PRÊMIO INDENIZADA','ABONO PERMANÊNCIA & OUTRAS INDENIZAÇÕES','REDUTOR SALARIAL','TOTAL LIQUÍDO (R$)']
    
    if(cargo == '*'):
        cargo = 'TODOS';

    for funcionariosCargos in funcionarios:
        if(funcionariosCargos[1] == cargo or cargo == 'TODOS'):
            if(float(funcionariosCargos[3].replace(',', '.')) > float(maiorFuncionarioSalario[3].replace(',', '.'))):
                maiorFuncionarioSalario = funcionariosCargos;
    
    
    print("O maior salario e do funcionario " + maiorFuncionarioSalario[0] + "(" + maiorFuncionarioSalario[1] +  ")" +  ", recebendo uma remuneracao mensal de " + maiorFuncionarioSalario[3] + " reais.");
    
    desejaContinuar();

def verFuncionarioPeloNome():
    funcionario = input("Insira o nome do funcionario para ver as informacoes: ");

    funcionarioInfo = None;

    for funcionarioNome in funcionarios:
        if(funcionarioNome[0].lower() == funcionario.lower()): #O .lower() e para deixar a string toda em letra minuscula.
            funcionarioInfo = funcionarioNome;
            break;
    
    if(funcionarioInfo != None):
        #NOME;CARGO;ORGÃO;REMUNERAÇÃO DO MÊS;FÉRIAS E 13º SALÁRIO;PAGAMENTOS EVENTUAIS;LICENÇA PRÊMIO INDENIZADA;ABONO PERMANÊNCIA & OUTRAS INDENIZAÇÕES;REDUTOR SALARIAL;TOTAL LIQUÍDO (R$)
        print(" ");
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

def verFuncionarioPorOrgao():
    orgao = input("Insira o orgao que voce deseja filtrar (se quiser ver todos, insira *): ");
    
    totalFuncionariosOrgao = 0;
    
    if(orgao == '*'):
        orgao = 'TODOS';

    for funcionariosOrgao in funcionarios:
        if(funcionariosOrgao[1] == orgao or orgao == 'TODOS'):
            print("Funcionario: " + funcionariosOrgao[0] + " - Orgao: " + funcionariosOrgao[2]);
            totalFuncionariosOrgao += 1;
            
    print("Total de " + str(totalFuncionariosOrgao) + " funcionarios registrados no orgao " + orgao + ".");
    
    desejaContinuar();

def enviarOpcoes(first):
    print(" ");
    if(first == True):
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
    