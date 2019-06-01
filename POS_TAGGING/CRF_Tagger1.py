import nltk
from nltk.corpus import brown
from nltk.tag import CRFTagger
 
def crf_tag():
    news_text = brown.tagged_sents(categories='news')
    train_sents=news_text[:3230]
    test_sents=news_text[3230:4600]
    ct = CRFTagger()
    tagger=ct.train(train_sents,'model.crf.tagger')
    test=ct.evaluate(test_sents)
    print test
    sent3="Narendra Modi won Lok Sabha election with massive majority after long years".decode('utf-8')
    sent_w=sent3.lower().split()
    print sent_w
    tag=ct.tag(sent_w)
    print "The Tag Is:",tag
    
    
