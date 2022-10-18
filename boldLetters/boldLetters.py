import pyperclip
import random as r

with open('a.txt', 'r', encoding='utf-8') as f:
    l = f.read()
    s = ""
    j = 0
    for i in range(len(l)):
        if l[i] == " ":
            s += " "
            j += 1
        elif l[i] in '(),:"-[]|>': 
            s += l[i]
            j += r.randrange(2)
        elif l[i] == "\n":
            s += "\n"
            j += r.randrange(2)
        elif i == j and not (l[i] in '(),:"-[]|>') and not (l[i] == "\n"):
            s += f'**{l[i]}**'
            j -= r.randrange(3, 6)
        else:
            #print(l[i])
            s += l[i]
            j += 2

    # with open('b.txt', 'w', encoding='utf-8') as f: f.write(s)
    print(s); pyperclip.copy(s)
