from random import choice

cont = 0

mudando = input('Deseja que haja mudança na escolha? ')

for x in range(1000):

    portas = [1, 2, 3]

    # seleciona uma porta aleatoria para ser a porta com o carro
    carro = choice(portas)

    # seleciona uma porta aleatoria para ser a porta escolhida pelo participante
    participante = choice(portas)

    apresentador = 0

    # testa se a porta com o carro é igual ou diferente da porta do participante para o apresentador escolher
    if carro == participante or carro != participante:
        apresentador = choice(portas)

        # repete a escolha até ser diferente da porta escolhida pelo participante ou com o carro
        if apresentador == carro or apresentador == participante:
            while apresentador == carro or apresentador == participante:
                apresentador = choice(portas)

    # testa quantas vezes o participante ganhou o carro sem mudar de escolha
    if mudando == 'nao':
        if carro == participante:
            cont += 1

    elif mudando == 'sim':

        # remove a porta escolhida pelo apresentador e a anteriomente escolhida
        # para facilitar a nova escolha
        portas.remove(apresentador)

        portas.remove(participante)

        nova_escolha = choice(portas)

        # testa quantas vezes o participante ganhou o carro mudando de escolha
        if carro == nova_escolha:
            cont += 1

print(f'Em 1000 testes o participante ganha {cont} vezes')







