import nltk
from nltk.corpus.reader import TaggedCorpusReader
import dill
from collections import Counter
import random
import itertools
#SAMPLE HINDI NER TRAINED ON DAINIK JAGRAN
def NER_HINDI():
    reader = TaggedCorpusReader('/python27/POS_9/', r'.*\.pos')
    f1=reader.fileids()
    print "The Files of Corpus are:",f1
    sents=reader.tagged_sents()
    sentn=reader.sents()
    #words=sentn.split()
    ls=len(sents)
    #lw=len(words)
    print "Length of Corpus Is:",ls
    #print "The Words are:",lw
    size1 = int(ls * 0.3)
    test_sents=sents[:size1]
    train_sents=sents[size1:]
    hmm_tagger=nltk.HiddenMarkovModelTagger.train(train_sents)
    test=hmm_tagger.test(test_sents)
    #THE GIVEN INPUT
    given_sent="नीतीश कुमार द्वारा भाजपा के साथ हाथ मिलाने से वहां का पूरा राजनीतिक परिदृश्‍य ही बदल गया है मगर शरद यादव इससे खुश नहीं हैं".decode('utf-8')
    gsw=given_sent.split()
    tag_gs=hmm_tagger.tag(gsw)
    print "GIVEN SENT TAG:",tag_gs
    ftag_gs=" ".join(list(itertools.chain(*tag_gs)))
    print "And its flattened Version is:",ftag_gs
    #INPUT FROM FILE
    with open('HINDIHMMNER1.dill', 'wb') as f:
        dill.dump(hmm_tagger, f)
    with open('HINDIHMMNER1.dill', 'rb') as f:
        hmm_tagger1 = dill.load(f)
    
    test_tags = [tag for sent in reader.sents()
    for (word, tag) in hmm_tagger1.tag(sent)]
    gold_tags = [tag for (word, tag) in reader.tagged_words()]
    ltesttag=len(test_tags)
    lgtags=len(gold_tags)
    print "Test Tag Len:",ltesttag
    print "Gold Tag Len:",lgtags
    cm=nltk.ConfusionMatrix(gold_tags, test_tags)
    print(cm.pretty_format(sort_by_count=True, show_percents=False, truncate=5))
    labels = set('NA GPE PERS DATE  ORG'.split())#THE TAG SETS AS GENERATED IN CONFUSION MATRIX
    true_positives = Counter()
    false_negatives = Counter()
    false_positives = Counter()
    for i in labels:
        for j in labels:
            if i == j:
                true_positives[i] += cm[i,j]
            else:
                false_negatives[i] += cm[i,j]
                false_positives[j] += cm[i,j]
    print "TP:", sum(true_positives.values()), true_positives
    print "FN:", sum(false_negatives.values()), false_negatives
    print "FP:", sum(false_positives.values()), false_positives
    print 

    for i in sorted(labels):
        if true_positives[i] == 0:
            fscore = 0
        else:
            precision = true_positives[i] / float(true_positives[i]+false_positives[i])
            recall = true_positives[i] / float(true_positives[i]+false_negatives[i])
            fscore = 2 * (precision * recall) / float(precision + recall)
            fscore1=fscore*100
            print "TAG:",i,"FMEASURE:", fscore1

