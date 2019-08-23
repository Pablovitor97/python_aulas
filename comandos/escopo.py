

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ESCOPOLOS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

#GLOBAL: VOCE CONSEGUE LER E ESCREVER EM QUALQUER LUGAR DO SU CODIGO
#LOCAL: SO VAI FUNCIONART DENTRO DE UMA FUNÇÃO;
#


a = 1     # esse ja e um global por estar fora do "def";
b = 2
c = 3
def abc():
    print(a)
    print(b)
    print(c)
abc()
print("----------FIM-------")



def abc():  # esse ja é local, porque todos estao dentro da função def"
    a = 1
    b = 2
    c = 3
    print(a)
    print(b)
    print(c)
abc()

print('--------- FIM --------------')





 
