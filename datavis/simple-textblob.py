from textblob.classifiers import NaiveBayesClassifier
from textblob.blob import TextBlob

train = [('I like this new tv show.', 'pos'), ('I am very happy', 'pos'), ('Today is a good day', 'pos'),
("I don't like talking", 'neg'), ('Computer science makes me crazy', 'neg'), ('I am lazy', 'neg')]
test = [('I do not enjoy my job', 'neg'), ('The book is interesting', 'pos')]

cl = NaiveBayesClassifier(train)
cl.classify('The new movie was amazing.')
cl.update(test)
blob = TextBlob('The food was good. But the service was horrible. My father was not pleased.', classfier=cl)
print(blob)
print(blob.classify())
for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())