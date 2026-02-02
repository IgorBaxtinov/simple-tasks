# Имеем строку, нужно вывести в терминал на каком месте (индексе) находится символ

stroka = 'aaufrghwhfueigfugaihhsofihudofguaoisfugauiguaguuiadgiysfdyuasyapfapafyupdfauysdfauydfausdasaa'

size = len (stroka)
count = 0

for i in range (size):
    if (stroka[i] == 'a'):
        count +=1
        print (i, end =' ')

print (count)

