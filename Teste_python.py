progra= "python","deep learning", "c#"
nome = "Angelo Antonio ","lais Tiemi"
pets =["Rambo","Tutu"]
idade = 26

print(f"Lista de nomes: {nome[1]} e linguagem de programação: {progra[0]} aqui")

print(f"Sou o {nome[1].title()}.")
print(f"Em 2021 farei {idade + 1} anos.")
print(f"Tenho {len(pets)} pets. ")
print("Os pets da casa são: "+str(pets))


print("")

n = "angelo"
print("{0} Programa, {0} estuda, {0} planta, {0} trabalha".format(n.title()))
print("%s programa, %s estuda, %s planta, %s trabalha. " %(n,n,n,n))



print(
    f"O quadrado dos inteiros de 1 a 20: "
    f"{[x ** 2 for x in range(1,21)]}"
    )


print(f"{{}}")
idade = 36

print(f"{{idade}}")
print(f"Tenho {{ {idade} }} anos.")


#format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]

nome = "Robô"

print(f"|  {nome: <40}  |")
print(f"|  {nome: >40}  |")
print(f"|  {nome: ^40}  |")
print(f"|  {nome:*^40} |")
print(f"|  {nome:_<40} |")
print(f"|  {nome:=<40} |")
print(f"|  {nome:+<52} |")
print(f"|  {nome:=<40} |")
print(f"|  {nome::>40} |")
print(f"|  {nome:=^40} |")
print(f"|  {nome:^^40} |")



saldo = 1_000_000

print(f"Meu saldo é: {saldo:,}")


questao = 10
acertos = 8

print(f"Acertei {acertos/questao:%} da prova.")
print(f"Acertei {acertos/questao:.2%} da prova.")


nome = "Angelo"

print(f"nome = {nome!r}")
print(f"nome = {nome}")
