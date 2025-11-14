# Задача считать количество слов, потом эти слова ввести и запомнить, а потом вывести эти слова на экран



n = int(input ('Введите количество слов для запоминания: '))

words = []

for i in range(n):
    word = input('введите слово: ')
    words.append(word)

print (words)

# Напишем и слово и его индекс

for i in range (len(words)):
    print (i, words[i])