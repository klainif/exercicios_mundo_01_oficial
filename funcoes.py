import math
import random
from unidecode import unidecode


#Desafio 001 - Deixando tudo pronto.


def desafio001():
  print('Olá, mundo!')

  
#Desafio 002 - Respondendo ao Usuário.


def desafio002():
  nome = input('Digite seu nome, por favor: ').strip()
  print(f'Seja muito bem-vindo, {nome}!')


#Desafio 003 - Somando dois números.


def desafio003():
  n1 = float(input('Digite um número, por favor: '))
  n2 = float(input('Digite um número, por favor: '))
  s = (n1 + n2)
  print(f'A soma entre {n1} e {n2} é: {s}')

  
#Desafio 004 - Dissecando uma variável.


def desafio004():
  algo = input('Digite algo: ')
  print(type(algo))
  print(f'{algo} é numérico? {algo.isalnum()}') 
  print(f'{algo} é alfabético? {algo.isalpha()}')
  print(f'{algo} é ascii? {algo.isascii()}')
  print(f'{algo} é feito com dígitos? {algo.isdigit()}')
  print(f'{algo} é decimal? {algo.isdecimal()}')
  print(f'{algo} é numérico? {algo.isnumeric()}')
  print(f'{algo} é um identificador? {algo.isidentifier()}')
  print(f'{algo} é feito com letras maiúsculas? {algo.isupper()}')
  print(f'{algo} é feito com letras minúsculas? {algo.islower()}')
  print(f'{algo} é printável? {algo.isprintable()}')
  print(f'{algo} só tem espaços? {algo.isspace()}')

  
#Desafio 5 - Antecessor e Sucessor.


def desafio005():
  a = float(input('Digite um número (se houver vírgula, substitua-a por um ponto): '))
  antecessor = (a - 1)
  sucessor = (a + 1)
  print(f'O antecessor de {a} é: {antecessor}. O sucessor de {a} é: {sucessor}.')

  
#Desafio 6 - Dobro, triplo, raiz quadrada.  


def desafio006():
  n = float(input('Olá, digite um número (se houver vírgula, substitua-a por um ponto): '))
  dobro = (n * 2)
  triplo = (n * 3)
  raiz = (n ** 0.5)
  print(f'O dobro de {n} é: {dobro}. O triplo de {triplo}. A raiz quadrada de {n} é: {raiz}')


#Desafio 7 - Média aritmética.
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


def desafio007():
  n1 = float(input('Digite sua nota na matéria de Português (substitua a vírgula por um ponto, se houver): '))
  n2 = float(input('Digite sua nota na matéria de Matemática (substitua a vírgula por um ponto, se houver): '))
  m = (n1 + n2) / 2
  print(f'Sua média é: {m}')


#Desafio 8 - Conversor de medidas.


def desafio008():
  m = float(input('Digite um número: '))
  cm = (m * (10 ** -2)) 
  mm = (m * (10 ** - 3))
  print(f'O valor {m} em metros, em centímetros valerá: {cm}cm e em milímetros valerá {mm}mm.')


#Desafio 9 - Tabuada.


def desafio009():
  n = float(input('Olá, digite um número, por favor: '))
  print('A tabuada do seu número de zero a dez é: ')
  print(n * 0)
  print(n * 1)
  print(n * 2)
  print(n * 3)
  print(n * 4)
  print(n * 5)
  print(n * 6)
  print(n * 7)
  print(n * 8)
  print(n * 9)
  print(n * 10)


#Desafio 10 - Conversor de moedas.


def desafio010():
  dinheiro = float(input('Olá, digite quantos reais você tem na carteira: '))
  conversao = (dinheiro / 5.12)
  print(f'Você pode comprar {conversao} dólar(es).')


#Desafio 11 - Pintando parede.

def desafio011():
  largura = float(input('Digite a largura da sua parede: '))
  altura = float(input('Digite a altura de sua parede: '))
  area = (largura * altura)
  litros = area / 2 
  print(f'A área da sua parede é: {area}m2 e os litros necessários para pintá-la são {litros}L')


#Desafio 12 - Calculando desconto.


def desafio012():
  preço = float(input('Digite o preço do seu produto: '))
  desconto = (preço * 0.05)
  novopreço = (preço - desconto)
  print(f'O seu produto com o desconto de 5% é: {novopreço}')

  
#Desafio 13 - Reajuste salarial.

  
def desafio013():
  salario = float(input('Digite o valor do seu salário: '))
  aumento = (salario * 0.15)
  novosalario = (salario + aumento)
  print(f'O novo valor de seu salário de valor {salario}, com 15% de aumento é: {novosalario}')


#Desafio 14 - Conversor de temperaturas.
  

def desafio014():
  temperatura = float(input('Digite um valor de temperatura em graus celsius: '))
  conversao = (((temperatura / 5) * 9) + 32)
  print(f'A sua temperatura {temperatura}°C em fahrenheit é: {conversao}°F')


#Desafio 15 - Aluguel de carros.
  

def desafio015():
  km = float(input('Digite a quantidade de quilômetros percorridos: '))
  dias = float(input('Digite a quantidade de dias alugados: '))
  pagamento = (km * 0.15 + dias * 60)
  print(f'O total a se pagar é: {pagamento}')


#Desafio 16 - Quebrando um número.


def desafio016():
  n = float(input('Digite um número: '))
  nquebrado = math.trunc(n)
  print(f'O seu número {n} na porção inteira é: {nquebrado}')


#Desafio 17 - Catetos e hipotenusa


def desafio017():
  b = float(input('Digite o cateto oposto: '))
  c = float(input('Digite o cateto adjacente: '))
  h = math.hypot(b, c)
  print(f'A hipotenusa mede: {h}')

  
#Desafio 18 - Seno, cosseno e tangente.


def desafio018():
  a = float(input('Digite um número, direi seu seno, cosseno e tangente: '))
  sen = math.sin(math.radians(a))
  cos = math.cos(math.radians(a))
  tan = math.tan(math.radians(a))
  print(f'O seno de {a} é:{sen}, o cosseno de {a} é: {cos} e a tangente de {a} é: {tan}')


#Desafio 19 - Sorteando uma ordem na lista


def desafio019():
  n1 = input('Digite o nome do primeiro aluno: ')
  n2 = input('Digite o nome do segundo aluno: ')
  n3 = input('Digite o nome do terceiro aluno: ')
  n4 = input('Digite o nome do quarto aluno: ')
  lista = [n1, n2, n3, n4]
  aluno_escolhido = random.choice(lista)
  print(f'O aluno sorteado para apagar o quadro foi: {aluno_escolhido}')
  

#Desafio 20 - Sorteando uma ordem na lista.


def desafio020():
  n1 = input('Digite o nome do primeiro aluno: ')
  n2 = input('Digite o nome do segundo aluno: ')
  n3 = input('Digite o nome do terceiro aluno: ')
  n4 = input('Digite o nome do quarto aluno: ')
  lista = [n1, n2, n3, n4]
  random.shuffle(lista)
  print(f'A ordem de apresentação será: {lista}')


#Desafio 22 - Manipulando Texto.


def desafio022():
  nome = str(input('Digite seu nome, por favor: ').strip())
  dividido = nome.split()
  print(f'O seu nome com letras maiúsculas é: {nome.upper()}.')
  print(f'O se nome com letras minúsculas é: {nome.lower()}.')
  ncompleto = len(nome) - nome.count(' ')
  print(f'O seu nome possui {ncompleto} letras.')
  print(f'Seu primeiro nome é {(dividido[0])} e ele possui {len(dividido[0])} letras.')


#Desafio 23 - Separando dígitos de um número.


def desafio023():
  num = int(input('Digite um número de 0 a 9999: '))
  u = num // 1 % 10
  d = num // 10 % 10
  c = num // 100 % 10
  m = num // 1000 % 10
  print(f'O milhar de {num} é: {u}.')
  print(f'A centena de {num} é: {d}.')
  print(f'A dezena de {num} é: {c}.')
  print(f'A unidade de {num} é: {m}.')


#Desafio 24 - Verificando as primeiras letras de um texto.



def desafio024():
  cidade = str(input('Digite o nome de sua cidade: ')).strip()
  nome_cidade = cidade[:5].upper()
  if nome_cidade == 'SANTO':
    print('O primeiro nome de sua cidade é "Santo".')
  else:
    print('O primeiro nome de sua cidade não é "Santo".')


#Desafio 25 - Procurando uma string dentro de outra.


def desafio025():
  nome = str(input('Digite seu nome, por favor: ')).upper().split()
  nome_silva = 'SILVA' in nome
  if nome_silva == True:
    print('Você possui o nome "Silva"!')
  else:
    print('Você não possui o nome "Silva", mas alguém que você conhece deve ter!')


#$Desafio 26 - primeira e última ocorrência de uma string.


def desafio026():
  frase = str(input('Digite uma frase: ')).strip().upper()
  sem_acentos = unidecode(frase)
  print(f'A letra "a" na sua frase apareceu {sem_acentos.count("A")} vezes.')
  print(f'A primeira letra "a" apareceu na posição {sem_acentos.find("A")+1}.')
  print(f'A última letra "a" apareceu na posição {sem_acentos.rfind("A")+1}.')


#Desafio 27 -  primeiro e último nome de uma pessoa.


def desafio027():
  nome = str(input('Digite seu nome completo: ')).strip().split()
  print(f'Seu primeiro nome é: {nome[0]}.\nSeu último nome é: {nome[-1]}.')


#Desafio 28 - Jogo da Adivinhação v.1.0.


def desafio028():
  lista = [0, 1, 2, 3, 4, 5]
  n1 = random.choice(lista)
  n2 = float(input('Estou pensando em um número de 0 a 5. Qual você acha que foi o número que eu escolhi? '))
  if n2 == n1:
    print('Você acertou o número que eu escolhi! You win!')
  else:
    print('Você não acertou o número que eu escolhi. You lose!')


#Desafio 29 - Radar eletrônico.


def desafio029():
  km = float(input('Digite o valor da velocidade do carro (substitua a vírgula por um acento, por favor): '))
  multa = (km - 80) * 7
  if km > 80:
    print(f'Você será multado, seu rachador! Este é o valor da multa: {multa}.')
  else:
    print('Então você respeita as leis de trânsito! Muito bem! Salvando vidas! Pode seguir viagem!')


#Desafio 30 - Par ou ímpar?


def desafio030():
  numero = int(input('Digite um número inteiro, direi se ele é par ou ímpar: '))
  if numero // 2 == numero / 2:
    print(f'O número {numero} é par.')
  else:
    print(f'O número {numero} não é par.')
    

#Desafio 31 - Custo da viagem.


def desafio031():
  km = float(input('Digite o valor da sua viagem em quilômetros calcularei o preço da passagem (se houver vírgula, por favor, a substitua por um ponto): '))
  preco_viagem_curta = (km * 0.50)
  preco_viagem_longa = (km * 0.45)
  if km < 200:
    print(f'O preço a pagar será: R${preco_viagem_curta}.')
  else:
    print(f'O preço a pagar será: R${preco_viagem_longa}.')


#Desafio 32 - Ano bissexto.


def desafio032():
  ano = float(input('Digite um ano e eu direi se ele é bissexto: '))
  if ano // 4 == ano / 4:
    print('Esse ano é bissexto!')
  else:
    print('Esse ano não é bissexto!')


#Desafio 33 - Maior e menor valores.


def desafio033():
  n1 = float(input('Digite um número: '))
  n2 = float(input('Digite outro número: '))
  n3 = float(input('Digite só mais um número: '))
  print(f'O maior número digitado foi: {max(n1, n2, n3)}.')
  print(f'O menor valor digitado foi: {min(n1, n2, n3)}.')
  

#Desafio 34 - Aumentos múltiplos.


def desafio034():
  salario = float(input('Digite o valor de seu salário que calcularei seu aumento (se houverem vírgulas, por favor, substitua-a por um ponto): '))
  salario_superior = (salario * 1.10)
  salario_inferior_igual = (salario * 1.15)
  if salario <= 1250:
    print(f'O seu novo salário é: {salario_inferior_igual}.')
  else: 
    print(f'O seu novo salário é: {salario_superior}.')


#Desafio 35 - Analisando triângulo v1.0.


def desafio035():
  seg1 = float(input('Digite o comprimento do primeiro segmento: '))
  seg2 = float(input('Digite o comprimento do segundo segmento: '))
  seg3 = float(input('Digite o comprimento do terceiro segmento: '))
  if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Um triângulo pode ser formado!')
  else:
    print('Um triângulo não pode ser formado!')