import os

d = {}
def a():
    pass

def b():
    pass

def c():
    m = []
    m1 = []
    for k in d.keys():
        m.append(os.path.basename(k))
    for v in d.values():
        m1.append(v)

    doubles = {}

    for i in range(len(m)):
        count = 0
        for j in range(len(m)):
            if m[i]==m[j]:
                if m1[i]==m1[j]:
                    count+=1
                doubles[m[i]]=count
    return d(doubles)

def d():
    pass

#точка ввода
print('/T\\')
print('|.|  Привет я точка входа, напиши "start" чтобы начать')
while True:
    vhod = input()
    if vhod =="start":
        break
a()