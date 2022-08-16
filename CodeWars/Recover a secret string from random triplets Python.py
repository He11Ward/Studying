def recoverSecret(triplets: list):
    phrase = triplets[0]
    del triplets[0]
    history_lst = []
    while True:
        pair_lst = []
        for i in range(len(phrase) - 1):
            for j in range(i+1, len(phrase)):
                if [phrase[i], phrase[j]] not in history_lst:
                    pair_lst.append([phrase[i], phrase[j]])
        if len(triplets) == 0:
            break
        for pair in pair_lst:
            for num, tri in enumerate(triplets):
                if tri[0] in phrase and tri[1] in phrase and tri[2] in phrase:
                    del triplets[num]
                    break
                if pair[0] in tri and pair[1] in tri:
                    tri = [(i, j) for i, j in enumerate(tri)]
                    for p in tri:
                        if p[1] == pair[0] or p[1] == pair[1]:
                            tri.remove(p)
                    if tri[0][0] == 0:
                        phrase.insert(phrase.index(pair[0]), tri[0][1])
                    elif tri[0][0] == 1:
                        phrase.insert(phrase.index(pair[0]) + 1, tri[0][1])
                    else:
                        phrase.insert(phrase.index(pair[1]) + 1, tri[0][1])
                    del triplets[num]
            if pair not in history_lst:
                history_lst.append(pair)
    return ''.join(phrase)


print(recoverSecret([
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]))
