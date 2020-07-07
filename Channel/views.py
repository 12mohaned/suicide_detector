from django.shortcuts import render
import nltk
from nltk.corpus import stopwords, state_union
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer
import csv
stop_words = set(stopwords.words("english"))
def readcsv():
    texts = []
    with open('test.csv', mode = 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            texts.append(row["text"])
    return texts
Text = readcsv()

def Home(request):
    if request.method == "POST":
        Body = request.POST.get("MessageForm")
        Body_Tokenized = word_tokenize(Body)
        modifiedBody_Tokenized = []
        for word in Body_Tokenized:
            if not word in stop_words:
                modifiedBody_Tokenized.append(word)
    return render(request,template_name = "Channel/Home.html")

def word_stemming(Sentence):
    Stemmer = PorterStemmer()
    Stemmed = []
    for word in Sentence:
        if not word in stop_words:
            Stemmed.append(Stemmer.stem(word))
    return Stemmed
