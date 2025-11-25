# Напишите декоратор на функции, которые выводят просто print

import time



# Пишем декоратор, который запишет время начала вызова функции

def my_decorator(func):
    def wrapper():
        time_start = time.time()
        func()
        print (time_start)
    return wrapper


@my_decorator
def say_hello():
    print ('hello')

@my_decorator
def say_bye():
    print ('bye')

print ('вывод с использованием декоратора:')

say_hello()
say_bye()






