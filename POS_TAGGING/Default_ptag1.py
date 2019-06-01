import nltk
from nltk import word_tokenize,pos_tag
def default_ptag():
    sent=raw_input("PLEASE PRINT A SENTENCE:")
    tag_sent=pos_tag(word_tokenize(sent))
    print "The tagged Output of the sentence is:",tag_sent
    
