
soma = lambda n1,n2:n1 + n2
div = lambda n1,n2:n1 / n2
minn = lambda n1,n2:n1 - n2
mul = lambda n1,n2:n1 * n2
op_escolha = input("Operação matemática:(1-Adição/2-Subtração/3-Divisão/4-Multiplicação))")

n1 = int(input("Primeiro número"))
n2 = int(input("segundo número"))
if op_escolha == '1':
    print("Resultado: ",int(soma(n1,n2)))
elif op_escolha == '2':
    print("Resultado: ",int(minn(n1,n2)))
elif op_escolha == '3':
    print("Resultado ",int(div(n1,n2)))
elif op_escolha == '4':
    print("Resultado: ",int(mul(n1,n2)))
else:
    print('Escolha não disponivel')
    
