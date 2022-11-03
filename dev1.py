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

def valida_questoes(questoes_por_nivel):
    lista_problemas = []

    for i in range(len(questoes_por_nivel)):
        y = valida_questao(questoes_por_nivel)
        if y == {}:
            lista_problemas.append({})
        else:
            lista_problemas.append(y)
    
    return lista_problemas


def sorteia_questao_inedida(questoes_por_nivel, nivel, lista_anteriores):
    
    sorteado = {}

    for i, j in questoes_por_nivel.items():
        if i == nivel:
            sorteado = random.choice(j)
            for k in range(len(lista_anteriores)):
                if lista_anteriores[k] == sorteado:
                    sorteado = random.choice(j)
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

    return ('----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}\n'.format(numero + 1, titulo, A, B, C, D))

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
        return '\033[0;36m\nDICA:\nOpções certamente erradas: {0} | {1}\033[m'.format(dica[0], dica[1])
    elif len(dica) == 1:
        return '\033[0;36m\nDICA:\nOpções certamente erradas: {0}\033[m'.format(dica[0])