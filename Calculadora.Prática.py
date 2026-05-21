#  CALCULADORA / PROJETO PRÁTICO IF/ELIF/ELSE


Numero1 = int(input("Digite um numero: "))
Numero2 = int(input("Digite outro numero: "))
Op = input ("Escolha uma operação  ( +, -, *, / ) ")
if Op == "+":
    Resultado1 = Numero1 + Numero2
    print ("A soma é: {}".format (Resultado1))
elif Op == "-":
    Resultado2 = Numero1 - Numero2
    print ("A subtração é: {}".format (Resultado2))
elif Op == "*":
    Resultado3 = Numero1 * Numero2
    print ("A multiplicação é: {}".format (Resultado3))
elif Op == "/":
    Resultado4 = Numero1 // Numero2
    print ("A divisão é: {}".format (Resultado4))
else:
    print ("Operação Inválida!")