#O programa que lê nome, idade e sexo de 8 pessoas.
#No final mostra:
#->a média de idade do grupo
#->qual é o nome do homem mais velho
#->quantas mulheres têm menos de 20 anos
cm = 0
cont = 0
mi = 0
hvn = ""
hvi = 0
for c in range (1,9):
    print(f"===Pessoa #{c}===")
    while True:
        nome = str(input("Nome:"))
        if nome.isalpha():
            break
        print("ERRO.Digite apenas LETRAS e não NÚMEROS.")
    while True:
        try:
            idade = int(input("Idade:"))
            break
        except ValueError:
            print("ERRO!Digite um número!")
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("SEXO: [M] ou [F]?\nDIGITE apenas uma LETRA->")).strip().upper()
    print("CADASTRADO(A)")
    mi += idade
    cont += 1
    if sexo == "M":
        if c == 1:
            hvi = idade
            hvn = nome
        elif idade > hvi:
            hvi = idade
            hvn = nome
    if sexo == "F" and idade < 20:
        cm+= 1
print(f"A média de idade do grupo é {mi/cont}")
print(f"O nome do homem mais velho é {hvn}")
print(f"E existem {cm} mulheres com menos de 20 anos.")

