#-------------Dosya okuma-------------
import json

colors= {
    'Red': "kırmızı",
    'green': "yeşil",
    'blue': "mavi",
    'orange': "turuncu",
    'purple': "mor",

}
with open('colors.json','w', encoding='utf-8') as f:
    json.dump(colors,f, ensure_ascii=False, indent=4)

with open('colors.json','r', encoding='utf-8') as f:
    data=json.load(f)
print(data)


#text file'a yazıp silme- write text line by line
colors= {"red","green","blue","yellow","orange","purple"}

with open('colors.txt','w', encoding='utf-8') as f:
    f.write("hello world" + '\n')
    for color in colors:
        f.write(color + '\n')

import random
def createPassword(length):
    password =""
    for i in range(length):
        password += random.choice("asdfghjklkjhgfdsasxcvbnlkjhgfds")
    return password
passwords =(createPassword(random.randrange(5,15)) for i in range(10000))

with open('passwords.txt','w', encoding='utf-8') as f:
    for password in passwords:
        f.write(password + '\n')

with open('passwords.txt','w', encoding='utf-8') as f:
    lines= f.readline()
    lines=[line.strip() for line in lines]

    print(lines[0])
    print(lines[1])

liste ={
    [1,2,3,4,5],
    [4,5,6,1],
    [1,2,3]
}
print(liste)
print(len(liste))
print(len(liste[0]))
print(liste[0])
print(liste[0][0])
print(liste[-1])
print(liste[-1][-1])

#listenin tüm elemanlarını ekrana teker teker print ediniz.
def printList(liste):
    for i in liste:
        for j in i:
            print(j)

def increaseList(liste):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            liste[i][j] += 1
        return liste

def reversePrint(liste):
    print([i[::-1]] for i in liste [::-1])

liste ={
    [1,2,3,4,5],
    [4,5,6,1],
    [1,2,3]
}
printList(liste)
liste=  increaseList(liste)
print(liste)
reversePrint(liste)
#



