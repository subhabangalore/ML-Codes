import nltk
from nltk.corpus.reader import TaggedCorpusReader
import dill
from collections import Counter
import random
import itertools
from nltk.tag.sequential import ClassifierBasedPOSTagger
#SAMPLE HINDI NER TRAINED ON DAINIK JAGRAN
def NER_HINDINBC():
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
    nbc_tagger=ClassifierBasedPOSTagger(train=train_sents)
    test=nbc_tagger.evaluate(test_sents)
    print "The Test Result is:",test
    #THE GIVEN INPUT
    given_sent="नीतीश कुमार द्वारा भाजपा के साथ हाथ मिलाने से वहां का पूरा राजनीतिक परिदृश्‍य ही बदल गया है मगर शरद यादव इससे खुश नहीं हैं".decode('utf-8')
    gsw=given_sent.split()
    tag_gs=nbc_tagger.tag(gsw)
    print "GIVEN SENT TAG:",tag_gs
    ftag_gs=" ".join(list(itertools.chain(*tag_gs)))
    print "And its flattened Version is:",ftag_gs
    
    
