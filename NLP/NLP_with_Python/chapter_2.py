import nltk
import numpy
# from nltk.corpus import webtext
# from nltk.corpus import nps_chat
from nltk.corpus import brown # categorical sources
# from nltk.corpus import reuters # classified documents into
# 90 topics (grouped into train and test)

from nltk.corpus import inaugural
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn

from nltk.corpus import gutenberg
texts = gutenberg.fileids()
emma = nltk.Text(gutenberg.words('austen-emma.txt'))


def first():
    """
    learning nltk.corpus abilities
    :return:
    """
    print(str(texts))
    print(str(len(emma)))

    # function sents() divide text to sentences
    sentences = gutenberg.sents('austen-emma.txt')
    print(str(sentences[370]))

    # maximal sentence
    # max_sentence = max([len(sent) for sent in sentences])
    # print(str([sent for sent in sentences if len(sent) == max_sentence]))

    # function raw() return all symbols including spaces
    symbols = gutenberg.raw('austen-emma.txt')
    print(str(symbols[0:15]))

    # plot word's using trend
    trend = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for word in inaugural.words(fileid)
        for target in ['america', 'money', 'business', 'woman', 'man']
        if word.lower().startswith(target)
    )
    trend.plot()

    # stop_words for 21 languages
    read = stopwords.readme()
    print(read)
    files = stopwords.fileids()
    print(len(files))
    russian_stop_words = stopwords.words('russian')
    stopwords.open('russian')
    print(russian_stop_words[:10])


def generate_model(cfdist, word, num=15):
    # Make sentence of num words based on
    # most likely to follow a given word
    for i in range(num):
        print(word)
        word = cfdist['news'].max()


def second():
    """

    :return:
    """
    # Add 'news' and 'romance' to each word
    # making pairs.
    genre_word = [(genre, word)
                  for genre in ['news', 'romance']
                  for word in brown.words(categories=genre)]
    len(genre_word)

    cfd = nltk.ConditionalFreqDist(genre_word)
    print(cfd.conditions())
    print(list(cfd['news'])[:5])
    days = ['Monday', 'Thursday', 'Wednesday', 'Tuesday',
            'Friday', 'Saturday', 'Sunday']
    cfd.tabulate(conditions=['news', 'romance'],
                 samples=days, cumulative=True)
    pairs = nltk.bigrams(brown.words(categories='news'))
    cfd_2 = nltk.ConditionalFreqDist(pairs)
    # generate_model(cfd_2, 'his')
    # print(cfd_2['Monday'].max())
    print(cfd['news'].max())

    # print synonyms
    for synset in wn.synsets('car'):
        print(synset.lemma_names())
        print(synset.definition())
        print(synset.examples())


def call():
    # first()
    second()
