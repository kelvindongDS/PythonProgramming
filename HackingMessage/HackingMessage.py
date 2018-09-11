

import  string

mess ='Get this message to the Kelvin Dong'

def sw(num):
    al = list(string.ascii_lowercase)
    l = []

    for i in range(1, num + 1)[::-1]:
        l.append(al[26 - i])
    for i in range(0, 26 - num):
        l.append(al[i])
    return l


def encrypt(text,num):
    al = list(string.ascii_lowercase)
    en = []
    l= sw(num)
    for letter in text.lower():
        if letter==' ': en.append(' ')
        else:
            en.append(l[al.index(letter)])
    print(al)
    print(l)

    return (''.join(en))



#testing which hacking message is appropriate
def decrypt(text):
    al = list(string.ascii_lowercase)
    for num in range(1,25):
        l = sw(num)
        en = []
        for letter in text.lower():
            if letter == ' ':
                en.append(' ')
            else:
                en.append(al[l.index(letter)])

        print('option : ', num)
        print(''.join(en))

target = encrypt(mess,16)
print('pass is : ',target)
decrypt(target)



