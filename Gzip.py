# -*- coding: utf8 -*-
import lempelZiv as lem
import huffman as huff
print('1.Сжать текст\n2.Вернуть текст в привычный вид')
choice = input('Введите действие (1 или 2): ')
if choice == '1':
    print('1.Сжать методом LZ77\n2.Сжать методом Хаффмана')
    choice_2 = input('Введите действие (1 или 2): ')
    if choice_2 == '1':
        lem.pack()
    elif choice_2 == '2':
        huff.huff_compress()
elif choice == '2':
    print('1.Декодирование LZ77\n2.Декодирование Хаффмана')
    choice_3 = input('Введите действие (1 или 2): ')
    if choice_3 == '1':
        lem.unpack()
    if choice_3 == '2':
        huff.huff_decompress()

else:
    print('Ошибка, перепроверьте выбор')
