import os

d = {}
def a():
    pass

def b():
    global d
    for filename in os.listdir(path):
        path_to_file = path + '\\' + filename
        d[path_to_file] = os.path.getsize(path_to_file)
        if os.path.isdir(path_to_file):
            b(path_to_file)

def c():
    pass

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