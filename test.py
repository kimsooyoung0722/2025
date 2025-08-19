import streamlit as st

# ----------------------------
# 국가별 문화 & 교육과정 데이터
# ----------------------------
courses = {
    "일본": {
        "description": "전통과 현대가 공존하는 문화, 세밀한 장인정신과 조화의 가치를 중시.",
        "recommendations": [
            {"title": "일본 전통 예절 교육", "desc": "다도, 와식 문화, 의례 이해", "link": "https://example.com/japan1"},
            {"title": "애니메이션과 스토리텔링", "desc": "일본 대중문화를 통한 창의적 이야기 학습", "link": "https://example.com/japan2"}
        ]
    },
    "프랑스": {
        "description": "예술과 철학의 중심지, 자유와 토론, 창의적 표현을 중시.",
        "recommendations": [
            {"title": "프랑스 미술사 탐구", "desc": "인상주의부터 현대미술까지 흐름 이해", "link": "https://example.com/france1"},
            {"title": "프랑스식 토론 교육", "desc": "비판적 사고와 설득력 있는 토론 훈련", "link": "https://example.com/france2"}
        ]
    },
    "인도": {
        "description": "다양한 종교와 전통, 영성과 공동체적 가치를 중시.",
        "recommendations": [
            {"title": "인도 철학과 요가", "desc": "명상과 요가를 통한 자기 성찰", "link": "https://example.com/india1"},
            {"title": "다문화 공존 교육", "desc": "인도의 다원적 사회 구조 이해", "link": "https://example.com/india2"}
        ]
    },
    "이탈리아": {
        "description": "르네상스의 발상지, 예술과 미식, 감각적 경험을 중시.",
        "recommendations": [
            {"title": "이탈리아 르네상스 미술", "desc": "다빈치와 미켈란젤로를 중심으로", "link": "https://example.com/italy1"},
            {"title": "이탈리아 요리 체험", "desc": "파스타와 피자를 직접 만들어보기", "link": "https://example.com/italy2"}
        ]
    },
    "브라질": {
        "description": "다양한 민족과 리듬의 문화, 축제와 음악이 삶의 중심.",
        "recommendations": [
            {"title": "삼바와 카니발", "desc": "브라질 축제 문화 체험", "link": "https://example.com/brazil1"},
            {"title": "브라질 환경 교육", "desc": "아마존 보존과 지속가능성 이해", "link": "https://example.com/brazil2"}
        ]
    },
    "이집트": {
        "description": "고대 문명의 뿌리, 역사와 전통을 중시.",
        "recommendations": [
            {"title": "고대 이집트 역사", "desc": "피라미드와 파라오 이야기", "link": "https://example.com/egypt1"},
            {"title": "이집트 상형문자 배우기", "desc": "히에로글리프 기초 학습", "link": "https://example.com/egypt2"}
        ]
    },
    "한국": {
        "description": "전통과 첨단 기술이 융합된 문화, 공동체와 효를 중시.",
        "recommendations": [
            {"title": "한식 요리 교실", "desc": "비빔밥과 김치 만들기", "link": "https://example.com/korea1"},
            {"title": "K-팝과 현대문화", "desc": "세계에 확산된 한류 이해", "link": "https://example.com/korea2"}
        ]
    },
    "미국": {
        "description": "다양성과 자유, 혁신과 도전 정신을 중시.",
        "recommendations": [
            {"title": "실리콘밸리 창업 문화", "desc": "스타트업 생태계 탐구", "link": "https://example.com/usa1"},
            {"title": "미국 민주주의 이해", "desc": "헌법과 시민 사회", "link": "https://example.com/usa2"}
        ]
    },
    "중국": {
        "description": "오랜 역사와 철학, 집단과 조화를 중시.",
        "recommendations": [
            {"title": "중국 철학과 사상", "desc": "유교, 도교, 불교 이해", "link": "https://example.com/china1"},
            {"title": "중국 서예 체험", "desc": "붓글씨를 통한 예술적 감각 배우기", "link": "https://example.com/china2"}
        ]
    },
    "멕시코": {
        "description": "원주민과 스페인 문화가 어우러진 다채로운 전통.",
        "recommendations": [
            {"title": "죽음의 날 축제 이해", "desc": "멕시코 고유의 기념일 문화", "link": "https://example.com/mexico1"},
            {"title": "멕시코 음식 문화", "desc": "타코와 전통 요리 체험", "link": "https://example.com/mexico2"}
        ]
    }
}

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="세계 문화 기반 교육과정 추천", page_icon="🌍", layout="wide")

st.title("세계 문화 기반 맞춤형 교육과정 추천")
st.caption("관심 있는 나라를 선택하면, 그 나라의 문화적 특징에 맞춘 교육과정을 추천합니다.")

country = st.selectbox("관심 있는 나라를 선택하세요:", list(courses.keys()))

if st.button("추천 받기"):
    st.subheader(f"선택한 나라: {country}")
    st.write(courses[country]["description"])

    st.markdown("### 추천 교육과정")
    for course in courses[country]["recommendations"]:
        with st.container(border=True):
            st.markdown(f"**{course['title']}**  ")
            st.markdown(course['desc'])
            st.markdown(f"[자세히 보기]({course['link']})")

st.markdown("---")
st.caption("© 2025 World Culture Curriculum Recommender • 예시 링크는 대체 URL입니다.")



