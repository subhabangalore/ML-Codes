from nltk import NaiveBayesClassifier as nbc
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk.classify import DecisionTreeClassifier
def dt_sentiment():
    training_data = [('I love this sandwich.', 'pos'),
                    ('This is an amazing place!', 'pos'),
                    ('I feel very good about these beers.', 'pos'),
                    ('This is my best work.', 'pos'),
                    ("What an awesome view", 'pos'),
                    ('I do not like this restaurant', 'neg'),
                    ('I am tired of this stuff.', 'neg'),
                    ("I can't deal with this", 'neg'),
                    ('He is my sworn enemy!', 'neg'),
                    ('My boss is horrible.', 'neg')]

    vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in training_data]))
    print vocabulary
    #for i in vocabulary:
        #print "voc:",i

    feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in training_data]
    lfs=len(feature_set)
    #print lfs
    #print feature_set
    
    dt_classifier = DecisionTreeClassifier.train(feature_set,binary=True, entropy_cutoff=0.8, depth_cutoff=5, support_cutoff=30)
    test_sentence = "This is the best work I deal with!"
    featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}
    #print featurized_test_sentence
    #for i1 in featurized_test_sentence:
        #print i1

    print "test_sent:",test_sentence
    print "tag:",dt_classifier.classify(featurized_test_sentence)
