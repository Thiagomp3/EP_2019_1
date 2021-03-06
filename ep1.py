# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:08:19 2019
@author: W10
"""

# EP 2019-1: Escape Insper
#
# Alunos:
# - aluno A: Thiago Pegorrer, thiagomp3@insper.edu.br
# - aluno B: André Nadalini, andrebn1@insper.edu.br
import json

def cenarios_Ep():
    with open("dicionario_arquivo.txt", 'r') as cenario:
        cenario_dict=json.load(cenario)
    cenarios=cenario_dict

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

Inventário= {"Airpods": {"descrição":"par de fones padrão InsperBoy","dano":30},
             "MacBook":{"descrição":"tal ferramenta permite que você tenha acesso a qualquer momento do EP"}
        }
          
        


def main():
    print ("Bem vindo ao Git")
    print ("----------------")
    print ()
    print ("Após inúmeras aulas de python, usando if, while, for,"
           "etc com o spyder você estava completamente confiante quanto"
           " à matéria de DesSoft, pensando que o EP seria tranquilo e "
           "possível de ser feito um dia antes da entrega.")
    print ()
    print ("Porém ao abrir o pdf você se depara com algo novo, o GIT!!"
            "Assim, comça a ler as instruções e tentar fazer o projeto"
            "pórem, depois de passar mais de 3 horas e não conseguir nem"
            "clonar o diretório para o seu computador nem entender o que"
            "fazia push e pull, você resolve partir para outra abordagem,"
            "pedir ao Mestre Andrew para adiar a entrega do EP. Assim "
            "começa a sua jornada, nobre aspirante a engenheiro. Boa Sorte"
            " e que o espírito do sábio Marcos Lisboa esteja com você.")
    print()
    chave=False
    avatar= (input("Qual o seu nome, nobre estudante? "))
    import random
    info_avatar={"Nome":avatar,
                 "Vida":300,
                 "Ataques":{"Ataque com airpods":30,
                            "Ataque BAITA INFRA":150}}
    cenarios, nome_cenario_atual = cenarios_Ep()
    game_over=False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        titulo=cenario_atual["titulo"]
        descricao=cenario_atual["descrição"]
        monstro= False
        y=random.randint(0,9)
        if y <= 2:
            monstro= True
        if monstro:
            info_monstro={"Vida":120,
                          "Ataque":50}
            print ("Você trombou o Jacaré da GV gastando a Raposa Loka e terá que "
                    "enfrentá-lo ou ser gastado pela GV pelo resto dos Econos")
            print()
            print ("Jacaré: ",info_monstro)
            print()
            print ("Você: ",info_avatar)
            t=input("Deseja lutar ou fugir? ")
            while t=="lutar" and info_monstro["Vida"]>0 and info_avatar["Vida"]>0:
                print("O monstro começa atacando...")
                x=random.randint(0,2)
                if x==1:
                    print("O adversário tirou 50 de vida seus")
                    info_avatar["Vida"]-=50
                else:
                    print("Ataque crítico, você perdeu 100 de vida")
                    info_avatar["Vida"]-=100
                print("Vida atual: ",info_avatar["Vida"])
                print()
                t=input("Deseja lutar ou fugir? ")
                print("Sua vez de atacar...")
                z=random.randint(0,3)
                if z==1:
                    print("Você usou o ataque com airpods e tirou 30 do jacaré")
                    info_monstro["Vida"]-=30
                elif z==2:
                    print("ataque crítico com airpods, causou 60 de dano")
                    info_monstro["Vida"]-=60
                else:
                    print("Ataque BAITA INFRA, 150 de dano!!")
                    info_monstro["Vida"]-=150
                    print("Vida do Jacaré: ",info_monstro["Vida"])
                    print()
                if info_monstro["Vida"]<=0:
                    print("Você derrotou o Jacaré da GV, parabéns")
                    loot=input("Deseja lootear o Jacaré (sim ou não)?")
                    if loot == "sim":
                        m=random.randint(0,5)
                        if m==1:
                            consumir=input("Você achou o Zsigmond dentro do Jacaré, deseja consumi-lo?" )
                            print()
                            if consumir=="sim":
                                print("Você consumiu o corpo de um grande sábio da programação e"
                                      "adquiriu as suas habilidades. Com isso, você tem o necessário"
                                      "para concluir o EP e não precisa mais achar o Mestre Andrew")
                                print()
                                print()
                                print("Acabou o jogo, parabens!!")
                                game_over= True
                                monstro= False
                                break
                        elif m>1:
                            print ("Voce encontrou um kit médico")
                            Inventário["Kit médico"]={"descrição":"Use para recuperar sua vida"}
                        else:
                            print("infelizmente voce nao encontrou nada")
                    monstro=False    
                elif info_avatar["Vida"]<=0:
                    print("Você foi derrotado!!")
                    game_over = True
                    break 
                else:
                    print("Você resolveu fugir, que vergonha")
        if cenario_atual["titulo"] == "Já é Econo!":
            print("Você optou por ficar bebendo no Econo atingindo o Nirvana!!.")
            game_over = True
            print ("O jogo acabou!!")
            break
        else:
            print()
            print (titulo)
            print("-"*len(titulo))
            print(descricao)
            print()
            if titulo=="fumodromo do Insper":
                print("Voce encontrou um Juul") 
                Inventário["Juul"]={"descrição":"Esse item pode ser usado para realizar trocas"}
                chave=True
            elif titulo=="Trono dos Deuses":
                if chave:
                    print("Com muito respeito, você suplica ao Mestre por um adiamento do EP")
                    print()
                    print("O Mestre pede algo em troca e você oferece o Juul do Mestre Supremo")
                    print()
                    print("Ele aceita o presente e você consegue um adiamento!")
                    print("Parabens!!! Você atingiu seu objetivo!")
                    game_over=True
                    break  
                elif not chave:
                    print("Com muito respeito você suplica ao mestre por um adiamento no ep")
                    print()
                    print("O Mestre promete um adiamento caso você consiga recuperar o Juul do Mestre Supremo que ele deseja") 
            opcoes = cenario_atual["opções"]
            print ()
            print("Opções: ")
            for key, value in opcoes.items():
                print("{0} : {1}".format(key, value))
            print("Abrir inventário : veja seus itens")
            print()
            escolha = input("O que fazer? ")
            if escolha in opcoes:
                nome_cenario_atual = escolha
            elif escolha=="Sujinhuus":
                nome_cenario_atual = "Salas secretas"
            elif escolha=="Abrir inventário":
                for key, value in Inventário.items():
                    print ("{0} : {1}".format(key, value))
                print()
                u=input("Item que deseja usar/voltar: ")
                if u == "Kit médico":
                    print ("Vida recuperada")
                    info_avatar["Vida"]=300
                elif u=="voltar":
                    print()
                elif u=="Breja do Sujinhuus":
                    print("Breja geladinha aumentou sua vitalidade")
                    info_avatar["Vida"]=400
                else:
                    print("nenhum item que pode ser utilizável com esse nome")   
                         
            else:
                print("escolha inválida")



# Programa principal.
if __name__ == "__main__":
    main()