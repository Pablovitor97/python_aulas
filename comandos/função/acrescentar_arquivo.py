novo = open('wiwi.txt','w');
novo.write("mais u teste.\n");
novo.write("criando umma pasta.\n");
novo.write("sera que vai funcionar? \n");
novo.close()

novo = open('wiwi.txt','r')
for linha in novo:
    linha = linha.rstrip()
    print(linha)
novo.close()


#### acrecendtando usando o modo A
print('\n')
texto = input('ADICIONE UMA FRASE:  \n')
novo = open('wiwi.txt','a')
novo.write(texto + "\n")
print("terminado " + novo.name + "muito bem")
novo.close()

print("\nAcrescentar o texto. \n")
novo = open('wiwi.txt','r')
for linha in novo:
    linha = linha.rstrip()
    print(linha)
novo.close()


