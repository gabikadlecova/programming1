num_list = []
num = 0

while num != -1:
    next_line = input().split()

    for num in next_line:
        num = int(num)
        if num == -1:
            break
        else:
            num_list.append(int(num))

num_list.reverse()

# mezera a konec řádku na konci - špatně
for num in num_list:
    print(f'{num} ')

# jen mezera na konci - špatně
for num in num_list:
    print(f'{num} ', end='')

# správně, ale zbytečně dlouhé
for i in range(len(num_list)):
    print(f"{num_list[i]}", end='')

    if i < len(num_list) - 1:
        print(' ', end='')


# správně, úsporné
str_list = []
for i in num_list:
    str_list.append(str(i))

print(' '.join(str_list))
