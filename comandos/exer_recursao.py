print("-----CALCULO FATORIAL-----")

# EXERCICIO 1

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)
w = int(input("Digite um numero para saber o seu fatorial: "))
res = fatorial(w)
print("o fatorial é {} e {}".format(w, res))

#O método format() serve para criar uma string 
#que contem campos entre chaves a serem substituídos pelos argumentos de format

print('+='*20)

# EXERCICIO 2

def calculo(num):
    if num == 0 or num == 1:
        return num
    else:
        return calculo(num - 1) + calculo(num - 2)
x = int(input("Digite um numero: "))
n = int(input("digite outro numero: "))
res = (x**n)
print("{} e {} e o resto é {}".format(x, n, res));
    
print('-='*20)
# EXERCICIO 3


def new(lista):
    array = [1, 2, 3, 4, 5, 7, 10]
    if (lista < len(array) - 1):
        return array[lista] + new(lista + 1);
    else:
        return array[lista];

print(new(0))

print('+='*20)


# EXERCICIO 4
def hello(num, ocorre, pos, iden):
    if(pos < len(str(num))):
        if(int(str(num)[pos] == iden)):
            return 1 + hello(num, ocorre, pos + 1, iden);
        else:
            return hello(num, ocorre, pos + 1, iden);
    else:
        return ocorre;
print(hello(1000, 0, 0, 0));







