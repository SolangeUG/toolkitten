from nltk.book import *


def get_lexical_diversity(text):
    """
    Return a measure of lexical diversity in a text
    :param text: the input text
    :return: lexical diversity score
    """
    unique_words = set(text)
    return len(text) / len(unique_words)


def get_tokens(word_list):
    """
    Return a sorted list of unique tokens from a list of words
    :param word_list: input list of words
    :return: sorted list of unique tokens
    """
    tokens = set(word_list)
    return sorted(tokens)


def get_most_common_words(text, n):
    """
    Return a list of n most common words in a given text
    :param text: the input text
    :param n: the number of words wanted
    :return: n most common words
    """
    distri = FreqDist(text)
    return distri.most_common(n)


def main():
    print()
    score = get_lexical_diversity(text1)
    print("Lexical diversity of «", text1.name, "» is of", score)

    sentence = "After all is said and done more is said than done"
    word_list = sentence.split(" ")
    tokens = get_tokens(word_list)
    print("A few tokens from our sentence:", tokens[-2:])

    text, n = text3, 100
    most_common = get_most_common_words(text, n)
    print("The", n, "most common words of «", text.name, "» are", most_common)


if __name__ == '__main__':
    main()
