import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint
from sklearn import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import re

import streamlit as st
import requests

# Streamlit UI
st.title("Tense Prediction")

sentence = st.text_input("Enter a Sentence:")

if sentence.strip() == '':
    st.warning('Please enter a sentence.')
else:
    # Make an HTTP request to your Flask backend
    response = requests.post("http://localhost:5000/predict_tense", json={"sentence": sentence})
    
    if response.status_code == 200:
        predicted_tense = response.json().get("predicted_tense")
        st.success(f'Predicted Tense: {predicted_tense}')
    else:
        st.error('Error predicting tense.')

if __name__ == "__main__":
    st.button("Run Streamlit App")

# Flask Backend
from flask import Flask, request, jsonify

application = Flask(__name__, template_folder='templates')
application.secret_key = '1d7e11875835300d5bdd0df069189c8e'

# Define your tense prediction route
@application.route("/predict_tense", methods=["POST"])
def predict_tense():
    data = request.json
    sentence = data.get("sentence")

    # Perform tense prediction logic here using your existing code
    # Replace this with your tense prediction logic
    predicted_tense = "Simple Present"

    return jsonify({"predicted_tense": predicted_tense})

if __name__ == "__main__":
    application.run(debug=True)



# model = pickle.load(open('model.pkl', 'rb'))
# vectorizer = pickle.load(open("vectorizer.pkl", 'rb'))

# tenseMapping = {
#     11: 'Simple Present',
#     6: 'Present Continuous',
#     7: 'Present Perfect',
#     8: 'Present Perfect Continuous',
#     10: 'Simple Past',
#     3: 'Past Continuous ',
#     4: 'Past Continuous ',
#     5: 'Past Perfect',
#     9: 'Past Perfect Continuous',
#     0: 'Past Perfect Continuous',
#     1: 'Simple Future',
#     2: 'Simple Future'}

# st.title("Tense Prediction")

# sentence = st.text_input("Enter a Sentence:")

# if sentence.strip() == '':
#     st.warning('Please enter a sentence.')
# else:
#     sentence = sentence.lower()  # Convert to lowercase
#     sentence = re.sub(r'\W', ' ', sentence)  # Remove non-alphanumeric characters
#     sentence = re.sub(r'\s+', ' ', sentence)  # Remove extra whitespaces

#     custom_sentence_vector = vectorizer.transform([sentence]).toarray()

#     predicted_tense = model.predict(custom_sentence_vector)[0]
#     predicted_tense = tenseMapping[predicted_tense]

#     st.success(f'Predicted Tense: {predicted_tense}')
