# Удалите все дубликаты в листе

# Первый метод

print ('Первый метод')

lst_1 = [3,3,6,6,7,7,7,9,12,15,29,0,-3,-100,-100,777]

my_set = set (lst_1)

print (my_set)

lst_res = list (my_set)

print (lst_res)

# Второй метод, используем цикл

print ('второй метод')

lst_res2 = []

for n in lst_1:
    if n not in lst_res2:
        lst_res2.append(n)
        
print (lst_res2)