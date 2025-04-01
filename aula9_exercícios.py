

def somar_elemento ():
    numeros=[]
    for i in range(5):
        numero=int(input("Digite um numero :"))
        numeros.append(numero)
    
    soma=sum(numeros)
    print(f"A soma dos valores lidos é {soma}")


def somar_elemento_v2 (vezes):
    numeros=[]
    for i in range(vezes):
        numero=int(input("Digite um numero :"))
        numeros.append(numero)
    
    soma=sum(numeros)
    print(f"A soma dos valores lidos é {soma}")


def numeros_impares():
    numeros=[]
    for i in range (1,51,2):
        numeros.append(i)
    print (f" Os numeros são: {numeros}")





if __name__ == "__main__":

    #somar_elemento ()
    # somar_elemento_v2 (10)
    numeros_impares()

    