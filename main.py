import os

d = {}
def a():
    path_to_directory = str(input())
    b(path_to_directory)
    c(d)

def b():
    global d
    for filename in os.listdir(path):
        path_to_file = path + '\\' + filename
        d[path_to_file] = os.path.getsize(path_to_file)
        if os.path.isdir(path_to_file):
            b(path_to_file)

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
    not_doubles = []
    for k, v in dict.items(doubles):
        if v == 1:
            not_doubles.append(k)
    for item in not_doubles:
        del doubles[item]
    if doubles == {}:
        print('Дубликатов не найдено')
    else:
        print(doubles)

#точка ввода
print('/T\\')
print('|.|  Привет я точка входа, напиши "start" чтобы начать')
while True:
    vhod = input()
    if vhod =="start":
        break
a()