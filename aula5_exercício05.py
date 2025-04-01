nome=input("Digite o seu login:")
senha=input("Informe a sua senha:")

if (len(nome) <3):
    print ("!!! ERRO - Nome Invalido !!!")
elif (len(senha) <6):
    print (" !!! ERRO - Senha invalida !!!")
elif (senha=="123456") or  (senha=="senha"):
    print ("!!! ERRO - senha Fraca !!!")
else:
    print ("[OK] cadatrado")
    