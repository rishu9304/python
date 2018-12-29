from nltk.corpus import wordnet as wd 
chair = 'chair'

chair_synsets = wd.synsets(chair)
print("senses of chair",chair_synsets)

for syn in chair_synsets:
	print("defination :",syn.definition())
	print("lemma :",syn.lemma_names())
	print("example :",syn.examples())