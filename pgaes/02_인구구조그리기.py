import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
@st.cache
def load_data():
    file_path = "age2411.csv"  # 파일명을 맞게 설정
    data = pd.read_csv(file_path)
    return data

data = load_data()

# Streamlit 앱 제목
st.title("인구 데이터 시각화")
st.write("서울특별시와 각 행정구역의 연령별 인구 데이터를 분석해보세요!")

# 선택 옵션: 행정구역
regions = data['행정구역'].unique()
selected_region = st.selectbox("행정구역을 선택하세요", regions)

# 선택한 행정구역의 데이터 필터링
region_data = data[data['행정구역'] == selected_region]

# 0~12세 인구 합산
age_columns = [col for col in data.columns if '계_' in col and '세' in col]
region_data['어린이_인구'] = region_data[age_columns[:13]].sum(axis=1)

# 시각화: 어린이 인구
st.subheader(f"{selected_region} 어린이 인구 (0~12세)")
st.write(f"{selected_region}의 어린이 인구를 확인하세요.")
fig, ax = plt.subplots()
ax.bar(age_columns[:13], region_data[age_columns[:13]].iloc[0])
ax.set_title("연령별 어린이 인구")
ax.set_xlabel("나이")
ax.set_ylabel("인구 수")
st.pyplot(fig)

# 전체 구역 비교
st.subheader("전체 구역 어린이 인구 비교")
data['어린이_인구'] = data[age_columns[:13]].sum(axis=1)
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(data['행정구역'], data['어린이_인구'])
ax.set_title("행정구역별 어린이 인구 비교")
ax.set_xlabel("행정구역")
ax.set_ylabel("어린이 인구 수")
ax.tick_params(axis='x', rotation=90)
st.pyplot(fig)

# 사용자 피드백
st.write
