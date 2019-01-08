import nltk
import re
import pprint
from urllib import request
from bs4 import BeautifulSoup
# The topic is get access to Webs


def first():
    url = 'http://www.gutenberg.org/files/48879/48879-0.txt'
    text = request.urlopen(url).read()
    print(type(text))
    print(len(text))
    print(text[:75])

    # tokenization
    tokens = nltk.word_tokenize(str(text))
    print(type(tokens))
    print(len(tokens))
    print(tokens[:10])

    # getting back to the Text
    # file = nltk.Text(text)


def second():
    url_2 = 'http://baguzin.ru/wp/prostaya-linejnaya-regressiya/'
    html = request.urlopen(url_2).read()
    print(type(html))
    print(html[:50])
    soup = BeautifulSoup(html, 'html.parser')
    tokens = soup.get_text()
    tokens_2 = nltk.word_tokenize(tokens)
    print(len(tokens_2))
    # print(tokens_2[1500:2000])
    text = nltk.Text(tokens_2)
    print(text.concordance('регрессия'))


    # all_links


def soup():
    url = 'http://baguzin.ru/wp/prostaya-linejnaya-regressiya/'
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Html-page structure
    # print(soup.prettify())

    # get all links
    for link in soup.find_all('a'):
        print(link.get('href'))

    # get all text
    print(soup.get_text())


def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def third():
    wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
    print(wordlist)

    temp = [w for w in wordlist if re.search('ed$', w)]
    print(temp)

    raw = """Hello, my name is Denis. I'm typing right now
    this text. It seems boring. I want to sleep and drink tea.
    And now I'll type some words: bitly, comes, glorious
    punishment, government"""
    tokens = nltk.word_tokenize(raw)
    print(tokens)
    print([stem(word) for word in tokens])

    # simple tokenization
    # re.split(r'[ \t\n]+', raw)

    # Through out all symbols besides characters of words
    # re.split(r'\W+', raw)

    # The same as the previous one but spaces were exluded
    # re.findall(r'\w+', raw)

    # nltk.regexp_tokenizer() is similar to re.findall()

    # from list to string
    list_of_words = ['Now', 'I', '\'', 'm', 'typing']
    print(' '.join(list_of_words))
    print(''.join(list_of_words))
    print('|'.join(list_of_words))


def call():
    # first()
    # second()
    # soup()
    third()
