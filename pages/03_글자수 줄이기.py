import streamlit as st

def truncate_to_bytes(text, max_bytes, encoding='utf-8'):
    """텍스트를 특정 바이트 단위로 잘라 반환하는 함수."""
    encoded_text = text.encode(encoding)
    if len(encoded_text) <= max_bytes:
        return text
    truncated_text = encoded_text[:max_bytes]
    while True:
        try:
            return truncated_text.decode(encoding)
        except UnicodeDecodeError:
            truncated_text = truncated_text[:-1]

# Streamlit UI 구성
st.title("바이트 단위 요약기")
st.write("입력한 텍스트를 지정된 바이트 수에 맞춰 요약합니다.")

# 텍스트 입력
user_input = st.text_area("텍스트를 입력하세요", height=200)
max_bytes = st.number_input("최대 바이트 수", min_value=1, value=100, step=1)

if st.button("요약하기"):
    if user_input.strip():
        summary = truncate_to_bytes(user_input, max_bytes)
        st.subheader("요약된 텍스트")
        st.text_area("요약 결과", summary, height=200)
        st.write(f"요약된 텍스트 길이: {len(summary.encode('utf-8'))} 바이트")
    else:
        st.warning("텍스트를 입력해주세요!")
