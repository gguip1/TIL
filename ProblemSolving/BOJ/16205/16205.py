import sys

case, word = sys.stdin.readline().strip().split()

if case == '1':
    print(word)
    for w in word:
        if w.isupper():
            print(f'_{w.lower()}', end='')
        else:
            print(w, end='')
    print()
    for index, w in enumerate(word):
        if index == 0:
            print(w.upper(), end='')
        else:
            print(w, end='')
    print()
elif case == '2':
    for i, w in enumerate(word.split('_')):
        if i == 0:
            print(w, end='')
        else:
            w_list = list(w)
            w_list[0] = w_list[0].upper()
            w = "".join(w_list)
            print(w, end='')
    print()
    print(word)
    for i, w in enumerate(word.split('_')):
        w_list = list(w)
        w_list[0] = w_list[0].upper()
        w = "".join(w_list)
        print(w, end='')
    print()
elif case == '3':
    for index, w in enumerate(word):
        if index == 0:
            print(w.lower(), end='')
        else:
            print(w, end='')
    print()
    for index, w in enumerate(word):
        if index == 0:
            print(w.lower(), end='')
        elif w.isupper():
            print(f'_{w.lower()}', end='')
        else:
            print(w, end='')
    print()
    print(word)
