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
NOTES
1. It was noted that cat and monkey had the largest similarity 0.59 probably because
they are both animals.

2. Furthermore, monkey and banana had a similarity of 0.40. This could mean that the system
might understand that monkeys eat banana. 

3. Banana and Cat had low "0.2" similarities this could be because their are really
no sililarities between both objects.  
'''

# Running an example file to compare man, woman and boy
word4 = nlp("man")
word5 = nlp("woman")
word6 = nlp("baby")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))


'''
OUTPUT
0.8273442557707831
0.41037265743069984
0.3225720635550094
'''

# Running the example file with the simpler language 'sm'
nlp1 = spacy.load('en_core_web_sm')
word4 = nlp1("man")
word5 = nlp1("woman")
word6 = nlp1("baby")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

''' 
OUTPUT
0.9191394981521782
0.797183715938096
0.8499397635691874
'''

'''
COMPARISON
When comaring both languages, I noted the following
1. The simpler language model gave a user warning which is UserWarning: [W007] The model
 you're using has no word vectors loaded, so the result of the Doc.similarity method will
be based on the tagger, parser and NER, which may not give useful similarity judgements. 

2. The similarities for man and woman are the highest in both languages(0.82, 0.91) although 
the smaller language estimated the highest similarity of 0.91

3. In comparing man and baby, woman and baby, the smaller language recorded that man and baby
has higher similarity of 0.84 and that woman and baby has a similarity of 0.79.
I personally dont agree with this.

4. In comparing man and baby, woman and baby, the medium language recorded that woman and baby
has higher similarity of 0.41 and that man and baby has a similarity of 0.32.
I was really hoping that woman and baby would have a high similarity.
'''