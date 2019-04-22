# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:08:19 2019

@author: W10
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:45:03 2019

@author: W10
"""

# EP 2019-1: Escape Insper
#
# Alunos:
# - aluno A: Thiago Pegorrer, thiagomp3@insper.edu.br
# - aluno B: André Nadalini, andrebn1@insper.edu.br

def cenarios_Ep():
    cenarios = {
        'inicio': {
            'titulo': 'saguão do Insper',
            'descrição': 'você se encontra no saguão do Insper e precisa achar o Mestre Andrew',
            'opções': {
                'segundo andar':'pegar elevador para o segundo andar',
                'fumodromo':'ir até o fumodromo',
                'Salas secretas': 'vá para a sala secreta e se teletransporte para qualquer umas das salas do jogo!'
            }
        },
        'segundo andar': {
            'titulo':'segundo andar do prédio novo',
            'descrição':'Você se encontra no segundo andar do Insper, porém o Mestre Andrew nao esta aí',
            'opções':{
                'Tobogã':'Pegar o tobogã para a sala dos professores'
            }
        },
        'fumodromo': {
            'titulo':'fumodromo do Insper',
            'descrição': 'Você adentra a misteriosa cortina de nicotina criada pelos Juuls, mas nao acha o Mestre. Eis que um Veterano te oferece um Juul da barganha',
            'opções': {
                'aceitar Juul':'Você aceita o Juul e sua visão se esfumaça',
                'inicio': 'Você ouve os conselhos de sua mae e nao aceita o Juul e volta para o Saguão do Insper'
            }
        },
        'Tobogã': {
            'titulo': 'Tobogã traiçoeiro',
            'descrição':'Voce pega o Tobogã, mas ao em vez de sair no terreo, voce se teletransporta para o Economiadas',
            'opções': {
                'Ficar bebendo': 'voce entra na Tenda e encarna o espirito do Econo',
                'inicio':'Voce resolve entrar no tobogã de novo e volta para o saguão do Insper'
            }
        },
        'Ficar bebendo':{
            'titulo': 'Já é Econo!',
            'descrição':'Você optou por esquecer o EP e ficar no Econo, atingindo o Nirvana!',
            'opções': {}
        },
        'Aceitar Juul': {
            'titulo': 'Caminho da salvação',
            'descrição': 'Ao aceitar o Juul sua visao se esfumaça e voce é guiado diretamente para o Mestre Andrew',
            'opções': {}
        },
        'Salas secretas': {
            'titulo': 'Teletransporte',
            'descrição': 'Escolha uma sala e se teletrasporte para ela',
            'opções': {
                'Inicio': 'Você volta para o saguão do Insper',
                    'segundo andar': 'Voce vai para o segundo andar',
                    'fumodromo': 'Voce é direcionado para o fumodromo',
                    'Tobogã': 'Voce entra no tobogã',
                    'Ficar bebendo': 'Voce vai para o Econo em busca da diversão',
                    'Aceitar o Juul': 'Você opta por aceitar o Juul e ir em busca de Mestre Andrew'
            }
        }
    }
    
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print ('Bem vindo ao Git')
    print ('----------------')
    print ()
    print ('Após inúmeras aulas de python, usando if, while, for,'
           'etc com o spyder você estava completamente confiante quanto'
           ' à matéria de DesSoft, pensando que o EP seria tranquilo e '
           'possível de ser feito um dia antes da entrega.')
    print ()
    print ('Porém ao abrir o pdf você se depara com algo novo, o GIT!!'
            'Assim, comça a ler as instruções e tentar fazer o projeto'
            'pórem, depois de passar mais de 3 horas e não conseguir nem'
            'clonar o diretório para o seu computador nem entender o que'
            'fazia push e pull, você resolve partir para outra abordagem,'
            'pedir ao Mestre Andrew para adiar a entrega do EP. Assim '
            'começa a sua jornada, nobre aspirante a engenheiro. Boa Sorte'
            ' e que o espírito do sábio Marcos Lisboa esteja com você.')
    avatar= (input('Qual o seu nome, nobre estudante? '))
    import random
    info_avatar={'Nome':avatar,
                 'Vida':300,
                 'Ataques':{'Ataque com airpods':30,
                            'Ataque BAITA INFRA':150}}
    cenarios, nome_cenario_atual = cenarios_Ep()
    game_over=False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        titulo=cenario_atual['titulo']
        descricao=cenario_atual['descrição']
        if titulo == 'Já é Econo':
            print("Parabéns!! Você se juntou ao Nirvana e não precisa mais se preocupar com o EP.")
            game_over = True
        elif titulo =='Aceitar o Juul':
            print('Parabéns!! Você encontrou o Mestre Andrew e por conta das'
                  'habilidades que o Juul da barganha te forneceu, você'
                  'conseguiu convencer o Mestre a adiar a entrega. A missão'
                  ' foi um sucesso')
            game_over = True
        else:
            print()
            print (titulo)
            print('-'*len(titulo))
            print(descricao)
            print()
            monstro= False
            y=random.randint(0,9)
            if y <= 3:
                monstro= True
            if monstro:
                info_monstro={'Vida':120,
                              'Ataque':50}
                print ('Você trombou o Jacaré da GV gastando a Raposa Loka e terá que '
                       'enfrentá-lo ou ser gastado pela GV pelo resto dos Econos')
                print()
                print ('Jacaré: ',info_monstro)
                print()
                print ('Você: ',info_avatar)
                t=input('Deseja lutar ou fugir? ')
                while t=='lutar' and info_monstro['Vida']>0 and info_avatar['Vida']>0:
                    print('O monstro começa atacando...')
                    x=random.randint(0,2)
                    if x==1:
                        print('O adversário tirou 50 de vida seus')
                        info_avatar['Vida']-=50
                    else:
                        print('Ataque crítico, você perdeu 100 de vida')
                        info_avatar['Vida']-=100
                    print('Vida atual: ',info_avatar['Vida'])
                    print()
                    t=input('Deseja lutar ou fugir? ')
                    print('Sua vez de atacar...')
                    z=random.randint(0,3)
                    if z==1:
                        print('Você usou o ataque com airpods e tirou 30 do jacaré')
                            info_monstro['Vida']-=30
                    elif z==2:
                        print('ataque crítico com airpods, causou 60 de dano')
                        info_monstro['Vida']-=60
                    else:
                        print('Ataque BAITA INFRA, 150 de dano!!')
                        info_monstro['Vida']-=150
                        print('Vida do Jacaré: ',info_monstro['Vida'])
                        print()
                if info_monstro['Vida']<=0:
                    print('Você derrotou o Jacaré da GV, parabéns')
                    loot=input('Deseja lootear o Jacaré (sim ou não)?')
                    if loot == 'sim':
                        consumir=input('Você achou o Zsigmond dentro do Jacaré, deseja consumi-lo?' )
                        print()
                    if consumir=='sim':
                        print('Você consumiu o corpo de um grande sábio da programação e '
                              'adquiriu as suas habilidades. Com isso, você tem o necessário'
                              'para concluir o EP e não precisa mais achar o Mestre Andrew')
                        print ('Acabou o jogo, parabens!!')
                        game_over= True
                        break
                    monstro= False
                    elif info_avatar['Vida']<=0:
                        print('Você foi derrotado!!')
                        game_over == True
                    else:
                        print('Você resolveu fugir, que vergonha')
            opcoes = cenario_atual['opções']
            for key, value in opcoes.items():
                print("{0} : {1}".format(key, value))
                print ()
            escolha = input('O que você quer fazer? ')
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print('escolha inválida')

print ('Acabou o jogo')

# Programa principal.
if __name__ == "__main__":
    main()
