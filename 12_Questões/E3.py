#Implemente um conversor de bases numéricas (decimal, binário, octal, hexadecimal)
# com validação
try:
    a = int(input("Digite um número para conversão: "))
    decimal = a
    binario = bin(a)
    octal = oct(a)
    hexadecimal = hex(a)

    print(f"Número {decimal} em binário é {binario}")
    print(f"Número {decimal} em octal é {octal}")
    print(f"Número {decimal} em hexadecimal é {hexadecimal}")
    

except ValueError:
    print("Valor informado esta errado, Digite um número para conversão.")
