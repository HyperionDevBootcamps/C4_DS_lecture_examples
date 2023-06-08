# For install : 
# pip install spacy
# python -m spacy download en_core_web_sm
import spacy

# language model
nlp = spacy.load('en_core_web_sm')

sample = "The quick brown fox, jumps over the lazy dog."
#print(sample.split()) # Primitive

doc = nlp(sample)

# how spacey sees the sentence
#print([token.orth_ for token in doc])

# leaving out the underscore gives the integer code of the word
#print([(token, token.orth_, token.orth) for token in doc])

# words that spacey thinks are stop words
'''for word in doc:
    if word.is_stop == True:
        print(word)'''

# Lemmatisation gives the origin word
sample = "sing sang singing"
doc = nlp(sample)

#print([token.lemma_ for token in doc])

# Entity Recognition
wiki_priyanka = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

nlp_priyanka = nlp(wiki_priyanka)
print([(i, i.label_, i.label) for i in nlp_priyanka.ents])

entity_fac = spacy.explain("CARDINAL")
print(f"CARDINAL:{entity_fac}")