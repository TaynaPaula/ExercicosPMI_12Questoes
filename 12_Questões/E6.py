#Implemente um gerador de senhas seguras com diferentes critérios e validação. 
import random
print("Gerador de senhas")

try:
    tamanho = int(input("Digite o tamanho da senha (mínimo 8 caracteres): "))
    
    if tamanho < 8:
        print("Tamanho inválido, deve ser no mínimo 8 caracteres.")
    else:
        letras = input("Incluir letras? (s/n): ").lower() == "s"
        numeros = input("Incluir números? (s/n): ").lower() == "s"
        carac_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == "s"

       
        caracteres_validos = ""
        if letras:
            caracteres_validos += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if numeros:
            caracteres_validos += "0123456789"
        if carac_especiais:
            caracteres_validos += "!@#$%^&*"

        if not caracteres_validos:
            print("Nenhum tipo de caractere selecionado. Não é possível gerar a senha.")
        else:
           
            senha_lista = []
            if letras:
                senha_lista.append(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
            if numeros:
                senha_lista.append(random.choice("0123456789"))
            if carac_especiais:
                senha_lista.append(random.choice("!@#$%^&*"))
            
            
            while len(senha_lista) < tamanho:
                senha_lista.append(random.choice(caracteres_validos))
            
           
            random.shuffle(senha_lista)
            
          
            senha = ''.join(senha_lista)

            print(f"Senha gerada: {senha}")

except ValueError:
    print("Valor informado está errado. Informe o tamanho da senha corretamente.")