import os
USE = os.environ.get( "USERNAME" )
print('''
    ─────────────────────────────────────────────────────────────
    ─██████████████─██████████████─████████████───██████████████─
    ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██─
    ─██░░██████████─██░░██████░░██─██░░████░░░░██─██░░██████░░██─
    ─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
    ─██░░██████████─██░░██████░░██─██░░██──██░░██─██░░██████░░██─
    ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─
    ─██████████░░██─██░░██████░░██─██░░██──██░░██─██░░██████░░██─
    ─────────██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
    ─██████████░░██─██░░██──██░░██─██░░████░░░░██─██░░██──██░░██─
    ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░████─██░░██──██░░██─
    ─██████████████─██████──██████─████████████───██████──██████─
    ─────────────────────────────────────────────────────────────
''')
if os.path.exists("C:/Users/{}/Documents/woss/notes.rw".format(USE)):
    fda = open("C:/Users/{}/Documents/woss/notes.rw".format(USE), 'r', -1, 'utf-16be')
    ur = fda.read()
    ur = ur.replace('\\n','\n')
    if ur != '':
        print(ur)
    fda.close()

if os.path.exists("C:/Users/{}/Documents/woss".format(USE)):
    pass
else:
    os.mkdir("C:/Users/{}/Documents/woss".format(USE))

while True:
    try:
        www = input('[>>')
        if www == 'h':
            print('''
# re === создать репозиторий
# sh === показать все созданные репозитории
# rh === прочитать репозиторий
# cre === очистить репозиторий и записать текст
# yy === очистить репозиторий
# rr === записать текст
# ir === удалить репозиторий
# rt === переименовать репозиторий
''')
        ww = www.split(' ')
        if ww[0] == 're':
            if os.path.exists("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ww[1])):
                print('репозиторий уже существует')
            else:
                fdafsf = open("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ww[1]), 'w', -1, 'utf-16be')
                fdafsf.write("")
                fdafsf.close()
                print('репозиторий '+ww[1]+' создан')
        
        elif ww[0] == 'sh':
            g = os.listdir("C:/Users/{}/Documents/woss".format(USE))
            g1 = 0
            print('')
            while g1 < len(g):
                oo = g[g1]
                oo = oo.replace('.rw','')
                print(g1+1,' >',oo)
                g1 = g1+1
            print('')

        elif ww[0] == 'rh':
            if os.path.exists("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ww[1])):
                fda = open("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ww[1]), 'r', -1, 'utf-16be')
                ur = fda.read()
                ur = ur.replace('\\n','\n')
                if ur != '':
                    print(ur)
                else:
                    print('репозиторий пустой')
                fda.close()
            else:
                print('какого репозитория нету')

        elif ww[0] == 'cre':
            ddd = ww[1].split(',')
            if os.path.exists("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0])):
                fdafsf = open("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0]), 'w', -1, 'utf-16be')
                fdafsf.write(ddd[1])
                fdafsf.close()
                print('текст сохранен')
            else:
                print('какого репозитория нету')

        elif ww[0] == 'yy':
            ddd = ww[1].split(',')
            if os.path.exists("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0])):
                fdafsf = open("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0]), 'w', -1, 'utf-16be')
                fdafsf.write('')
                fdafsf.close()
                print('репозиторий очищен')
            else:
                print('какого репозитория нету')

        elif ww[0] == 'rr':
            ddd = ww[1].split(',')
            if os.path.exists("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0])):
                fdafsf = open("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0]), 'a', -1, 'utf-16be')
                fdafsf.write(ddd[1])
                fdafsf.close()
                print('текст сохранен')
            else:
                print('какого репозитория нету')

        elif ww[0] == 'rt':
            ddd = ww[1].split(',')
            if os.path.exists("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0])):
                os.rename("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[0]),
                "C:/Users/"+USE+"/Documents/woss/{}.rw".format(ddd[1]))
                print('файл '+ddd[0]+' переименован в '+ddd[1])
            else:
                print('какого репозитория нету')

        elif ww[0] == 'ir':
            if os.path.exists("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ww[1])):
                os.remove("C:/Users/"+USE+"/Documents/woss/{}.rw".format(ww[1]))
                print('репозиторий '+ww[1]+' удален')
            else:
                print('какого репозитория нету')
            
    except:
        print('!!!')