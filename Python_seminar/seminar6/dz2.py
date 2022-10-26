# Орел и решка

text = 'VIIIIIINNNNIIIIIIIIIIPUUUH'
char_to_find = 'I'


max_count = 0
tmp = 0

for c in text:
    if char_to_find == c:
        tmp += 1
    else:
        if tmp > max_count:
            max_count = tmp
        tmp = 0
if tmp > max_count:
    max_count = tmp


print(f'Последовательность: {text}')
print(f'Максимальная последовательность решки: {max_count}')