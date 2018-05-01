import string

def get_book():
    FILE = open("pridejane.txt", "rU")
    book = FILE.read()
    FILE.close()
    book = book.translate(None, string.punctuation).lower()
    book_words = book.split()
    return book_words

def word_freq(word, book):
    return len([x for x in book if x == word])
    # return reduce(lambda a, b: a + b, [1 for x in get_book() if x == word]) if word in get_book() else 0

def group_freq(word_list):
    book = get_book()
    return reduce(lambda a, b : a + b, [word_freq(wrd, book) for wrd in word_list])

def most_freq():
    book = get_book()
    # book_trim = list(set(book)) # remove duplicates
    d = {wrd: 0 for wrd in book}
    for wrd in book:
        d[wrd] += 1
    freqs = [[wrd, d[wrd]] for wrd in d]
    # print freqs
    return reduce(lambda a, b : a if a[1] > b[1] else b, freqs)



if __name__ == "__main__":
    # print get_book()
    print "frequency of word 'limited': " + str(word_freq("limited", get_book()))
    word_list = ['limited', 'quite']
    print "frequency of words 'limited' and 'quite': " + str(group_freq(word_list))
    print "the most frequent word is..."
    print most_freq()
