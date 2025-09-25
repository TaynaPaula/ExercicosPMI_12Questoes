#Desenvolva um sistema de notas que calcule média, identifique aprovação/reprovação e 
# trate entradas inválidas.
try:
    n1=float(input("Digite o valor da n1: "))
    n2=float(input("Digite o valor da n2: "))
    n3=float(input("Digite o valor da n3: "))

    Nota_Final=(n1+n2+n3)/3
    if 0<=Nota_Final<4:
       print(f"Reprovado, média:{Nota_Final}. Notas lançadas {n1}, {n2} e {n3}")
    else:
       print(f"Aprovado, média:{Nota_Final}. Notas lançadas {n1}, {n2} e {n3}")
except ValueError:
    print("Valor informado esta errado, Tente novamente ")