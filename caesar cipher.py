spisok = 'abcdefghijklmnopqrstuvwxyz'
text = input()
k = input()
for i in text:
    if i.isalpha():
        flag = i.isupper()
        x = spisok.index(i.lower())
        y = (x + int(k)) % 26
        if flag == True:
            print(spisok[y].upper(), sep='', end='')
        else:
            print(spisok[y], sep='', end='')
    else:
        print(i, sep='', end='')