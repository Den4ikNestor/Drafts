import nltk
import numpy
from nltk.book import *


def meet():
    print("\n")
    # Нахождение соответствий
    text1.concordance("ChapTeR")
    print("\n")
    # Поиск всех слов с близким значением в контексте
    # Что и слово "monstrous" (чудовищный)
    text2.similar("monstrous")
    # Выводит общий контекст, где употреблены
    # перечисленные слова
    text2.common_contexts(["very", "a"])
    # Лексическая дисеперсия. Распределение слов тексте
    text7.dispersion_plot(["business", "friend", "democracy",
                           "man", "success", "money"])


def info(text):
    print("Количество токенов (последовательностей) в тексте = " + str(len(text)))
    print(sorted(set(text)))
    print("Количество уникальных токенов = " + str(len(set(text))))
    # количество раз, которое встречается слово в тексте
    print("Количество употреблений слова In = " + str(text.count("In")))
    freq_dist = FreqDist(text)
    print(str(freq_dist))
    vocabulary = sorted(freq_dist.keys(), reverse=True)
    print("Самое распространенное слово в тексте:")
    print(str(vocabulary[0]))
    print("Слова в тексте, встречающиеся больше 50 раз с длиной больше 7 символов")
    print(sorted([word for word in set(text) if len(word) > 7 and freq_dist[word] > 50], reverse=True))
    print("Пары слов, встречающиеся в тексте чаще других")
    print(str(text.collocations()))
    print("Частота слов в зависимости от их длины")
    fdist = FreqDist([len(word) for word in text])
    print(str(sorted(fdist.items(), reverse=True)))
    print("Сделать все слова из маленьких букв и подсчитать их уникальность")
    print(str(len(set([word.lower() for word in text]))))


def lists(list):
    # Добавление слова в конец списка
    list.append('word')
    print("Список: " + str(list))
    print("Второе слова в списке - это " + str(list[1]))


if __name__ == "__main__":
    # meet()
    info(text3)
    # lists(sent3)

