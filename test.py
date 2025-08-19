import streamlit as st

courses = {
    "일본": {
        "description": "전통과 현대가 공존하는 문화, 세밀한 장인정신과 조화의 가치를 중시.",
        "recommendations": [
            {"title": "일본 전통 예절 교육", "desc": "다도, 와식 문화, 의례 이해", "link": "https://example.com"},
            {"title": "애니메이션과 스토리텔링", "desc": "일본 대중문화를 통한 창의적 이야기 학습", "link": "https://example.com"}
        ]
    },
    "프랑스": {
        "description": "예술과 철학의 중심지, 자유와 토론, 창의적 표현을 중시.",
        "recommendations": [
            {"title": "프랑스 미술사 탐구", "desc": "인상주의부터 현대미술까지 흐름 이해", "link": "https://example.com"},
            {"title": "프랑스식 토론 교육", "desc": "비판적 사고와 설득력 있는 토론 훈련", "link": "https://example.com"}
        ]
    },
    "인도": {
        "description": "다양한 종교와 전통, 영성과 공동체적 가치를 중시.",
        "recommendations": [
            {"title": "인도 철학과 요가", "desc": "명상과 요가를 통한 자기 성찰", "link": "https://example.com"},
            {"title": "다문화 공존 교육", "desc": "인도의 다원적 사회 구조 이해", "link": "https://example.com"}
        ]
    }
}

st.title("세계 문화 기반 맞춤형 교육과정 추천")

country = st.selectbox("관심 있는 나라를 선택하세요:", list(courses.keys()))

if st.button("추천 받기"):
    st.subheader(f"선택한 나라: {country}")
    st.write(courses[country]["description"])

    st.markdown("### 추천 교육과정")
    for course in courses[country]["recommendations"]:
        st.markdown(f"**{course['title']}**  \n{course['desc']}  \n[자세히 보기]({course['link']})")


