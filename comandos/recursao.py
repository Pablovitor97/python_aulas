print("----------RECURSIVIDADE----------")
print("----------CALCULANDO FATORIAL----------")

def fatori(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatori(numero - 1)
w = int(input("digite um numero para qualcular o seu fatorial: "))
res = fatori(w)
print(f"O fatorial de {w} é {res}")





print("----------FIBONACCI RECURSIVO----------")

def fibona(num):
    if num <= 1:
        return num
    else:
        return fibona(num - 1) + fibona(num - 2)

w = int(input("digite um numero para qualcular o seu fibonacci: "))
res = fibona(w - 1)
print(f"O fibonnaci de {w} é {res}")
