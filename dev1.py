import random

print('Ismael R. Silva')

def transforma_base(lista_de_questoes):
    questoes_por_nivel = {}

    for i in range(len(lista_de_questoes)):
        for j, k in lista_de_questoes[i].items():
            if j == 'nivel':
                if k not in questoes_por_nivel.keys():
                    questoes_por_nivel[k] = []
                    questoes_por_nivel[k].append(lista_de_questoes[i])
                elif k in questoes_por_nivel.keys():
                    questoes_por_nivel[k].append(lista_de_questoes[i])
    
    return questoes_por_nivel

def valida_questao(questao):

    validacao = {}

    # titulo
    if 'titulo' not in questao.keys():
        validacao['titulo'] = 'nao_encontrado'

    else:
        if questao['titulo'] == '' or questao['titulo'].isspace():
            validacao['titulo'] = 'vazio'

    # nivel
    if 'nivel' not in questao.keys():
        validacao['nivel'] = 'nao_encontrado'

    else:
        if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
            validacao['nivel'] = 'valor_errado'

    # opcoes
    if 'opcoes' not in questao.keys():
        validacao['opcoes'] = 'nao_encontrado'

    elif len(questao['opcoes']) != 4:
        validacao['opcoes'] = 'tamanho_invalido'

    elif len(questao['opcoes']) == 4:
        for i in questao['opcoes'].keys():
            if i != 'A' and i != 'B' and i != 'C' and i != 'D':
                validacao['opcoes'] = 'chave_invalida_ou_nao_encontrada'


    for g, h in questao.items():
        if g == 'opcoes':
            for m, n in h.items():
                if type(n) == str:
                    zz = list(n)
                    if n.endswith(' ') or '\t' in zz:
                        if 'opcoes' not in validacao.keys():
                            validacao['opcoes'] = {}
                            validacao['opcoes'][m] = 'vazia'
                        else:
                            validacao['opcoes'][m] = 'vazia'


    # correta
    if 'correta' not in questao.keys():
        validacao['correta'] = 'nao_encontrado'

    elif 'correta' in questao.keys():
        for j, k in questao.items():
            if j == 'correta':
                if k != 'A' and k != 'B' and k != 'C' and k != 'D':
                    validacao['correta'] = 'valor_errado'

    # questao
    if len(questao) != 4:
        validacao['outro'] = 'numero_chaves_invalido'

    return validacao

lista_problemas = {}
def valida_questoes(questoes_por_nivel):

    for i in range(len(questoes_por_nivel)):
        que = valida_questao(questoes_por_nivel[i])
        lista_problemas.append(que)
    
    return lista_problemas


def sorteia_questao_inedida(questoes_por_nivel, nivel, lista_anteriores):
    
    sorteado = {}

    for i, j in questoes_por_nivel.items():
        if i == nivel:
            sorteado = random.choice(j)
            for k in range(len(lista_anteriores)):
                if lista_anteriores[k] == sorteado:
                    random.choice(j)
                    k = 0
            lista_anteriores.append(sorteado)
    
    sorteios = [sorteado, lista_anteriores]
    return sorteios

def questao_para_texto(questao_sorteada, numero):
    titulo = questao_sorteada['titulo']
    A = questao_sorteada['opcoes']['A']
    B = questao_sorteada['opcoes']['B']
    C = questao_sorteada['opcoes']['C']
    D = questao_sorteada['opcoes']['D']

    return ('----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}\n'.format(numero, titulo, A, B, C, D))

def gera_ajuda(questao_sorteada):
    correta = questao_sorteada['correta']
    lista_incorretas = []
    dica = []

    for i, j in questao_sorteada['opcoes'].items():
        if i != correta:
            lista_incorretas.append(j)

    n = [1, 2]
    qt = random.choice(n)

    k = 0
    while k < qt:
        dica.append(random.choice(lista_incorretas))
        k += 1

    if len(dica) == 2:
        return 'DICA:\nOpções certamente erradas: {0} | {1}'.format(dica[0], dica[1])
    elif len(dica) == 1:
        return 'DICA:\nOpções certamente erradas: {0}'.format(dica[0])


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
          'correta': 'B'},

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
print('Primeiro acerto: R$1000\nSegundo acerto: R$5000\nTerceiro acerto: R$10000\nQuarto acerto: R$30000\nQuinto acerto: R$50000\nSexto acerto: R$100000\nSétimo acerto: R$300000\nOitavo acerto: R$500000\nNono acerto: R$1000000')
print('Seu objetivo é acertar o maior número de questões possíveis para acumular uma maior premiação. Para isso você poderá PULAR uma questão 3 vezes durante o jogo e pedir AJUDA 2 vezes. A ajuda irá te informar uma ou duas alternativas certamente erradas.')
print('Caso você erre a resposta você perde o prêmio acumulado, então gerencie bem as suas dicas e lembre-se que a qualquer momento você pode parar e sair com o prêmio acumulado até então.')
print('Sendo assim, boa sorte!')

nova_questao = True

def jogo(jogador):

    lista_de_premiacoes = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    lista_anteriores = [] #inicial
    nivel = 'facil' #inicial
    numero = 0 #inicial
    pulo = 3 #inicial
    ajuda = 2 #inicial
    nova_questao = True

    numero += 1
    questoes_ordenadas = transforma_base(lista_questoes)
        
    sorteio = sorteia_questao_inedida(questoes_ordenadas, nivel, lista_anteriores)
    questao_sorteada = sorteio[0]
    lista_anteriores = sorteio[1]
    mostrar_questao = questao_para_texto(questao_sorteada, numero)
    decisao_jogador = ('Digite sua resposta {0}, pular, ajuda ou parar: '.format(jogador))

    while decisao_jogador == 'pular':
        if pulo > 0:
            pulo -= 1
            nova_questao = True
        else:
            print('Ops, parece que você não tem mais pulos disponíveis.')
            print(mostrar_questao)
            print(decisao_jogador)
    while decisao_jogador == 'ajuda':
        if ajuda > 0:
            ajuda -= 1
            print(gera_ajuda(questao_sorteada))
            print(mostrar_questao)
            print(decisao_jogador)
        else:
            print('Ops, parece que você não tem mais ajudas disponíveis.')
            print(mostrar_questao)
            print(decisao_jogador)
    while decisao_jogador == 'parar':
        decisao_final = input('{0}, seu saldo final foi de {1}. Caso deseje jogar novamente digite jogar, caso queira parar por hoje digite encerrar: '.format(jogador, lista_de_premiacoes(numero)))
        if decisao_final == 'jogar' or decisao_final == 'Jogar':
            print('Okay, vamos começar novamente!')
        elif decisao_final == 'encerrar' or decisao_final == 'Encerrar':
            return 'Obrigado por ter jogado, {0}. Espero que tenha gostado e até breve.'.format(jogador) 
    while decisao_jogador == 'A' or decisao_jogador == 'B' or decisao_jogador == 'C' or decisao_jogador == 'D':
        if decisao_jogador == questao_sorteada['correta']:
            print('Parabens, {0}, você acertou. Seu saldo agora é de: R${1}'.format(jogador, lista_de_premiacoes[numero]))

print(jogo(jogador))