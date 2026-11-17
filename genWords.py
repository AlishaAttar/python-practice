def word_generator(sentence):
    words = sentence.split()

    for word in words:
        yield word


sentence = "Python is easy to learn"

for word in word_generator(sentence):
    print(word)