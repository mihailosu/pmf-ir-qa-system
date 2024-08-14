# THIS FILE CAN BE IGNORED/ERASED -> contents used now in main.py

import json
import numpy as np
import pandas as pd
import torch
from torchtext.vocab import GloVe
from tensorflow.keras.models import load_model

glove = GloVe(name="6B", dim=50)
questions = pd.read_json('indexer_questions.json')

# print(questions)

def preprocess_question(question, glove): # first we need to preprocess the questions
    tokens = question.lower().split()
    vectors = [glove[token] for token in tokens if token in glove] # filter tokens that are in glove vocabulary
    if len(vectors) == 0:
        return np.zeros(glove.dim) # return a zero vector if no tokens are found
    vector = torch.mean(torch.stack(vectors), dim=0).numpy()
    return vector

vectors = []
for index, question in questions['q'].items():
    question_vector = preprocess_question(question, glove)
    question_vector = np.expand_dims(question_vector, axis=0) # reshape to match the input expected by the model
    vectors.append(question_vector)

questions['vector'] = vectors
users_question = questions.iloc[[-1]]
# print(users_question)

questions = questions.drop(questions.index[-1])
# print(questions)

users_question = questions.iloc[[-1]]


siamese_network = load_model('model/siamese_model.h5') # load the model

similarity_scores = []
user_vector = users_question['vector'].values[0]

for vector in questions['vector']:
    vector = np.squeeze(vector)
    user_vector = np.squeeze(user_vector)
    
    similarity_score = siamese_network.predict([np.expand_dims(vector, axis=0), np.expand_dims(user_vector, axis=0)]) # compute similarity
    similarity_scores.append(similarity_score[0][0])  # append to list


questions['similarity_score'] = similarity_scores # add column

# print(questions)

questions_sorted = questions.sort_values(by='similarity_score', ascending=False)
# print(questions_sorted)
# print(questions_sorted.iloc[0]) 
# print(questions_sorted.iloc[0][['q', 'a']]) 

best_question_answer = questions_sorted.iloc[0][['q', 'a']].to_dict()
# print(best_question_answer)


with open('output/best_question_answer.json', 'w') as json_file:
    json.dump(best_question_answer, json_file, indent=4)