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