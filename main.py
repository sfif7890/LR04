import os

d = {}
def a():
    path_to_directory = str(input())
    b(path_to_directory)
    c(d)

def b():
    pass

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