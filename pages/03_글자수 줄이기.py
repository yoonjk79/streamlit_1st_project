import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk
import os

nltk_data_dir = os.path.expanduser('~/nltk_data')
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_dir, quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=nltk_data_dir, quiet=True)

nltk.data.path.append(nltk_data_dir)


# NLTK 데이터 다운로드
nltk.download('punkt')
nltk.download('stopwords')

def shorten_text(text, target_length):
    # 단어 토큰화
    words = word_tokenize(text)
    
    # 불용어 제거
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # 축약형 사용
    contractions = {
        "are not": "aren't", "cannot": "can't", "could not": "couldn't",
        "did not": "didn't", "does not": "doesn't", "do not": "don't",
        "had not": "hadn't", "has not": "hasn't", "have not": "haven't",
        "he is": "he's", "she is": "she's", "it is": "it's",
        "i am": "I'm", "i will": "I'll", "i have": "I've",
        "let us": "let's", "might not": "mightn't", "must not": "mustn't",
        "should not": "shouldn't", "that is": "that's", "they are": "they're",
        "they have": "they've", "we are": "we're", "we have": "we've",
        "were not": "weren't", "what is": "what's", "will not": "won't",
        "would not": "wouldn't", "you are": "you're", "you have": "you've"
    }
    
    for i, word in enumerate(filtered_words):
        for full, contraction in contractions.items():
            if word.lower() == full.split()[0]:
                if i+1 < len(filtered_words) and filtered_words[i+1].lower() == full.split()[1]:
                    filtered_words[i] = contraction
                    filtered_words.pop(i+1)
                    break
    
    # 목표 길이에 맞춰 단어 선택
    shortened_text = ' '.join(filtered_words[:target_length])
    
    return shortened_text

st.title('텍스트 축소기')

input_text = st.text_area("축소할 텍스트를 입력하세요:", height=200)
target_length = st.slider("목표 단어 수:", min_value=10, max_value=500, value=100)

if st.button('축소하기'):
    if input_text:
        shortened = shorten_text(input_text, target_length)
        st.write("축소된 텍스트:")
        st.write(shortened)
        st.write(f"원본 단어 수: {len(word_tokenize(input_text))}")
        st.write(f"축소된 단어 수: {len(word_tokenize(shortened))}")
    else:
        st.write("텍스트를 입력해주세요.")
