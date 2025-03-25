from flask import Flask, request, jsonify, render_template 
import re
import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords  # Import stopwords from nltk.corpus
app = Flask(__name__)

# Load the model, vectorizer, and label encoder
with open('model/model.pkl', 'rb') as model_file:
    naive_bayes_model = pickle.load(model_file)
with open('model/vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)
with open('model/label_encoder.pkl', 'rb') as le_file:
    label_encoder = pickle.load(le_file)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data['question']
    
    # Preprocess the question
    question_preprocessed = data_prep(question)
    
    # Vectorize the question
    question_vectorized = tfidf_vectorizer.transform([question_preprocessed])
    
    # Predict the answer
    answer_code = naive_bayes_model.predict(question_vectorized)
    answer = label_encoder.inverse_transform(answer_code)[0]
    
    return jsonify({'answer': answer})

def data_prep(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = " ".join(t for t in text.split() if t not in stopwords.words('english'))
    return text

if __name__ == '__main__':
    app.run(debug=True)
