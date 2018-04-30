import string

def get_book():
    FILE = open("pridejane.txt", "rU")
    book = FILE.read()
    FILE.close()
    book = book.translate(None, string.punctuation).lower()
    book_words = book.split()
    return book_words

def word_freq(word):
    book = get_book()
    return len([x for x in book if x == word])
    # return reduce(lambda a, b: a + b, [1 for x in get_book() if x == word]) if word in get_book() else 0

def group_freq(word_list):
    return reduce(lambda a, b : a + b, [word_freq(wrd) for wrd in word_list])

def most_freq():
    book = get_book()
    d = {wrd : 0 for wrd in book}
    freqs = [[wrd, word_freq(wrd)] for wrd in d]
    # print freqs
    return reduce(lambda a, b : a if a[1] > b[1] else b, freqs)
    # print d
    # d = {wrd : lambda wrd : d[wrd] + 1 for wrd in book}
    # print d
    # top_freq = max(d.values())
    # return [wrd for wrd, freq in d.items() if freq == top_freq]



if __name__ == "__main__":
    # print get_book()
    print "frequency of word 'limited': " + str(word_freq("limited"))
    word_list = ['limited', 'quite']
    print "frequency of words 'limited' and 'quite': " + str(group_freq(word_list))
    print most_freq()
