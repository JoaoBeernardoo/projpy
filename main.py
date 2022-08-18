import time

def media(a=0, b=0, c=0, d=0):
    media = (a + b + c + d)/4
    print('Calculando a media...')
    time.sleep(2)
    if media > 6:
        print(f'Voce foi aprovado com a media de {media}: ')
    elif media == 6:
        print(f'Voce esta de recuperação com a media de {media}: ')
    else:
        print(f'Voce esta reprovado com a media de {media}: ')
    
    

def opçao(c=0):
    c = 'n'
    ok = str(input('Deseja ir para o menu principal? s/n  '))

    if ok == 's':
        print('Aguarde em quanto te redirecionamos para o menu principal')
    else:
        print('Opção invalida!')




galera = list()
dado = list()

c = 's'
while c == 's':

    for p in range(1,5):
        dado.append(int(input(f'qual sua nota do {p} bimestre:  ')))
    
    galera.append(dado[:])
    dado.clear

    media(dado[0], dado[1], dado[2], dado[3])
    c = str(input('Quer continuar s/n :: '))
    opçao(c)
    time.sleep(2)

print('Bem vindo ao menu')
    