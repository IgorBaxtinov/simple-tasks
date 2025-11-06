# Задача для while
# Перебрать все символы в строке

my_str = 'My name is Igor'

i = 0

while i < len (my_str):
    print (my_str[i])
    i +=1

print ('Количество символов в строке:')
print (len(my_str))

# Теперь используепм цикл for

for i in my_str:
    print (i)

print ('Количество символов в строке:')
print (len(my_str))

# Теперь выведем идекс и символ в строке

for i in range (len(my_str)):
    print (i, my_str[i])






