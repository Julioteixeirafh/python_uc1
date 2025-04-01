idade=int(input("Digite a sua idade:"))
renda=float(input("Qual é o valor da sua renda?:"))
condicao=input("Seu nome está sujo?: <s/n>")

if (idade>=21) and (renda>=2000) and (condicao=="n"):
    print ("EMPRESTIMO ACEITO")
else:
    print ("EMPRESTIMO NEGADO")