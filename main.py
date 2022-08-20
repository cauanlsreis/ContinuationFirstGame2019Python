import random

mapa1 = [
    "---------------",
    "|  +++++++++  |",
    "| + -9-     + |",
    "| +         + |",
    "| +         + |",
    "| +         + |",
    "------| |------",
]

mapa2 = [
    "---------------",
    "|<           >|",
    "@             @",
    "|<           >|",
    "@             @",
    "|<           >|",
    "------| |------",
]

mapa3 = [
    "------| |------",
    "|<           >|",
    "@             @",
    "|<           >|",
    "@             @",
    "|<           >|",
    "---------------",
]

quarto01 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| (    &    )_|",
    "| (           @",
    "| (    &    )-|",
    "| (.... ....) |",
    "--------------",
]
quarto02 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| ( &       )_|",
    "| (           @",
    "| (       & )-|",
    "| (.... ....) |",
    "--------------",
]

quarto03 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| (       & )_|",
    "| (           @",
    "| ( &       )-|",
    "| (.... ....) |",
    "--------------",
]

quarto04 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| (         )_|",
    "| (    &      @",
    "| (    &    )-|",
    "| (.... ....) |",
    "--------------",
]

quarto05 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| (   &  &  )_|",
    "| (           @",
    "| (         )-|",
    "| (.... ....) |",
    "--------------",
]

quarto06 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| (         )_|",
    "| (           @",
    "| (   &  &  )-|",
    "| (.... ....) |",
    "--------------",
]

quarto07 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| (&        )_|",
    "| (           @",
    "| (&        )-|",
    "| (.... ....) |",
    "--------------",
]

quarto08 = [
    "---------------",
    "|  >>>>+<<<<  |",
    "| (        &)_|",
    "| (           @",
    "| (        &)-|",
    "| (.... ....) |",
    "--------------",
]

suspeitos = [{"Nome:": "Anúbis",
              "Características:": ":",
              "Altura": "Alto",
              "Sexo": "Masculino",
              "Cor da pele": "Preto",
              "Acessório": "Bracelete",
              "Acessório2": "Brincos",
              },

             {"Nome:": "Hórus",
              "Características:": ":",
              "Altura": "Alto",
              "Sexo": "Masculino",
              "Cor da pele": "Marrom",
              "Acessório": "Colar",
              "Acessório2": "Bracelete"},

             {"Nome:": "Seth",
              "Características "
              "Altura": "Baixo",
              "Sexo": "Masculino",
              "Cor da pele": "Marrom",
              "Acessório": "Brincos",
              "Acessório2": "Colar"},

             {"Nome:": "Rá",
              "Características:": ":",
              "Altura": "Média",
              "Sexo": "Masculino",
              "Cor da pele": "Amarela",
              "Acessório": "Bracelete",
              "Acessório2": "Colar"},

             {"Nome:": "Bastet",
              "Características:": ":",
              "Altura": "Média",
              "Sexo": "Feminino",
              "Cor da pele": "Amarela",
              "Acessório": "Colar",
              "Acessório2": "Bracelete"},

             {"Nome:": "Ísis",
              "Características:": ":",
              "Altura": "Baixa",
              "Sexo": "Feminino",
              "Cor da pele": "Preto",
              "Acessório": "Brincos",
              "Acessório2": "Colar"},

             {"Nome:": "Sekhmet",
              "Características:": ":",
              "Altura": "Média",
              "Sexo": "Feminino",
              "Cor da pele": "Marrom",
              "Acessório": "Brincos",
              "Acessório2": "Bracelete"}, ]

locais = [{
   "Quarto de RÁ" :"– quarto número 789"},
   {"Quarto de SETH" :  "- quarto número 456"},
   {"Quarto de ISÍS" : "– quarto de número 123"},
   {"Quarto de SEKHMET" : "– quarto número 189"},
   {"Quarto de HÓRUS" : "– quarto número 246"},
   {"Quarto de ANÚBIS" : "– quarto número 323"},
   {"Quarto de BASTET" :  "- quarto número 471"},
   {"Quarto de OSÍRIS" : "quarto número 592"}, ]

armas = [{"FOICE:" " Cor": "Preto", "Tipo0": "Cortante", "Símbolo0": "Ouroboro"},
{"ADAGA:" " Cor": "Ouro","Tipo01": "Cortante","Símbolo01": "Escaravelho"},
{"BASTÃO:" " Cor":"Branco", "Tipo02": "Nociva", "Símbolo02": "Ouroboros"},
{"CHICOTE:" " Cor": "Preto", "Tipo03": "Nociva", "Símbolo03":"Escaravelho"},
{"LANÇA:" " Cor": "Ouro", "Tip04": "Perfurante", "Símbolo04": "Ouroboros"},
{"CAJADO DA MORTE:" " Cor": "Preto", "Tipo05": "Nociva", "Símbolo05": "Amenta"},
{"ANKH PERFURANTE:" " Cor": "Branco", "Tipo06": "Perfurante", "Símbolo06": "Escaravelhovo"},
{"ARCO E FLECHAS:" " Cor": "Ouro", "Tipo07": "Perfurante", "Símbolo07": "Amenta"},
]

dicas = []
mapa0 = mapa1

print("\nVocê é o servo mais confiável dos deuses do Egito.")
print("Um deus foi achado morto na pirâmide Divina em meio a uma comemoração após a vida na Terra ser exterminada!")
print("Você foi confiado pelos deuses para achar o assassino, a arma utilizada no assassinato e o quarto da morte.\n")
print("\n                       LEGENDA:"
      "\n                -9- - CORPO DE OSÍRIS"
      "\n                    & - SERVOS"
      "\n                   ? - DETETIVE"
      "\n                   || - SAÍDAS"
      "\n                    @ - PORTAS\n")


def exibe_mapa(mapa0):
    for linha in mapa0:
        print(linha)


def exibe_mapa_personagem(mapa0, px, py):
    for l, linha in enumerate(mapa0):
        print(l, end='')
        for c, coluna in enumerate(linha):
            if px == c and py == l:
                print("?", end='')
            else:
                print(coluna, end='')
        print()

chances = 0
def exibe_menu():
    print("********** MENU DE AÇÕES **********")
    print("1 - CIMA")
    print("2 - BAIXO")
    print("3 - DIREITA")
    print("4 - ESQUERDA")
    print("5 - OLHAR DICAS")
    print("6 - OLHAR FICHAS DOS SUSPEITOS")
    print("7 - OLHAR FICHA DE ARMAS SUSPEITAS")
    print("8 - OLHAR FICHA DE QUARTOS")
    print("9 - EXILAR O ASSASSINO ENCONTRADO")
    opcao = int(
        input("Vasculhe as  pirâmide embusca de pistas! Digite o que você quer fazer: "))
    return opcao


def exibe_menu_exilar():
    print("********** MENU DE EXÍLIO **********")
    print("0 - VOLTAR AO MENU ANTERIOR")
    print("1 - Anúbis")
    print("2 - Hórus")
    print("3 - Seth")
    print("4 - Rá")
    print("5 - Bastet")
    print("6 - Ísis")
    print("7 - Sekhmet")
    opcao2 = int(input("Digite qual o assassino descoberto para exilá-lo do mundo místico: "))
    return opcao2


px = 7
py = 3
mapa0 = mapa1
exibe_mapa(mapa0)
exibe_mapa_personagem(mapa0, px, py)
Verdadeiro = 0

while Verdadeiro == 0:
    opcao = exibe_menu()
    if opcao == 1:
        py = py - 1
        if py < 0:
            py = 0
    if opcao == 2:
        py = py + 1

    if opcao == 3:
        px = px + 1
    if opcao == 4:
        px = px - 1

    if opcao == 5:
        print(dicas)

    if opcao == 6:
        for j in range(len(suspeitos)):
            print(suspeitos[j])
    if opcao == 7:
        for k in range(len(armas)):
            print(armas[k])
    if opcao == 8:
        for l in range(len(locais)):
            print(locais[l])
    # Falta a opcao 7 olha no menu
    # Falta a opcao 8 olha no menu

        if opcao == 9:
            opcao2 = exibe_menu_exilar()
            if opcao2 == 0:
                opcao2 = exibe_menu()
                chances = 0
    opcao2 = exibe_menu_exilar()
    if opcao2 == 5:
        print("************* PARABÉNS, VOCÊ ACERTOU E VENCEU! *************")

    if opcao2 != 5 and opcao2 != 0:
        print("************* VOCÊ PERDEU! *************\n"
                         "OBRIGADO POR JOGAR!")
        chances = chances + 1
        if chances > 2:
            break



    # Pra achar o corpo de Osíris.
    if py == 2 and px == 5:
        print("Você encontrou o corpo de Osíris")

    # Pra entrar no 1º corredor de quartos!
    if py == 6 and px == 7:
        mapa0 = mapa2
        py = 1
        px = 7
        print("Você chegou no 1º corredor de quartos!")

        # Pra entrar no quarto 1 do 1º corredor de quartos!
        if py == 2 and px == 0:
            mapa0 = quarto01
            py = 3
            px = 13
            print("Você entrou no quarto de Rá, número 789")
            print("Vá interrogar os servos '&' atrás de dicas!")
            exibe_mapa_personagem(mapa0, px, py)


        # Pra entrar no quarto 2 do 1º corredor de quartos!
        if py == 4 and px == 0:
            mapa0 = quarto02
            print("Você entrou no quarto de Seth, número 456")
            print("Vá interrogar os servos '&' atrás de dicas!")
            py = 3
            px = 13
            exibe_mapa_personagem(mapa0, px, py)

            if py == 3 and px == 13:
                mapa0 = mapa2
                print("Você chegou no 1º corredor de quartos!")
                py = 4
                px = 0
                exibe_mapa_personagem(mapa0, px, py)

        # Pra entrar no quarto 3 do 1º corredor de quartos!
        if py == 2 and px == 13:
            mapa0 = quarto03
            print("Você entrou no quarto de Isís, número 123")
            print("Vá interrogar os servos '&' atrás de dicas!")
            py = 3
            px = 13
            exibe_mapa_personagem(mapa0, px, py)

            if py == 3 and px == 14:
                mapa0 = mapa2
                print("Você chegou no 1º corredor de quartos!")
                py = 2
                px = 13
                exibe_mapa_personagem(mapa0, px, py)

        # Pra entrar no quarto 4 do 1º corredor de quartos!
        if py == 4 and px == 13:
            mapa0 = quarto04
            print("Você chegou no quarto de Sekhmet, número 189")
            print("Vá interrogar os servos '&' atrás de dicas!")
            py = 3
            px = 13
            exibe_mapa_personagem(mapa0, px, py)

            if py == 3 and px == 14:
                print("Você chegou no 1º corredor de quartos!")
                py = 1
                px = 7
                exibe_mapa_personagem(mapa0, px, py)

        # Pra entrar no 2º corredor de quartos!
        if mapa0 == mapa2:
            if py == 6 and px == 7:
                mapa0 = mapa3
                print("Você chegou no 2º corredor de quartos!")
                exibe_mapa_personagem(mapa0, px, py)

            # Pra entrar no quarto 5 do 2º corredor de quartos!
            if mapa0 == mapa3:
                if mapa0 == mapa3 and py == 2 and px == 0:
                    mapa0 = quarto05
                    print("Você entrou no quarto de Hórus, número 246")
                    print("Vá interrogar os servos '&' atrás de dicas!")
                    py = 3
                    px = 13
                    exibe_mapa_personagem(mapa0, px, py)

                    if py == 3 and px == 14:
                        mapa0 = mapa2
                        print("Você chegou no 2º corredor de quartos!")
                        py = 1
                        px = 7
                        exibe_mapa_personagem(mapa0, px, py)

                # Pra entrar no quarto 6 do 2º corredor de quartos!
                if mapa0 == mapa3 and py == 4 and px == 0:
                    mapa0 = quarto06
                    print("Você entrou no quarto de Anúbis, número 323")
                    print("Vá interrogar os servos '&' atrás de dicas!")
                    py = 3
                    px = 13
                    exibe_mapa_personagem(mapa0, px, py)

                    if py == 3 and px == 14:
                        mapa0 = mapa3
                        print("Você chegou no 2º corredor de quartos!")
                        py = 1
                        px = 7
                        exibe_mapa_personagem(mapa0, px, py)

                # Pra entrar no quarto 7 do 2º corredor de quartos!
                if mapa0 == mapa3 and py == 2 and px == 14:
                    mapa0 = quarto07
                    print("Você entrou no quarto de Bastet, número 471")
                    print("Vá interrogar os servos '&' atrás de dicas!")
                    py = 3
                    px = 13
                    exibe_mapa_personagem(mapa0, px, py)

                    if py == 3 and px == 14:
                        mapa0 = mapa3
                        print("Você chegou no 2º corredor de quartos!")
                        py = 1
                        px = 7
                        exibe_mapa_personagem(mapa0, px, py)

                # Pra entrar no quarto 8 do 2º corredor de quartos!
                if mapa0 == mapa3 and py == 4 and px == 14:
                    mapa0 = quarto08
                    print("Você chegou no quarto de Osíris, número 572")
                    print("Vá interrogar os servos '&' atrás de dicas!")
                    py = 3
                    px = 13
                    exibe_mapa_personagem(mapa0, px, py)

                    if py == 3 and px == 14:
                        print("Você chegou no 2º corredor de quartos!")
                        py = 1
                        px = 7
                        exibe_mapa_personagem(mapa0, px, py)

    exibe_mapa_personagem(mapa0, px, py)