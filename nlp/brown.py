import nltk
from nltk.corpus import brown 

print(brown.categories())


genres = ['fiction', 'humor', 'romance'] 
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who'] 

for i in range(len(genres)):
	gener = genres[i]
	print("analyzing text")
	words = brown.words(categories=gener)
	fdist = nltk.FreqDist(words)
	for wh in whwords:
		print(wh,fdist[wh])

#word with maximun occurence
print(fdist[fdist.max()])
#unique words
print(fdist.N())
#10 most common
print(fdist.most_common(10))
#tabulate the entire frequency distribution
print(fdist.tabulate())
#plot the graph
fdist.plot(cumulative=True)