'''
You work for a tourism agency. 
Part of your company's customer benefits is personalised dining experiences. 
You are tasked with creating a program that will recommend dining experiences given a customer's description of what and where they like to eat.
'''

import spacy

def find_dining_experience(description):

    nlp = spacy.load('en_core_web_md')

    # Read dining experience descriptions from the text file 
    file = open('Dining_experiences.txt', 'r')

    # Store dining descriptions in a list
    dining_descriptions = file.read().splitlines()
    #print(dining_descriptions)

    file.close()

    # Obtain similarity scores between customer's description and each dining experience description
    # Create empty list to store scores   
    similarity_scores = []
    for dining in dining_descriptions:
        doc1 = nlp(dining)      # dining desription from list
        doc2 = nlp(description) # customer description
        similarity_scores.append(doc1.similarity(doc2))

    #print(similarity_scores)
    max_score = max(similarity_scores)

    # Get index of the most similar dining experience
    max_index = similarity_scores.index(max_score)

    return dining_descriptions[max_index]

# Example
customer_description_1 = "I really enjoy trying different types of food. I am not really picky when it comes to cuisine types. From spicy Thai curries to Italian pasta dishes. And when it comes to how much things cost, I am willing to spend anything on a good dining experience."
rec_dining_1 = find_dining_experience(customer_description_1)
print("Recommended dining experience for person 1 is", rec_dining_1)

customer_description_2 = "I like burgers and fries. I don't mind eating outside or indoors, as long as I'm surrounded by good company. Also, if it's too expensive, there's food at home."
rec_dining_2 = find_dining_experience(customer_description_2)
print("Recommended dining experience for person 2 is", rec_dining_2)