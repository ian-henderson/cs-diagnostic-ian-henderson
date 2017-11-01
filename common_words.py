from collections import Counter

def most_common_words(text, k):
    list_of_words = text.split(" ")
    counter = Counter(list_of_words)
    most_common_words = []
    for word in counter.most_common()[:k]:
        most_common_words.append(word[0])
    return most_common_words


print(most_common_words('all awesome all yeah bye all yeah', 2))
