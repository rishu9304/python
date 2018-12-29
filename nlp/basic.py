import nltk

from nltk.corpus import wordnet 

word = wordnet.synsets("spectacular")

print(word)

print(word[0].defination())

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

print(stemmer.stem("decreases"))

from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()
print(lemma.lemmatize("decreases"))