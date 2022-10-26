# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from RLE import RLE

text = 'YYYYHHHggggPPIii'
print('Исходная строка: ' + text)

enc_str = RLE.encrypt(text)
print('Зашифрованная строка: ' + enc_str)

print('Расшифрованная строка: ' + RLE.decrypt(enc_str))