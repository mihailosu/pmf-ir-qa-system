import json
import numpy as np
import pandas as pd
import torch
import requests
from torchtext.vocab import GloVe
from tensorflow.keras.models import load_model
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

# Load GloVe embeddings
glove = GloVe(name="6B", dim=50) # load glove embeddings

app = FastAPI() # create FastAPI app

# response = requests.get("http://127.0.0.1:8000/") # fetch json data from a server


def preprocess_question(question, glove): # first we need to preprocess the questions
    tokens = question.lower().split()
    vectors = [glove[token] for token in tokens if token in glove] # filter tokens that are in glove vocabulary
    if len(vectors) == 0:
        return np.zeros(glove.dim) # return a zero vector if no tokens are found
    vector = torch.mean(torch.stack(vectors), dim=0).numpy()
    return vector

@app.post("/process-questions/")
async def process_questions(request: Request):
    questions_json = await request.json()  # Receive the JSON data
    questions = pd.DataFrame(questions_json)  # convert JSON to DataFrame

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
    return JSONResponse(content=best_question_answer)  # Return the best question and answer


    # print(best_question_answer)
    # PREVIOUS SOLUTION -> sent asnwer to a .json file
    # with open('output/best_question_answer.json', 'w') as json_file:
    #     json.dump(best_question_answer, json_file, indent=4)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)  # Run the FastAPI server on port 3000

# @app.get("/")
# def get_best_question_answer():
#     return JSONResponse(content=best_question_answer) # prepare json

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8080) # send best_question_answer json to port 8080