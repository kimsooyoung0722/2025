import streamlit as st

# MBTI 데이터
courses = {
    "ENFP": {
        "description": "창의적이고 에너지가 넘치며 새로운 아이디어를 즐깁니다.",
        "recommendations": [
            {"title": "창의적 문제 해결 워크숍", "desc": "창의성을 활용해 실제 문제를 해결하는 실습 과정", "link": "https://example.com"},
            {"title": "리더십과 커뮤니케이션", "desc": "팀워크와 리더십 스킬 향상 과정", "link": "https://example.com"}
        ]
    },
    "ISTJ": {
        "description": "체계적이고 책임감이 강하며 현실적인 계획을 선호합니다.",
        "recommendations": [
            {"title": "프로젝트 관리 입문", "desc": "효율적인 프로젝트 관리 기술", "link": "https://example.com"},
            {"title": "데이터 분석 기본", "desc": "정확한 의사결정을 위한 데이터 분석", "link": "https://example.com"}
        ]
    }
}

st.title("MBTI 기반 맞춤형 교육과정 추천")

mbti_list = list(courses.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

if st.button("추천 받기"):
    st.subheader(f"당신의 MBTI: {selected_mbti}")
    st.write(courses[selected_mbti]["description"])
    
    st.markdown("### 추천 교육과정")
    for course in courses[selected_mbti]["recommendations"]:
        st.markdown(f"**{course['title']}**  \n{course['desc']}  \n[자세히 보기]({course['link']})")




