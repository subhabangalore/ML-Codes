import nltk
import collections
import nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.tokenize import word_tokenize
from itertools import chain
from operator import concat
#AUTHOR IDENTIFICATION OF BENGALI LANGUAGE
def author_beng_nbc():
    #1st Set
    bankc=open("/python27/Bankim500_1.txt","r").read()
    bankw=bankc.split()
    bankz=reduce(concat,[['bankim',x] for x in bankw[1:]],bankw[0:1])
    #print a3
    it=iter(bankz)
    bankt=zip(it, it)
    #print a4
    #2nd Set
    bibhuc=open("/python27/Bibhuti500_1.txt","r").read()
    bibhuw=bibhuc.split()
    bibhuz=reduce(concat,[['bibhuti',x] for x in bibhuw[1:]],bibhuw[0:1])
    #print b3
    it1=iter(bibhuz)
    bibhut=zip(it1, it1)
    #print b4
    #3rd Set
    rabindrac=open("/python27/Rabindra500_1.txt","r").read()
    rabindraw=rabindrac.split()
    rabindraz=reduce(concat,[['rabindra',x] for x in rabindraw[1:]],rabindraw[0:1])
    #print a3
    it2=iter(rabindraz)
    rabindrat=zip(it2, it2)
    #4th Set
    saratc=open("/python27/Sarat500_1.txt","r").read()
    saratw=saratc.split()
    saratz=reduce(concat,[['sarat',x] for x in saratw[1:]],saratw[0:1])
    #print a3
    it3=iter(saratz)
    saratt=zip(it3, it3)
    add1=bankt+bibhut+rabindrat+saratt
    #print c1
    training_data=add1
    vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in training_data]))
    feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in training_data]
    #print "###",feature_set
    from nltk.classify import NaiveBayesClassifier as nbc
    train_set, test_set = feature_set[:300], feature_set[300:]
    print len(train_set)
    print len(test_set)
    classifier = nbc.train(train_set)
    test_sentence = "আলীপুরের উকিল বিশেষ কিছু হয় বলিয়া মনে হয় না বালিগঞ্জের ওদিকে কোথায় একটা টিউশনি আছে"
    featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}
    print "test_sent:",test_sentence
    print "tag:",classifier.classify(featurized_test_sentence)
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)
    for i, (feats, label) in enumerate(test_set):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)
       
    print 'bankim precision:', nltk.precision(refsets['bankim'], testsets['bankim'])
    print 'bankim recall:', nltk.recall(refsets['bankim'], testsets['bankim'])
    print 'bankim F-measure:',nltk.f_measure(refsets['bankim'], testsets['bankim'])
    print 'bibhuti precision:', nltk.precision(refsets['bibhuti'], testsets['bibhuti'])
    print 'bibhuti recall:', nltk.recall(refsets['bibhuti'], testsets['bibhuti'])
    print 'bibhuti F-measure:', nltk.f_measure(refsets['bibhuti'], testsets['bibhuti'])
    print 'bankim precision:', nltk.precision(refsets['rabindra'], testsets['rabindra'])
    print 'bankim recall:', nltk.recall(refsets['rabindra'], testsets['rabindra'])
    print 'bankim F-measure:',nltk.f_measure(refsets['rabindra'], testsets['rabindra'])
    print 'bibhuti precision:', nltk.precision(refsets['sarat'], testsets['sarat'])
    print 'bibhuti recall:', nltk.recall(refsets['sarat'], testsets['sarat'])
    print 'bibhuti F-measure:', nltk.f_measure(refsets['sarat'], testsets['sarat'])
    
    
    
    
    
    
