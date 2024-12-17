import streamlit as st
import re

def shorten_text(text, target_bytes):
    # 축약어 사전
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
    
    # 축약어 적용
    for full, contraction in contractions.items():
        text = re.sub(r'\b' + full + r'\b', contraction, text, flags=re.IGNORECASE)
    
    # 불필요한 공백 제거
    text = ' '.join(text.split())
    
    # 목표 바이트 수에 맞추기
    while len(text.encode('utf-8')) > target_bytes and len(text) > 0:
        text = text[:-1]
    
    return text

st.title('텍스트 글자 수 줄이기')

input_text = st.text_area("줄일 텍스트를 입력하세요:", height=200)
target_bytes = st.number_input("목표 바이트 수:", min_value=1, value=100)

if st.button('글자 수 줄이기'):
    if input_text:
        shortened = shorten_text(input_text, target_bytes)
        st.write("줄어든 텍스트:")
        st.write(shortened)
        st.write(f"원본 바이트 수: {len(input_text.encode('utf-8'))}")
        st.write(f"줄어든 바이트 수: {len(shortened.encode('utf-8'))}")
    else:
        st.write("텍스트를 입력해주세요.")
