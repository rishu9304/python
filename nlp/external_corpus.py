from nltk.corpus import CategorizedPlaintextCorpusReader as cr 

reader = cr(r'/Volumes/Data/NLPCookBook/Reviews/txt_sentoken', r'.*\.txt', cat_pattern=r'(\w+)/*') 
print(reader.categories()) 
print(reader.fileids())

posFiles = reader.fileids(categories='pos') 
negFiles = reader.fileids(categories='neg')

from random import randint 
fileP = posFiles[randint(0,len(posFiles)-1)] 
fileN = negFiles[randint(0, len(posFiles) - 1)] 
print(fileP) 
print(fileN) 