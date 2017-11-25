from textblob.classifiers import NaiveBayesClassifier

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]
cl = NaiveBayesClassifier(train)
cl.classify("Their burgers are amazing")  # "pos"
cl.classify("I don't like their pizza.")  # "neg"

from textblob import TextBlob
blob = TextBlob("The beer was amazing. "
                "But the hangover was horrible. My boss was not happy.",
                classifier=cl)
blob.classify()  # "neg"
for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
# "pos", "neg", "neg"
cl.accuracy(test)
# 0.83
cl.show_informative_features(5)
# Most Informative Features
#             contains(my) = True              neg : pos    =      1.7 : 1.0
#             contains(an) = False             neg : pos    =      1.6 : 1.0
#             contains(my) = False             pos : neg    =      1.3 : 1.0
#          contains(place) = False             neg : pos    =      1.2 : 1.0
#             contains(of) = False             pos : neg    =      1.2 : 1.0

