# Este é um comentário
print("Olá mundo :D")

print("Olá 2!") # Exemplo de print
'''
Um comentário em bloco é definido com três áspas
Sejam elas simples ou duplas
Filé?
'''

# Variáveis não necessitam definição de tipo e
# podem assumir qualquer valor/tipo
num = 10
num = "Rafael"
num = 10.98

a = num * 10

# Jeito simples separando os parâmetros por vírgula
print( "O resultado é", num, ", certo?" )

# Usando uma função para formatar a string
print( "O resultado é {}, certo?".format(num) )

nome = "Rafael"

# O sinal {} representa o valor de uma variável
print("{}, o resultado é {}, certo?".format(nome, num))

# Operador de potência é **
num = 5 ** 2 # 5 ao quadrado
num = 5 ** 3 # 5 ao cubo
num = 10 ** 8 # 10 elevado a 8

# Prioridade de operadores
# ** * / + -

# Calculando raiz
num = 9 ** 1 / 2 # isso é 4,5
num = 9 ** (1/2) # isso é raiz = 3
num = 256 ** (1/8) # Raiz de grau 8 de 256

# # # # # # # # # # # # # # # # # # # # # # # # #

# A identação define que código pertence a quem

# Condicionais
if(num % 2 == 0): # finaliza com dois pontos
    print("O número {} é par!".format(num))
    # Coisas do IF devem ficar identadas
    # ...
    if(True):
        # Cuide da identação!
        print("Pertence ao IF interno")

        while(True):
            print("Código do While!")

            break
        # Fim do while

    # Fim do IF interno

# Fim do IF externo
else:
    print("O número {} é ímpar!".format(num))

# Condicionais compostas:
# && Em python é --> and
# || Em python é --> or

# Toda entrada do input é string
num = input("Digite um número: ")
# Conversão para int() ou float() é necessária
num = int(num)

# Variável de controle
i = 0
while(i <= 10): # Depois da condição coloca :
    # Mantenha o código identado para pertencer ao while
    res = i * num
    print( "{} x {} = {}".format(num, i, res) )

    # Não existe i++ ou i--
    # Acrescenta 1 ao valor de i
    i += 1 # é igual a i = i + 1
# Fim do while

# Listas, vetor, array
# Criando vetor vazio/nulo
vetor = []

# Adicionar algo ao vetor
vetor.append(10)
vetor.append(3)
vetor.append(7)
vetor.append(8)

# Criando um vetor já preenchido
vetor = [10, 5, 19, 53, 48, 9]

# Cria vetor vazio com tamanho N
vetor = [""] * 10
vetor[0] = 19
vetor[1] = 5
vetor[9] = 12

# Pedindo para o usuário os valores...
vetor = [""] * 4
i = 0

# len() calcula o tamanho de algo
while( i < len(vetor) ):
    # Pede um valor, converte pra int e armazena na posição "i"
    vetor[i] = int( input("Número: ") )

    # Incremento da posição
    i = i + 1

# Mostrando o vetor
print(vetor)

# Para fazer a soma
soma = 0

# Percorrendo o vetor com o FOREACH
for x in vetor:
    print( "O vetor tem o valor {}".format(x) )

    soma = soma + x

print("A soma do vetor é {}.".format(soma) )

media = soma / len(vetor)

print("A média do vetor é {}.".format(media) )

# # # # # # # # # # # # # # # # # # # # # # # #

# Funções e Classes

# Não precisa especificar tipo de parâmetro e de retorno
# def nome(parâmetro):
#   ...
def somar(a, b, c):
    print(a+b+c)
    # O retorno é opcional

# Fim da função

# Classe é a mesma coisa
class Aluno():
    nome = "Rafael"

    def metodo():
        return ""

# class Nome(Herança)

# class Aluno(Pessoa):
    # A classe Aluno "extends" a classe Pessoa
    # Código da classe
