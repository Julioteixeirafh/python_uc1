vet_dados=[15, 2, 94, 30, 8, 76, 2025]
vetor=[10, 20, 30, 40, 50, 3, 3, 5, 3]

def criar_imprimir_lista ():
    vetor=[15, 2, 94, 30, 8, 76, 2025]
    print (f"\n\t O conteudo do vetor é {vetor}\n")


def criar_imprimir_lista_v2(vetor):
    print (f"\n\t O conteudo do vettor é {vetor}\n")


def interando_sobre_uma_lista (vetor) :
    for elemento in vetor:
        print (f"Elemento: {elemento}")


def somar(vetor): 
    soma = sum(vetor)
    print("soma dos elementos é: ", soma)


def maior_menor(vetor):
    maior= max(vetor)
    menor= min(vetor)

    print ("O número maximo: ", maior)
    print ("O numero minimo: ",menor)


def inversao(vetor):
    vetor_invertido = vetor[::-1]
    print("Vetor invertido: ", vetor_invertido)


def multiplicacao(vetor):
    multiplicador=5
    for elemento in vetor:
        variavel=elemento*multiplicador
        print(f"elemento: , {variavel}")


def contador (vetor):
    vezes=vetor.count(3)
    print(f"\n\t vetor ordenado: {vezes}\n")


def ordem_crescente(vetor):
    crescente=vetor[+1]
    print("Ordem crescente: ", crescente)


if __name__ == "__main__":

    # criar_imprimir_lista_v2 (vet_dados)
    # interando_sobre_uma_lista (vet_dados)
    # somar(vet_dados)
    # maior_menor(vet_dados)
    # inversao(vet_dados)
    # multiplicacao(vet_dados)
    # contador(vetor)
     ordem_crescente(vet_dados)



