from django.shortcuts import render
import nltk
from nltk.corpus import stopwords, state_union
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
import csv

stop_words = set(stopwords.words("english"))
punctuations="?:!.,;--"
word_lemmatizer = WordNetLemmatizer()

def readcsv():
    texts = []
    with open('test.csv', mode = 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            text = row["text"]
            tokenized = word_tokenize(text)
            for text in tokenized:
                texts.append(text)
    return texts

Text = readcsv()

def Home(request):
    if request.method == "POST":
        Body = request.POST.get("MessageForm")
        Body_Tokenized = word_tokenize(Body)
        #modifiedBody_Tokenized = remove_stopwords(Body_Tokenized)
        for word in Body_Tokenized:
            if not word in punctuations:
                print(lemmatize_verb(word))

    return render(request,template_name = "Channel/Home.html")

#returning the verb to it's origin
def lemmatize_verb(word):
    word = word_lemmatizer.lemmatize(word, pos = 'v')
    return word

#returning the adjective to it's origin
def lemmatize_adjective(word):
    word = word_lemmatizer.lemmatize(word, pos ='a')
    return word
#remove stop words from the speech
def remove_stopwords(Text):
    Modified_Body = []
    for word in Text:
        if not word in stop_words:
            Modified_Body.append(word)
    return Modified_Body
"""
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent\'s
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when"""
