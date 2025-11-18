# Запросить у пользователетя число и проверить что б это было не 0 и не буквы методом ловли ошибок


try:
    n = int (input('Введите число: '))
    print (10 /n)
except ZeroDivisionError:
    print ('На ноль делать нельзя')

except ValueError:
    print ('Нужно ввести число цифрами')

finally:
    print ('the end')

