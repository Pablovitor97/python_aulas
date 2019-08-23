def nini():
    nome = input("digite um nome: ");
    if nome == "pablo" or nome == "Pablo":
        print("que nome bonito,", nome);
    else:
        print("ata, muito prazer", nome);

nini();


def ata():
    from time import sleep;
    for c in range(10, 0, -1):
        print(c);
        sleep(1);
    print('___FOGUETE LANÇADO___');

ata();


# numeros de 1 a 50
def sing():  
    for c in range(1, 51):
        print(c, end=' ');

sing();




