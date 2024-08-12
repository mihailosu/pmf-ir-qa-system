import json
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors

with open('indexer_questions.json', 'r') as file:
    data = json.load(file)
    
questions = pd.read_json('indexer_questions.json')

print(questions)