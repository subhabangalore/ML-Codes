Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: C:\Python27\NERHINDI1.py =====================
>>> NER_HINDI()
The Files of Corpus are: ['pos1_10.pos', 'pos1_11.pos', 'pos1_12.pos', 'pos1_13.pos', 'pos1_7_1.pos', 'pos1_7_2.pos', 'pos1_7_3.pos', 'pos1_7_3_1.pos', 'pos1_7_3_2.pos', 'pos1_7_4.pos', 'pos1_7_4_1.pos', 'pos1_7_4_2.pos', 'pos1_7_4_3.pos', 'pos1_7_4_4.pos', 'pos1_7_5.pos', 'pos1_7_5_1.pos', 'pos1_7_5_2.pos', 'pos1_7_5_3.pos', 'pos1_7_6.pos', 'pos1_7_6_1.pos', 'pos1_7_6_2.pos', 'pos1_7_7.pos', 'pos1_7_7_1.pos', 'pos1_8.pos', 'pos9_1.pos', 'pos_9.pos']
Length of Corpus Is: 3868
accuracy over 14210 tokens: 90.63
GIVEN SENT TAG: [(u'\u0928\u0940\u0924\u0940\u0936', u'PERS'), (u'\u0915\u0941\u092e\u093e\u0930', u'PERS'), (u'\u0926\u094d\u0935\u093e\u0930\u093e', u'NA'), (u'\u092d\u093e\u091c\u092a\u093e', u'ORG'), (u'\u0915\u0947', u'NA'), (u'\u0938\u093e\u0925', u'NA'), (u'\u0939\u093e\u0925', u'NA'), (u'\u092e\u093f\u0932\u093e\u0928\u0947', u'NA'), (u'\u0938\u0947', u'NA'), (u'\u0935\u0939\u093e\u0902', u'NA'), (u'\u0915\u093e', u'NA'), (u'\u092a\u0942\u0930\u093e', u'NA'), (u'\u0930\u093e\u091c\u0928\u0940\u0924\u093f\u0915', u'NA'), (u'\u092a\u0930\u093f\u0926\u0943\u0936\u094d\u200d\u092f', u'NA'), (u'\u0939\u0940', u'NA'), (u'\u092c\u0926\u0932', u'NA'), (u'\u0917\u092f\u093e', u'NA'), (u'\u0939\u0948', u'NA'), (u'\u092e\u0917\u0930', u'NA'), (u'\u0936\u0930\u0926', u'PERS'), (u'\u092f\u093e\u0926\u0935', u'PERS'), (u'\u0907\u0938\u0938\u0947', u'NA'), (u'\u0916\u0941\u0936', u'NA'), (u'\u0928\u0939\u0940\u0902', u'NA'), (u'\u0939\u0948\u0902', u'NA')]
And its flattened Version is: नीतीश PERS कुमार PERS द्वारा NA भाजपा ORG के NA साथ NA हाथ NA मिलाने NA से NA वहां NA का NA पूरा NA राजनीतिक NA परिदृश्‍य NA ही NA बदल NA गया NA है NA मगर NA शरद PERS यादव PERS इससे NA खुश NA नहीं NA हैं NA
Test Tag Len: 47367
Gold Tag Len: 47367
     |                 P           D |
     |           O     E     G     A |
     |     N     R     R     P     T |
     |     A     G     S     E     E |
-----+-------------------------------+
  NA |<39163>  368   269    94   425 |
 ORG |   405 <2116>   46    92    44 |
PERS |    87    16 <1432>   16    86 |
 GPE |   121    86    39 <1247>   27 |
DATE |    57     3     .     3 <1105>|
-----+-------------------------------+
(row = reference; col = test)

TP: 45063 Counter({'NA': 39163, 'ORG': 2116, 'PERS': 1432, 'GPE': 1247, 'DATE': 1105})
FN: 2284 Counter({'NA': 1156, 'ORG': 587, 'GPE': 273, 'PERS': 205, 'DATE': 63})
FP: 2284 Counter({'NA': 670, 'DATE': 582, 'ORG': 473, 'PERS': 354, 'GPE': 205})

TAG: DATE FMEASURE: 77.408056042
TAG: GPE FMEASURE: 83.9165545087
TAG: NA FMEASURE: 97.7218285258
TAG: ORG FMEASURE: 79.9697656841
TAG: PERS FMEASURE: 83.6692959392
>>> 
