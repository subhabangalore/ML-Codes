import nltk
from nltk.corpus import brown
def hmm_tag():
    news_text = brown.tagged_sents(categories='news')
    train_sents=news_text[:3230]
    test_sents=news_text[3230:4600]
    hmm_tagger=nltk.HiddenMarkovModelTagger.train(train_sents)
    test=hmm_tagger.test(test_sents)
    sent3="Narendra Modi won Lok Sabha election with massive majority after long years"
    sent_w=sent3.lower().split()
    print sent_w
    tag=hmm_tagger.tag(sent_w)
    print "The Tag Is:",tag
    
    
