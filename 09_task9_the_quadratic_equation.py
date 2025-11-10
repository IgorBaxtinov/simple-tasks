# Посмотерть как работает двойной цикл, решить уравние
# Ответ и скать в промежутке от -100 до 100

# 2*x + 5*y = 32

found = False

for x in range(-100, 100):
    for y in range(-100,100):
        if 2*x + 5*y == 32:
            print(x,y)
            found = True
if not found:
    print ('Решение не найдено')