import pyperclip
import random as r

with open('a.txt', 'r', encoding='utf-8') as f:
    l = f.read()
    splt = l.split(' ')
    radBold = 0
    s = ''

    for i in range(len(splt)):
        lenLett = len(splt[i]); #print(splt[i])
        radBold = r.randrange(lenLett)

        for j in range(len(splt[i])):
            if splt[i][j] in '\n"(),:-[]|>./':
                radBold = r.randrange(lenLett)
            elif j == radBold:
                s += f'**{splt[i][j]}**'; continue
            s += splt[i][j]
        s += ' '
    #with open('b.txt', 'w', encoding='utf-8') as f: f.write(s)
    print(s); pyperclip.copy(s)
