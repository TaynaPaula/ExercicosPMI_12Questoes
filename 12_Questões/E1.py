#Crie um programa que valide um número de telefone brasileiro e formate-o
#corretamente usando try/except

try:
    a=input("Digite o numero de tellefone com prefixo e DDD:")
    prefixo=a[0:2]
    if prefixo =="55" and len(a)==13:
        print(f"Número de telefone {a} é válido e é brasileiro")
    elif prefixo !="55" and len(a)==13:
        print(f"Número de telefone {a} é válido mas não é brasileiro")
    else:
        print(f"Número de telefone {a} não é válido")
except ValueError:
    print("Por favor, informe os valores corretamente.")