a=open('names.txt','r')
b=open('phonenumbers.txt','r')
k={}
t={}
vowel=['a','e','i','o','u','A','E','I','O','U']
def phonebook(a,b):
    for i in a:
        for j in b:
             t[i.strip()] = j.strip()
             break
    for i in list(t.keys()):
        if i[0] not in vowel:
            t.pop(i)
    for i in t:
        j=t[i][::-1][len(t[i])-2:].rjust(len(t[i]),'*')
        k[i]=j
    return k
def sortedphonebook(k):
    return dict(sorted(k.items()))
def count(k):
    a,e,i,o,u=0,0,0,0,0
    for j in k:
        if j[0].lower()=='a':
            a+=1
        if j[0].lower()=='e':
            e+=1
        if j[0].lower()=='i':
            i+=1
        if j[0].lower()=='o':
            o+=1
        if j[0].lower()=='u':
            u+=1
    t={'A':a,'E':e,'I':i,'O':o,'U':u}
    return t
print(phonebook(a,b))
print(sortedphonebook(phonebook(a,b)))
print(count(phonebook(a,b)))
 
        