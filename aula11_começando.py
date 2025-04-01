#1

# pessoa={"nome" : "Julio", "idade" : 25, "cidade": "Petropolis"}
# print (f"Dados da pessoa: {pessoa}")

# pessoa["idade"]=24
# print (f"dados atualizado: {pessoa}")

# pessoa["email"]= "juliocezarteifilho@gmail.com"
# print(f"Dados atualizados: {pessoa}")

# pessoa["sexo"]="m"
# print(f"dados atualizado: {pessoa}")


#2


# d3=d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# print (f"Dicionários originais:")
# print (f"D1 : {d1}")
# print (f" d2 : {d2}")

# d1.update(d2)
# d2.update(d3)

# print (f"Dicionários atualizados:")
# print (f"D1 : {d1}")
# print (f" d2 : {d2}")


#3


# frase = "o rato roeu a roupa do rei de roma"
# palavras = frase.split()
# contagem = {}

# for i in palavras:
#     contagem [i] = contagem.get(i, 0)+1

# print (contagem)


#4


# aluno_1 = {"nome": "Maria", "notas": [7.5, 8.0, 9.2]}
# aluno_2 = {"nome": "João", "notas": [6.0, 7.8, 8.5]}
# aluno_3 = {"nome": "Carlos", "notas": [5.5, 6.5, 7.0]}

# print (f"dados do aluno {aluno_1}")

# print (f"As notas do aluno{aluno_1 {'nome'}} são {aluno_1{'notas'}}")

# media = sum (aluno_1{"notas"}) / len (aluno_1{"notas"})
# print (f"O aluno {aluno_1["nome"]} obteve media igua a: [media]")

# aluno_1 {"media"}=media
# print (f"Dados do aluno 1 {aluno_1}")



#TREFA 2


#1


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def exibir_info(self):        
       
        if self.ligado == True:
            status = "ligado"
        else :
            status = "desligado"
       
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}.")

    def ligar(self):
        self.ligado=True
        #print(f"O carro etsá ligado")

    def desligar(self):
        self.ligado= False
        #print(f"O carro etsá desligado")



if __name__=="__main__":
    print (f"criano um objeto da classe carros")
    meu_carro= Carro ("Toyota","Corolla", 2020)
    meu_carro.exibir_info()
    meu_carro.ligar()
    meu_carro.exibir_info()


   






