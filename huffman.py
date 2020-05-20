# -*- coding: utf8 -*-

def fn_cmp(a, b):
    if a[0] > b[0]: return 1
    if a[0] < b[0]: return -1
    return 0

#-- создать дерево хаффмана по тексту -
def make_tree(text):

    se = set(text)
    ls = [(text.count(ch), ch) for ch in se]
    ls.sort()

    #-- построить двоичное дерево по этому списку
    while len(ls) >= 2:
        d = (ls[0] [0] + ls [1] [0], (ls[0] [1], ls[1] [1]))

        if ls[-1] [0]< d[0]:
            ls.append(d)
        else:
            for num in range(2, len (ls)) :
                if ls [num] [0]>= d[0]:
                    break
            ls.insert(num, d)
        ls.pop(0)
        ls.pop(0)
    return ls [0] [1]


#-- рекурсивно создать бинарный код листов элемента
def fn_cod(st, el):
    global ls_haf
    if type (el) == str:
        ls_haf.append((el, st))
        return
    fn_cod(st+"0", el[0])
    fn_cod(st+'1', el[1])
    return

#-- создать словарь хаффмана по тексту -
def make_dict(text):
    global ls_haf
    ls = make_tree(text)
    ls_haf=[]
    fn_cod('',ls)
    dc_haf= dict(ls_haf)
    return dc_haf

#-- сжать по хаффману
def compress(text, dc_haf):
    st_res = ''
    for ch in text:
        st_res = st_res + dc_haf[ch]
    return st_res

#-- decompress
def decompress(text_decompress, key_decompress):
    dc_decod = {key_decompress[key]:key for key in key_decompress}
    st_res = ''
    while len(text_decompress) > 0:
        num = 1
        while text_decompress[:num] not in dc_decod:
            num+=1
        st_res += dc_decod[text_decompress[:num]]
        text_decompress = text_decompress[num:]
    return st_res


#== программа
def huff_compress():
    with open(input('Введите ссылку на ваш файл (test.txt)(только кодировка "Utf-8"): '), "r", encoding = 'utf-8') as file:
        contents = file.read()
        text = str(contents)
        file.close()

    dc_haf = make_dict(text)
    compressed_text = compress(text, dc_haf)
    compressed_text2 = hex(int(compressed_text, 2))

    save = input('Сохраним файл? (Да/Нет): ')
    if save == 'Да':
        name_save = input('Введите, название нового файла или ссылку куда хотите сохранить файл с его названием(test): ')
        f = open(name_save + '.gz','w', encoding = 'utf-8')
        f.writelines(compressed_text2)
        f.close()
        key = input('Введите, название нового ключ или ссылку куда хотите сохранить ключ с его названием(key): ')
        key_f = open(key + '.gz','w', encoding = 'utf-8')
        key_f.write(str(dc_haf))
        key_f.close()
    elif save == 'Нет':
        raise SystemExit
    else:
        print('Вы ввели неверные данные, проверьте регистр')

def huff_decompress():

    file_decompress = open(input('Введите ссылку на ваш файл (test.gz): '), "r", encoding = 'utf-8')
    contents_2 = file_decompress.read()
    text_decompress = bin(int(contents_2, 16)).replace('b', '')
    file_decompress.close()
    text_decompress = str(text_decompress)


    file_key = open(input('Введите ссылку на ключ (key.gz): '), "r", encoding = 'utf-8')
    str_lst = file_key.read()
    key_decompress = eval(str_lst)
    file_key.close()

    decompress_text = decompress(text_decompress, key_decompress)

    save = input('Сохраним файл? (Да/Нет): ')
    if save == 'Да':
        name_save = input('Введите, название нового файла или ссылку куда хотите сохранить файл с его названием(test): ')
        f = open(name_save + '.txt','w', encoding = 'utf-8')
        f.writelines(decompress_text)
        f.close()
    elif save == 'Нет':
        raise SystemExit
    else:
        print('Вы ввели неверные данные, проверьте регистр')
