temperatura=int(input("Qual é a temperatura?:"))

if (temperatura>=30):
    print ("QUENTE")
elif (temperatura<=10):
    print ("FRIO")
elif (temperatura<30) and (temperatura>10):
    print ("AGRADAVEL")