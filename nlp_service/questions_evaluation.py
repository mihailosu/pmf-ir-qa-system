import json
# from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors

# Load your pre-trained Word2Vec model
# word2vec = KeyedVectors.load_word2vec_format("~/DEV/envs/pmf-projekat/GoogleNews-vectors-negative300.bin", binary=True)

# Load your saved Siamese model
# model = load_model('model/siamese_model.h5')

# Load the JSON file
with open('indexer_questions.json', 'r') as file:
    data = json.load(file)
    


questions = pd.read_json('indexer_questions.json')

print(questions)


# Extract the user's question (the 11th question)
users_question = data[10] #['q']

#print(users_question)

# # Define a function to vectorize the questions using Word2Vec
# def vectorize_question(question, word2vec):
#     words = question.split()
#     vectors = [word2vec[word] for word in words if word in word2vec]
#     if vectors:
#         return np.mean(vectors, axis=0)
#     else:
#         return np.zeros(word2vec.vector_size)

# # Vectorize the user's question
# users_question_vector = vectorize_question(users_question, word2vec)

# # Vectorize the first 10 questions
# question_vectors = np.array([vectorize_question(item['q'], word2vec) for item in data[:10]])

# # Expand dimensions to match the input shape of the model
# users_question_vector_expanded = np.expand_dims(users_question_vector, axis=0)

# # Initialize list to store similarity scores
# similarity_scores = []

# # Evaluate similarity for each question pair
# for question_vector in question_vectors:
#     # Expand dimensions to match the input shape of the model
#     question_vector_expanded = np.expand_dims(question_vector, axis=0)
    
#     # Predict similarity using the Siamese network
#     similarity = model.predict([users_question_vector_expanded, question_vector_expanded])
    
#     # Store the similarity score
#     similarity_scores.append(similarity[0][0])

# # Find the index of the highest similarity
# best_match_idx = np.argmax(similarity_scores)

# # Retrieve the best matching question and its answer
# best_question = data[best_match_idx]['q']
# best_answer = data[best_match_idx]['a']

# # Create a new JSON structure with the best match
# best_match = {
#     "best_match_question": best_question,
#     "best_match_answer": best_answer
# }

# # Save the best match to a new JSON file
# with open('best_match.json', 'w') as outfile:
#     json.dump(best_match, outfile, indent=4)

# print("The best matching question and its answer have been saved to 'best_match.json'.")
