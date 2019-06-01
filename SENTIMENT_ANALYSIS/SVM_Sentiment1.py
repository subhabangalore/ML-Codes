import nltk
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from nltk.tokenize import word_tokenize
from sklearn.svm import SVC
#TRAINING AND TEST DATA
def SVM_Classifier():
    train = [('I love this sandwich.', 'pos'),
            ('This is an amazing place!', 'pos'),
            ('I feel very good about these beers.', 'pos'),
            ('This is my best work.', 'pos'),
            ("What an awesome view", 'pos'),
            ('I do not like this restaurant', 'neg'),
            ('I am tired of this stuff.', 'neg'),
            ("I can't deal with this", 'neg'),
           ('He is my sworn enemy!', 'neg'),
          ('My boss is horrible.', 'neg')]
    test = [
        ('The beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg')]
  test_sentence = "This is the best band I've ever heard!"
  #FEATURESETS
  all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
  t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
  testf=[({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in test]
  test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
  #CLASSIFICATION
  #SUPPORT VECTOR MACHINE
  classif1 = SklearnClassifier(SVC(), sparse=False).train(t)
  classif1.classify(test_sent_features)
