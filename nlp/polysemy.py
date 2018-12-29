from nltk.corpus import wordnet as wn 
types = 'n'
synsets = wn.all_synsets(type) 

lemmas = []
for synset in synsets:
	for lemma in synset.lemmas():
		lemmas.append(lemma.name())

lemmas = set(lemmas)

count = 0
for lemma in lemmas:
	count+=len(wn.synsets(lemma,type))

print("average polysmey",count/len(lemmas))
