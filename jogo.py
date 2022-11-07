from dev1 import *
 
lista_questoes = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'C'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]

######## aqui começa a rodar o jogo ###########

jogador = input('Olá, seja bom-vind@ ao Fortuna DesSoft. O jogo irá começar em breve. Antes disso, me informe seu nome por favor: ')

print('Aqui vai um breve manual de como nosso jogo irá funcionar.\nVocê responderá perguntas de multipla escolha de modo a acumular um prêmio maior a cada acerto seguindo a seguinte métrica:\n\n')
print('Primeiro acerto: R$1000\nSegundo acerto: R$5000\nTerceiro acerto: R$10000\nQuarto acerto: R$30000\nQuinto acerto: R$50000\nSexto acerto: R$100000\nSétimo acerto: R$300000\nOitavo acerto: R$500000\nNono acerto: R$1000000\n')
print('Seu objetivo é acertar o maior número de questões possíveis para acumular uma maior premiação. Para isso você poderá PULAR uma questão 3 vezes durante o jogo e pedir AJUDA 2 vezes. A ajuda irá te informar uma ou duas alternativas certamente erradas.')
print('Caso você erre a resposta você perde o prêmio acumulado, então gerencie bem as suas dicas e lembre-se que a qualquer momento você pode parar e sair com o prêmio acumulado até então.\n')
print('Sendo assim, boa sorte!\n')

nova_questao = True

def jogo(jogador, lista_questoes):
    incio = True

    while incio:
        lista_de_premiacoes = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
        lista_anteriores = [] #inicial
        nivel = 'facil' #inicial
        numero = 0 #inicial
        pulo = 3 #inicial
        ajuda = 2 #inicial
        nova_questao = True
        
        while nova_questao:
            if numero < 3:
                nivel = 'facil'
            elif numero >= 3 < 6:
                nivel = 'medio'
            else:
                nivel = 'dificil'
            questoes_ordenadas = transforma_base(lista_questoes)
            questoes_validadas = valida_questoes(questoes_ordenadas)
            sorteio = sorteia_questao_inedida(questoes_ordenadas, nivel, lista_anteriores)
            questao_sorteada = sorteio[0]
            lista_anteriores = sorteio[1]
            questao = questao_sorteada
            mostrar_questao = questao_para_texto(questao, numero)
            print(mostrar_questao)
            decisao_jogador = input('Digite sua resposta {0}, pular, ajuda ou parar: '.format(jogador))
            respondido = True
        
            while respondido:
                if numero < 8:
                    if decisao_jogador == 'pular':
                        if pulo > 0:
                            pulo -= 1
                            numero += 1
                            print('\033[0;36mVocê possui mais\033[m \033[1;36m{0}\033[m \033[0;36mpulos.\033[m'.format(pulo))
                            respondido = False
                        else:
                            while decisao_jogador == 'pular':
                                print('\033[0;33mOps, parece que você não tem mais pulos disponíveis.\033[m')
                                print(mostrar_questao)
                                decisao_jogador = input('Digite sua resposta {0}, pular, ajuda ou parar: '.format(jogador))
                    elif decisao_jogador == 'ajuda':
                        if ajuda > 0:
                            ajuda -= 1
                            print(gera_ajuda(questao_sorteada))
                            print(mostrar_questao)
                            print('\033[0;36mVocê possui mais\033[m \033[1;36m{0}\033[m \033[0;36majudas\033[m'.format(ajuda))
                            decisao_jogador = input('Digite sua resposta {0}, pular, ajuda ou parar: '.format(jogador))
                        else:
                            print('\033[0;33mOps, parece que você não tem mais ajudas disponíveis.\033[m')
                            print(mostrar_questao)
                            decisao_jogador = input('Digite sua resposta {0}, pular, ajuda ou parar: '.format(jogador))
                    elif decisao_jogador == 'parar':
                        decisao_final = input('{0}, seu saldo final foi de \033[1;36m{1}\033[m.\nCaso deseje jogar novamente digite jogar, caso queira parar por hoje digite encerrar: '.format(jogador, lista_de_premiacoes[numero]))
                        if decisao_final == 'jogar' or decisao_final == 'Jogar':
                            print('Okay, vamos começar novamente!')
                            nova_questao = False
                            respondido = False       
                        elif decisao_final == 'encerrar' or decisao_final == 'Encerrar':
                            return 'Obrigado por ter jogado, {0}. Espero que tenha gostado e até breve.'.format(jogador) 
                    elif decisao_jogador == 'A' or decisao_jogador == 'B' or decisao_jogador == 'C' or decisao_jogador == 'D':
                        if decisao_jogador == questao_sorteada['correta']:
                            if numero < 9:
                                numero += 1
                                print('\033[0;36mParabéns, {0}, você acertou. Seu saldo agora é de: \033[1;36mR${1}\033[m'.format(jogador, lista_de_premiacoes[numero]))
                                respondido = False
                            else:
                                print('\033[0;32mParabéns, {0}!!! Você venceu o \033[1;32mFortuna DesSoft\033[m'.format(jogador))
                                decisao_final = input('{0}, seu saldo final foi o máximo: \033[1;32m{1}\033[m.\nCaso deseje jogar novamente digite jogar, caso queira parar por hoje digite encerrar: '.format(jogador, lista_de_premiacoes[numero]))
                                if decisao_final == 'jogar' or decisao_final == 'Jogar':
                                    print('Okay, vamos começar novamente!')
                                    nova_questao = False
                                    respondido = False
                                elif decisao_final == 'encerrar' or decisao_final == 'Encerrar':
                                    return 'Obrigado por ter jogado, {0}. Meus parabéns novamente. Espero que tenha gostado e até breve.'.format(jogador)
                        if decisao_jogador != questao_sorteada['correta']:
                            print('\033[0;31mInfelizmente esta não era a resposta certa, {0}. Seu saldo final foi de: \033[1;31mR${1}\033[m'.format(jogador, lista_de_premiacoes[numero]))
                            decisao_final = input('{0}, seu saldo final foi de \033[1;36m{1}\033[m.\nCaso deseje jogar novamente digite jogar, caso queira parar por hoje digite encerrar: '.format(jogador, lista_de_premiacoes[numero]))
                            if decisao_final == 'jogar':
                                print('Okay, vamos começar novamente!')
                                nova_questao = False
                                respondido = False
                            elif decisao_final == 'encerrar' or decisao_final == 'Encerrar':
                                return 'Obrigado por ter jogado, {0}. Espero que tenha gostado e até breve.'.format(jogador)
                else:
                    print('\033[1;32mParabéns!!! Você venceu o Fortuna DesSoft\033[m')
                    decisao_final = input('\033[1;32m{0}, seu saldo final foi de {1}.\033[m Caso deseje jogar novamente digite jogar, caso queira parar por hoje digite encerrar: '.format(jogador, lista_de_premiacoes[numero + 1]))
                    if decisao_final == 'jogar' or decisao_final == 'Jogar':
                        print('Okay, vamos começar novamente!')
                        nova_questao = False
                        respondido = False
                    elif decisao_final == 'encerrar' or decisao_final == 'Encerrar':
                        return 'Obrigado por ter jogado, {0}. Meus parabéns novamente. Espero que tenha gostado e até breve.'.format(jogador)
 
jogar = input('{0}, deseja iniciar um novo jogo agora? [sim/nao]\n'.format(jogador))

if jogar == 'sim':
    y = jogo(jogador, lista_questoes)
    print(y)
else:
    print('Okay, até breve!')