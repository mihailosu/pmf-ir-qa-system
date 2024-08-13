import json
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from tensorflow.keras.models import load_model

questions = pd.read_json('indexer_questions.json')

# print(questions)

# load pre-trained Word2Vec model -> download from https://code.google.com/archive/p/word2vec/
word2vec_model = KeyedVectors.load_word2vec_format('~/DEV/envs/pmf-projekat/GoogleNews-vectors-negative300.bin', binary=True)

def preprocess_question(question, word2vec_model): # first we need to preprocess the questions
    tokens = question.lower().split()
    vector = np.mean([word2vec_model[token] for token in tokens if token in word2vec_model], axis=0)
    return vector


vectors = []


for index, question in questions['q'].items():
    question_vector = preprocess_question(question, word2vec_model)
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

# questions_sorted = questions_sorted.drop('vector')

# print(questions_sorted)
# print(questions_sorted.iloc[0]) 
# print(questions_sorted.iloc[0][['q', 'a']]) 

best_question_answer = questions_sorted.iloc[0][['q', 'a']].to_dict()
# print(best_question_answer)

with open('best_question_answer.json', 'w') as json_file:
    json.dump(best_question_answer, json_file, indent=4)