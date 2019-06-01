Welcome to Canopy's interactive data-analysis environment!

Kernel running in the 'User' environment.

Pylab is active using Qt4Agg.

Python 2.7.13 |Enthought, Inc. (x86_64)| (default, Mar  2 2017, 16:05:12) [MSC v.1500 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

stoplist = set('for a of the and to in'.split())

texts = [[word for word in document.lower().split() if word not in stoplist]
       for document in documents]

from collections import defaultdict

frequency = defaultdict(int)

for text in texts:
     for token in text:
         frequency[token] += 1
        

texts = [[token for token in text if frequency[token] > 1]
          for text in texts]

dictionary = corpora.Dictionary(texts)
2019-01-06 13:49:16,407 : INFO : adding document #0 to Dictionary(0 unique tokens: [])
2019-01-06 13:49:16,423 : INFO : built Dictionary(12 unique tokens: [u'minors', u'graph', u'system', u'trees', u'eps']...) from 9 documents (total 29 corpus positions)

dictionary.save('deerwester.dict')
2019-01-06 13:50:05,493 : INFO : saving Dictionary object under deerwester.dict, separately None
2019-01-06 13:50:05,572 : INFO : saved deerwester.dict

new_doc = "Human computer interaction"

new_vec = dictionary.doc2bow(new_doc.lower().split())

corpus = [dictionary.doc2bow(text) for text in texts]

from gensim import corpora, models, similarities
if (os.path.exists("deerwester.dict")):
    dictionary = corpora.Dictionary.load('deerwester.dict')
    corpus = corpora.MmCorpus('deerwester.mm')
    print("Used files generated from first tutorial")
else:
  print("Please run first tutorial to generate data set")
  
2019-01-06 14:00:04,647 : INFO : loading Dictionary object from deerwester.dict
2019-01-06 14:00:04,661 : INFO : loaded deerwester.dict
2019-01-06 14:00:04,661 : INFO : loaded corpus index from deerwester.mm.index
2019-01-06 14:00:04,770 : INFO : initializing cython corpus reader from deerwester.mm
2019-01-06 14:00:04,786 : INFO : accepted corpus with 9 documents, 12 features, 28 non-zero entries
Used files generated from first tutorial

tfidf = models.TfidfModel(corpus)
2019-01-06 14:00:32,446 : INFO : collecting document frequencies
2019-01-06 14:00:32,571 : INFO : PROGRESS: processing document #0
2019-01-06 14:00:32,585 : INFO : calculating IDF weights for 9 documents and 11 features (28 matrix non-zeros)

doc_bow = [(0, 1), (1, 1)]

corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
2019-01-06 14:01:49,026 : INFO : using serial LSI version on this node
2019-01-06 14:01:49,026 : INFO : updating model with new documents
2019-01-06 14:01:49,026 : INFO : preparing a new chunk of documents
2019-01-06 14:01:49,088 : INFO : using 100 extra samples and 2 power iterations
2019-01-06 14:01:49,104 : INFO : 1st phase: constructing (12L, 102L) action matrix
2019-01-06 14:01:49,197 : INFO : orthonormalizing (12L, 102L) action matrix
2019-01-06 14:01:49,588 : INFO : 2nd phase: running dense svd on (12L, 9L) matrix
2019-01-06 14:01:50,025 : INFO : computing the final decomposition
2019-01-06 14:01:50,072 : INFO : keeping 2 factors (discarding 47.565% of energy spectrum)
2019-01-06 14:01:50,086 : INFO : processed documents up to #9
2019-01-06 14:01:50,118 : INFO : topic #0(1.594): 0.703*"trees" + 0.538*"graph" + 0.402*"minors" + 0.187*"survey" + 0.061*"system" + 0.060*"time" + 0.060*"response" + 0.058*"user" + 0.049*"computer" + 0.035*"interface"
2019-01-06 14:01:50,134 : INFO : topic #1(1.476): -0.460*"system" + -0.373*"user" + -0.332*"eps" + -0.328*"interface" + -0.320*"response" + -0.320*"time" + -0.293*"computer" + -0.280*"human" + -0.171*"survey" + 0.161*"trees"

corpus_lsi = lsi[corpus_tfidf]

lsi.print_topics(2)
2019-01-06 14:02:36,247 : INFO : topic #0(1.594): 0.703*"trees" + 0.538*"graph" + 0.402*"minors" + 0.187*"survey" + 0.061*"system" + 0.060*"time" + 0.060*"response" + 0.058*"user" + 0.049*"computer" + 0.035*"interface"
2019-01-06 14:02:36,263 : INFO : topic #1(1.476): -0.460*"system" + -0.373*"user" + -0.332*"eps" + -0.328*"interface" + -0.320*"response" + -0.320*"time" + -0.293*"computer" + -0.280*"human" + -0.171*"survey" + 0.161*"trees"
Out[38]: 
[(0,
  u'0.703*"trees" + 0.538*"graph" + 0.402*"minors" + 0.187*"survey" + 0.061*"system" + 0.060*"time" + 0.060*"response" + 0.058*"user" + 0.049*"computer" + 0.035*"interface"'),
 (1,
  u'-0.460*"system" + -0.373*"user" + -0.332*"eps" + -0.328*"interface" + -0.320*"response" + -0.320*"time" + -0.293*"computer" + -0.280*"human" + -0.171*"survey" + 0.161*"trees"')]

lda=models.LdaModel(corpus, id2word=dictionary, num_topics=10)
2019-01-06 14:04:32,342 : INFO : using symmetric alpha at 0.1
2019-01-06 14:04:32,358 : INFO : using symmetric eta at 0.1
2019-01-06 14:04:32,358 : INFO : using serial LDA version on this node
2019-01-06 14:04:32,515 : INFO : running online (single-pass) LDA training, 10 topics, 1 passes over the supplied corpus of 9 documents, updating model once every 9 documents, evaluating perplexity every 9 documents, iterating 50x with a convergence threshold of 0.001000
2019-01-06 14:04:32,529 : WARNING : too few updates, training might not converge; consider increasing the number of passes or iterations to improve accuracy
2019-01-06 14:04:32,624 : INFO : -8.215 per-word bound, 297.2 perplexity estimate based on a held-out corpus of 9 documents with 29 words
2019-01-06 14:04:32,624 : INFO : PROGRESS: pass 0, at document #9/9
2019-01-06 14:04:32,654 : INFO : topic #6 (0.100): 0.206*"computer" + 0.108*"user" + 0.108*"system" + 0.108*"survey" + 0.108*"time" + 0.108*"response" + 0.108*"human" + 0.108*"interface" + 0.010*"trees" + 0.010*"graph"
2019-01-06 14:04:32,654 : INFO : topic #9 (0.100): 0.083*"trees" + 0.083*"minors" + 0.083*"graph" + 0.083*"system" + 0.083*"user" + 0.083*"eps" + 0.083*"interface" + 0.083*"human" + 0.083*"response" + 0.083*"survey"
2019-01-06 14:04:32,654 : INFO : topic #3 (0.100): 0.206*"system" + 0.206*"trees" + 0.206*"graph" + 0.108*"eps" + 0.108*"human" + 0.108*"minors" + 0.010*"user" + 0.010*"interface" + 0.010*"time" + 0.010*"response"
2019-01-06 14:04:32,654 : INFO : topic #5 (0.100): 0.083*"trees" + 0.083*"graph" + 0.083*"user" + 0.083*"system" + 0.083*"minors" + 0.083*"human" + 0.083*"interface" + 0.083*"response" + 0.083*"eps" + 0.083*"survey"
2019-01-06 14:04:32,671 : INFO : topic #2 (0.100): 0.083*"trees" + 0.083*"system" + 0.083*"graph" + 0.083*"user" + 0.083*"human" + 0.083*"minors" + 0.083*"response" + 0.083*"time" + 0.083*"interface" + 0.083*"survey"
2019-01-06 14:04:32,671 : INFO : topic diff=6.339295, rho=1.000000
