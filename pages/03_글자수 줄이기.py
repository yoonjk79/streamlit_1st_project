import streamlit as st
from transformers import pipeline
import textwrap

# 요약 함수
def summarize_text(text, max_bytes, encoding="utf-8"):
    summarizer = pipeline("summarization", model="t5-small")
    
    # 원문 요약 수행
    summarized = summarizer(text, max_length=300, min_length=50, do_sample=False)
    summary_text = summarized[0]["summary_text"]
    
    # 바이트 단위로 자르기 (문자가 잘리지 않도록 처리)
    encoded_summary = summary_text.encode(encoding)
    if len(encoded_summary) <= max_bytes:
        return summary_text
    truncated_summary = encoded_summary[:max_bytes]
    while True:
        try:
            return truncated_summary.decode(encoding)
        except UnicodeDecodeError:
            truncated_summary = truncated_summary[:-1]

# Streamlit UI
st.title("텍스트 요약기")
st.write("원문 내용을 유지하면서 지정된 바이트 수로 텍스트를 요약합니다.")

# 텍스트 입력
user_input = st.text_area("요약할 텍스트를 입력하세요:", height=200)
max_bytes = st.number_input("최대 바이트 수:", min_value=1, value=500, step=10)

if st.button("요약하기"):
    if user_input.strip():
        try:
            summary = summarize_text(user_input, max_bytes)
            st.subheader("요약된 텍스트")
            st.text_area("요약 결과:", summary, height=200)
            st.write(f"요약된 텍스트 길이: {len(summary.encode('utf-8'))} 바이트")
        except Exception as e:
            st.error(f"요약 중 오류가 발생했습니다: {e}")
    else:
        st.warning("텍스트를 입력해주세요!")
