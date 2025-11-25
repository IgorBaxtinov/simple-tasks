# Напишите декоратор на функции, которые выводят просто print

import time



# Пишем декоратор, который запишет время начала вызова функции
# При этом функции не выводят print они работают через return


def my_decorator(func):
    def wrapper():
        time_start = time.time()
        result = func()
        print (time_start)
        return result
    return wrapper



@my_decorator
def say_hello():
    return 'hello'

@my_decorator
def say_bye():
    return 'bye'

print ('вывод с использованием декоратора:')

print(say_hello())
print(say_bye())
