story1 = story1.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold() 
story2 = story2.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold() 

story1_words = story1.split(" ") 
print("First Story words :",story1_words) 
story2_words = story2.split(" ") 
print("Second Story words :",story2_words)


story1_vocab = set(story1_words) 
print("First Story vocabulary :",story1_vocab)
story2_vocab = set(story2_words)
print("Second Story vocabulary",story2_vocab)

common_vocab = story1_vocab & story2_vocab 
print("Common Vocabulary :",common_vocab)