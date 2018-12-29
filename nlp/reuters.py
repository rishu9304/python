import nltk
from nltk.corpus import reuters

files = reuters.fileids()
print(files)

words = reuters.words(files[0])
print(words[:20])

cate = reuters.categories()
print("categories",cate)