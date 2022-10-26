print('Ismael R. Silva')

def transforma_base(l):
    dic = {}

    for i in range(len(l)):
        for j, k in l[i].items():
            if j == 'nivel':
                if k not in dic.keys():
                    dic[k] = []
                    dic[k].append(l[i])
                elif k in dic.keys():
                    dic[k].append(l[i])
    
    return dic

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


def valida_questoes(questoes):
    lista_problemas = []

    for i in range(len(questoes)):
        x = valida_questao(questoes[i])
        lista_problemas.append(x)
    
    return lista_problemas


import random

def sorteia_questao(dic, nivel):
    sorteado = {}

    for i, j in dic.items():
        if i == nivel:
            sorteado = random.choice(j)
    return sorteado