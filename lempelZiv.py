# -*- coding: utf8 -*-
def pack():
    with open(input('Введите ссылку на ваш файл (файл кодировки "Utf-8")(test.txt): '), "r", encoding = 'utf-8') as file:
        contents = file.read()
        src = str(contents)
        file.close()

    #print('src: ' + src)

    pack = []
    i = 0
    while i < len(src):
        ln = 9
        found = False
        while not found and ln > 3:
            j = i - ln
            while j >= 0 and (i - j) < 100:
                if src[i:i+ln] == src[j:j+ln]:
                    pack += '#%1d%2d' %(ln, (i - j))
                    i += ln
                    found = True
                    break
                j -= 1
            ln -= 1

        if not found:
            pack += src[i]
            i += 1
    #Если хотим проверить эффективность сжатия
    #print(f'Сжатие символов (Сжатый текст - Исходный текст) {len(pack)} - {len(src)}')
    #print('pack: ' + pack)
#cp1251
    save = input('Сохраним файл? (Да/Нет): ')
    if save == 'Да':
        name_save = input('Введите, название нового файла или ссылку куда хотите сохранить файл с его названием(test): ')
        f = open(name_save + '.gz','w', encoding = 'cp1251')
        f.writelines(pack)
        f.close()
    elif save == 'Нет':
        raise SystemExit
    else:
        print('Вы ввели неверные данные, проверьте регистр')

def unpack():
    with open(input('Введите ссылку на ваш файл(test.gz): '), "r", encoding = 'cp1251') as file:
        contents = file.read()
        pack = str(contents)
        src = str(contents)
        file.close()
    unpack = ''
    i = 0
    while i < len(pack):
        if pack[i] != '#':
            unpack += pack[i]
            i += 1
            continue
        ln = int(pack[i+1: i+2])
        dist = int(pack[i+2: i+4])
        unpack += unpack[-dist: -dist+ln]
        i += 4

    #print('unpack: ' + unpack)

    save = input('Сохраним файл? (Да/Нет): ')
    if save == 'Да':
        name_save = input('Введите, название нового файла или ссылку куда хотите сохранить файл с его названием(test): ')
        f = open(name_save + '.txt','w', encoding = 'utf-8')
        f.writelines(unpack)
        f.close()
    elif save == 'Нет':
        raise SystemExit
    else:
        print('Вы ввели неверные данные, проверьте регистр')
