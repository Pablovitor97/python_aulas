# mais testes
#!/usr/bin/python

dirArquivo = 'C:\\Users\\PABLO\\Desktop\\REMUNERACAO.txt';
funcionarios = [];
numFuncio = 0;
run = True;


def inicar(diretorio):  # o diretorio é o dirarquivo
    global numFuncio # para conseguir alterar a variavel que esta definida
    numFuncio = carregarFuncionarios(diretorio);# carrega todos os funcionarios
    enviarOpcoes(True);
    tratarOpcao();

def carregarFuncionarios(diretorio): # vai pegar todos os func e criar um diretorio parra carrregar o arquivo
    arquivo = open(diretorio, 'r'); # ele vai abrir e ler o arquivo
    funcionariosTotais = 0;
    for funcionariosInfo in arquivo:
        funcionarios.append(funcionariosInfo.split(';'));
        funcionariosTotais += 1; # contador
    arquivo.close();

    return funcionariosTotais; # aqui ele vai voltar para todos od func

def tratarOpcao():
    while(run):
        resposta = input("Insira a opcão desejada: ");

        if(respostar == '1'):
            verQuantidadeFuncionarios();
        if(resposta == '2'):
            verFuncionariosPeloCargo();
        if(resposta == '3'):
            verMediaSalarial();
        if(resposta == '4'):
            verMaiorSalario;
        if(resposta == '5'):
            verFuncionarioPeloNome;
        if(resposta == '6'):
            verFuncionarioPorOrgao;
        if(resposta == '7'):
            sair();

def verQuantidadeFuncionarios():
    print(" ");
    print("Total de" + str(numFuncio)+ " funcionarios encontrados.");
    print(" ");
    desejaContinuar();

def verFuncionarioPeloCargo():
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos digite *): ");
        # vai pegar um em expecifico..
    totalFuncionariosCargo = 0;

    if(cargo == '*'):
        cargo = 'TODOS';

    for funcionariosCargos in funcionarios:  #funcio e carg expecificas..
        if(funcionariosCargos[1] == cargo or cargo == 'TODOS'):
            print("funcionarios: " + funcionariosCargos[0] + " - Cargos: " + funcionariosCargos[1]); # print em todso oos funcio
            totalFuncionarioscargos += 1;

    print("total de " + str(totalFuncionariosCargo) + " funcionarios resgistrrados no cargo" + cargo + " . ");

    desejaContinuar();

def verMediaSalarial():
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *) : ";

    totalFuncionariosSalario = 0;
    totalFuncionariosCargo = 0;

    if(cargo == '*'):
        cargo == 'TODOS';

    for funcionariosCargo in funcionarios:
        if(funcionariosCargos[1] == cargo or cargo 'TODOS'):
            totalFuncionariosSalario += float(funcionarioscargos[3].replace(',', '.'));
            tatalFuncionariosCargo += 1;

    mdiaSalarial = totalFuncionariosSalario / totalFuncionariosCargos;
    print("Total de " + str(totalFuncionariosCargo) + " funcionarios no cargo " + cargo + ", obtendo uma media salarial de " str(mediaSalarial) + " reais.");

    desejaContinuar();

def verMaiorSalario();
    cargo = input("Insira o cargo que voce deseja filtrar (se quiser ver todos, insira *): "));'
                            
    maiorFuncionarioSalario = ['NOME', 'CARGO', 'ORGÃO', '0.0', 'FÉRIAS E 13º SALÁRIO', 'PAGAMENTOS EVENTUAIS','LICENÇA PRÊMIO INDENIZADA','ABONO PERMANÊNCIA & OUTRAS INDENIZAÇÕES','REDUTOR SALARIAL','TOTAL LIQUÍDO (R$)']

    if(cargo == '*'):
        cargo = 'todos';

    for funcionarioCargos in funcioanrio:
        if(funcioanriosCargos[1])
    
 
                  
        
        
        
