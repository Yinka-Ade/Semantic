# Similarity with spacy
import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
I noted that the similarity between apple and banana is the highest which was 0.66. 
I think the reason could be attributed to the fact that both items are both fruits. 
It was also noted that cat and monkey had the second largest similaries probably because
they are both animals
Furthermore, monkey and banana had a similarity of 0.40. This could mean that the system
might understand that monkeys eat banana. 
Every other similaries were low 0.2.  
'''

# # Working with Vectors
# tokens = nlp('cat apple monkey banana ')
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))

# # Working with sentences
# sentence_to_compare = "Why is my cat on the car"
# sentences = ["where did my dog go",
# "Hello, there is my car",
# "I\'ve lost my car in my car",
# "I\'d like my boat back",
# "I will name my dog Diana"]
# model_sentence = nlp(sentence_to_compare)
# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", similarity)


# My example
nlp1 = spacy.load('en_core_web_sm')
word1 = nlp1("cat")
word2 = nlp1("monkey")
word3 = nlp1("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
