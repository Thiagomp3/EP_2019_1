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
                'fumodromo':'ir até o fumodromo'
            }
        },
        'segundo andar': {
            'titulo':'segundo andar do prédio novo',
            'descrição':'Você se encontra no segundo andar do Insper, porem o Mestre Andrew nao esta ai',
            'opções':{
                'Tobogã':'Pegar o tobogã para a sala dos professores'
            }
        },
        'fumodromo': {
            'titulo':'fumodromo do Insper',
            'descrição': 'Você adentra a misteriosa cortina de nicotina criada pelos Juuls, mas nao acha o Mestre. Eis que um Veterano te oferece um Juul da barganha',
            'opcões': {
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
        }
    }
    
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
