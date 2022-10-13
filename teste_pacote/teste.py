#Testando pacote criado
from Pacote_Calculadora import operacoes

valor1= float(input("Digite o primeiro valor: "))
valor2= float(input("Digite o segundo valor: "))
operacao = int(input("Digite qual opecação deseja efetuar :\n [1] para soma: \n [2] para subtração: \n [3] para multiplicacao: \n [4] para divisão: "))

# implementando metodos do pacote criado
if operacao == 1:
    print(operacoes.soma(valor1, valor2))

elif operacao == 2:
    print(operacoes.subtracao(valor1, valor2))

elif operacao == 3:
    print(operacoes.multiplicacao(valor1, valor2))

elif operacao == 4 and valor2 != 0:
    print(operacoes.divisao(valor1, valor2))      
