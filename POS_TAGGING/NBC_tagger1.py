import nltk
from nltk.corpus import brown
from nltk.tag.sequential import ClassifierBasedPOSTagger
def nbc_tagger():
    news_text = brown.tagged_sents(categories='news')
    train_sents=news_text[:3230]
    test_sents=news_text[3230:4600]
    nbc_tagger=ClassifierBasedPOSTagger(train=train_sents)
    test=nbc_tagger.evaluate(test_sents)
    print "The Test Results Is:",test
    sent3="Narendra Modi won Lok Sabha election with massive majority after long years"
    sent_w=sent3.lower().split()
    print sent_w
    tag=nbc_tagger.tag(sent_w)
    print "The Tag Is:",tag
    
    
