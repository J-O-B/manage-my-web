import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('chatbot_model.h5')

import json
import random

intents = json.loads(open('talk_intents.json', encoding='utf-8').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


# Reduce words in sentence to their source
def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# Convert words into binary style format for neural processing
def group_of_words(sentence, words):
    # Tokenize pattern
    sentence_words = clean_sentence(sentence)
    # Start with only 0
    group = [0] * len(words)
    for section in sentence_words:
        for i, word in enumerate(words):
            if word == section:
                # Assign 1 instead of a 0 
                group[i] = 1
    return(np.array(group))


# Predictions using the trained model
def predict(sentence, model):
    # Throw away predictions that are outside error threshold
    input = group_of_words(sentence, words)
    result = model.predict(np.array([input]))[0]
    ERROR_THRESHOLD = 0.2
    results = [[i,r] for i, r in enumerate(result) if r > ERROR_THRESHOLD]

    # Bring the most probable result to top
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


# Get a response to return
def chatbot_response(message):
    ints = predict_class(message, model)
    result = getResponse(ints, intents)
    return result
