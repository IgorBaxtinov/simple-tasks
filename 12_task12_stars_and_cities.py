# Задача написать звездочек столько сколько букв в каждом городе

# первый способ

cities = ['Yekaterinburg', 'Tokio', 'London', 'Paris', 'Lisabon']

print ('Первый способ')

for i in cities:
    print ('*' * len(i))

# попробуем написать тоже самое через вложенные циклы
print ('Второй способ')


for i in cities:
    count = len (i)
    for i in range (count):
        print ('*', end ='')
    print ()



