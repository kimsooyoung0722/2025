import streamlit as st
from dataclasses import dataclass
from typing import List, Dict, Any
import pandas as pd

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="MBTI 기반 맞춤형 교육과정 추천",
    page_icon="🎯",
    layout="wide",
)

# ----------------------------
# Data models
# ----------------------------
@dataclass
class Course:
    id: str
    title: str
    desc: str
    tags: List[str]
    difficulty: str  # Beginner / Intermediate / Advanced
    duration_hours: int
    delivery: str  # Online / Offline / Blended
    link: str

# ----------------------------
# Course catalog (샘플)
# ----------------------------
CATALOG: List[Course] = [
    Course("C101", "디자인 씽킹 부트캠프", "문제정의부터 아이데이션, 프로토타이핑까지 전 과정 실습.", ["innovation", "creativity", "facilitation"], "Beginner", 12, "Offline", "https://example.com/design-thinking"),
    Course("C102", "데이터 분석 입문", "파이썬과 스프레드시트로 데이터 기초 분석.", ["data", "logic", "analysis"], "Beginner", 14, "Online", "https://example.com/data101"),
    Course("C103", "커뮤니케이션 & 프레젠테이션", "스토리텔링 기반 발표와 설득 스킬.", ["communication", "leadership"], "Beginner", 8, "Blended", "https://example.com/comms"),
    Course("C104", "프로젝트 관리(PMBOK)", "일정/범위/리스크를 체계적으로 관리.", ["process", "organization", "planning"], "Intermediate", 16, "Online", "https://example.com/pmp"),
    Course("C105", "애자일 & 스크럼 실전", "스프린트, 백로그, 레트로스펙티브까지 실습.", ["agile", "teamwork", "experimentation"], "Intermediate", 10, "Offline", "https://example.com/agile"),
    Course("C106", "리더십 Essentials", "상황적 리더십, 동기부여, 코칭.", ["leadership", "people"], "Intermediate", 12, "Blended", "https://example.com/leadership"),
    Course("C107", "UX 리서치 기초", "사용자 인터뷰, 여정지도, 페르소나 작성.", ["ux", "empathy", "people"], "Beginner", 10, "Online", "https://example.com/ux"),
    Course("C108", "고급 데이터 시각화", "인사이트 중심의 대시보드 설계.", ["data", "visualization", "story"], "Advanced", 18, "Online", "https://example.com/dataviz"),
    Course("C109", "문제 해결과 비판적 사고", "MECE, 가설검증, 논증 구조화.", ["logic", "analysis", "problem-solving"], "Intermediate", 9, "Offline", "https://example.com/critical"),
    Course("C110", "팀 퍼실리테이션 워크샵", "회의 설계, 참여 촉진, 갈등 중재.", ["facilitation", "communication", "people"], "Intermediate", 8, "Offline", "https://example.com/facilitation"),
    Course("C111", "클라우드 기초", "클라우드 서비스 개념과 실습.", ["systems", "operations", "planning"], "Beginner", 12, "Online", "https://example.com/cloud"),
    Course("C112", "서비스 운영 최적화", "KPI 설계, 표준화, 장애 대응.", ["operations", "process", "organization"], "Advanced", 16, "Blended", "https://example.com/ops"),
    Course("C113", "창의 글쓰기 & 스토리", "아이디어 발상과 스토리 구조화.", ["creativity", "story", "communication"], "Beginner", 6, "Online", "https://example.com/story"),
    Course("C114", "협상 전략", "상호이득 기반 협상 프레임.", ["communication", "people", "leadership"], "Advanced", 8, "Offline", "https://example.com/negotiation"),
    Course("C115", "제품 로드맵 수립", "비전-전략-실행 로드맵.", ["planning", "organization", "leadership"], "Intermediate", 10, "Blended", "https://example.com/roadmap"),
]

# ----------------------------
# MBTI 설명 및 성향 -> 태그 매핑
# ----------------------------
MBTI_DESCRIPTIONS: Dict[str, str] = {
    "INTJ": "전략가형 — 장기적 비전과 체계적 문제 해결을 선호.",
    "INTP": "논리술사형 — 개념과 아이디어 탐구, 분석을 즐김.",
    "ENTJ": "지도자형 — 목표지향적, 조직과 실행에 강점.",
    "ENTP": "변론가형 — 새로운 아이디어, 토론과 실험을 즐김.",
    "INFJ": "옹호자형 — 의미와 가치를 중시, 사람과 비전을 연결.",
    "INFP": "중재자형 — 공감과 창의적 표현, 스토리에 강점.",
    "ENFJ": "선도자형 — 리더십과 코칭, 사람 성장에 동기.",
    "ENFP": "활동가형 — 창의성/에너지, 새로운 도전과 네트워킹.",
    "ISTJ": "현실주의자형 — 체계/책임, 표준화·프로세스 선호.",
    "ISFJ": "수호자형 — 헌신적, 안정적 운영과 지원.",
    "ESTJ": "경영자형 — 조직화와 실행, 결과 중심.",
    "ESFJ": "집정관형 — 협력과 서비스, 팀 조화 중시.",
    "ISTP": "장인형 — 문제 해결과 실험, 도구 활용에 능숙.",
    "ISFP": "모험가형 — 섬세한 미감, 사용자 경험/제작에 강점.",
    "ESTP": "사업가형 — 행동지향, 즉흥적 문제 해결.",
    "ESFP": "연예인형 — 에너지/커뮤니케이션, 실전 중심 학습.",
}

# 각 글자별 성향을 코스 태그로 매핑
LETTER_TO_TAGS: Dict[str, List[str]] = {
    "E": ["communication", "leadership", "facilitation", "teamwork"],
    "I": ["analysis", "problem-solving", "research", "logic"],
    "N": ["innovation", "creativity", "story", "experimentation"],
    "S": ["operations", "process", "organization", "systems"],
    "T": ["logic", "data", "analysis", "planning"],
    "F": ["people", "ux", "empathy", "communication"],
    "J": ["planning", "process", "organization"],
    "P": ["agile", "experimentation", "creativity"],
}

ALL_TYPES = list(MBTI_DESCRIPTIONS.keys())

# ----------------------------
# Helpers
# ----------------------------
def score_course_for_mbti(course: Course, mbti: str) -> int:
    score = 0
    for ch in mbti:
        for t in LETTER_TO_TAGS.get(ch, []):
            if t in course.tags:
                score += 2
    # 가벼운 가중치: 난이도/시간을 선호 편향 (I/N/T/J는 이론/중급 이상 선호, E/F/P는 활동/경험 선호)
    if set(mbti) & set("INTJ"):
        if course.difficulty in ("Intermediate", "Advanced"):
            score += 1
    if set(mbti) & set("EFP"):
        if any(tag in course.tags for tag in ["facilitation", "teamwork", "communication", "experimentation"]):
            score += 1
    return score


def recommend_courses(mbti: str, catalog: List[Course], top_k: int = 6) -> List[Course]:
    ranked = sorted(catalog, key=lambda c: score_course_for_mbti(c, mbti), reverse=True)
    return ranked[:top_k]


def filter_catalog(catalog: List[Course], delivery: str | None, max_hours: int | None, difficulty: List[str] | None) -> List[Course]:
    items = catalog
    if delivery and delivery != "전체":
        items = [c for c in items if c.delivery == delivery]
    if max_hours is not None:
        items = [c for c in items if c.duration_hours <= max_hours]
    if difficulty and len(difficulty) > 0:
        items = [c for c in items if c.difficulty in difficulty]
    return items


def validate_mbti(text: str) -> str | None:
    t = (text or "").upper().strip()
    if len(t) == 4 and t[0] in "EI" and t[1] in "NS" and t[2] in "TF" and t[3] in "JP":
        return t
    return None


# ----------------------------
# UI Components
# ----------------------------
def course_card(c: Course, score: int | None = None):
    with st.container(border=True):
        left, right = st.columns([5, 2])
        with left:
            st.markdown(f"### {c.title}")
            st.markdown(c.desc)
            st.markdown(
                f"**태그**: " + ", ".join([f"`{t}`" for t in c.tags])
            )
            st.markdown(f"난이도: **{c.difficulty}** · 예상 소요: **{c.duration_hours}h** · 방식: **{c.delivery}**")
        with right:
            if score is not None:
                st.metric("적합도", f"{score}")
            st.link_button("자세히 보기", c.link, use_container_width=True)


def render_result(mbti: str, catalog: List[Course]):
    st.subheader(f"당신의 MBTI: :blue[{mbti}]")
    st.write(MBTI_DESCRIPTIONS.get(mbti, ""))

    st.divider()
    st.markdown("#### 추천 교육과정")

    # 필터
    with st.expander("필터(선택)"):
        col1, col2, col3 = st.columns(3)
        with col1:
            delivery = st.selectbox("교육 방식", ["전체", "Online", "Offline", "Blended"], index=0)
        with col2:
            max_hours = st.slider("최대 소요 시간(시간)", 4, 24, 16)
        with col3:
            difficulty = st.multiselect("난이도", ["Beginner", "Intermediate", "Advanced"], default=[])

    filtered = filter_catalog(CATALOG, delivery, max_hours, difficulty)
    recs = recommend_courses(mbti, filtered, top_k=6)

    if not recs:
        st.info("필터 조건에 맞는 과정이 없습니다. 조건을 완화해 보세요.")
        return

    # 점수 계산 후 카드 렌더링
    data_rows = []
    for c in recs:
        s = score_course_for_mbti(c, mbti)
        course_card(c, s)
        data_rows.append({
            "ID": c.id,
            "제목": c.title,
            "난이도": c.difficulty,
            "시간(h)": c.duration_hours,
            "방식": c.delivery,
            "태그": ", ".join(c.tags),
            "적합도": s,
            "링크": c.link,
        })

    df = pd.DataFrame(data_rows)
    st.download_button(
        "추천 목록 CSV 다운로드",
        data=df.to_csv(index=False).encode("utf-8-sig"),
        file_name=f"{mbti}_추천과정.csv",
        mime="text/csv",
        use_container_width=True,
    )

    with st.expander("표 형태로 보기"):
        st.dataframe(df, use_container_width=True, hide_index=True)


# ----------------------------
# Quick MBTI Quiz (8문항)
# ----------------------------
QUIZ = [
    ("모임에서 나는", "E", "I", "새로운 사람들과 빨리 친해진다", "가까운 사람들과 조용히 있는 편이다"),
    ("정보를 받아들일 때", "S", "N", "사실과 디테일을 중시한다", "아이디어와 가능성을 본다"),
    ("결정할 때", "T", "F", "논리와 일관성을 본다", "사람과 가치를 본다"),
    ("일정 관리", "J", "P", "계획대로 진행한다", "상황에 따라 유연히 바꾼다"),
    ("아이디어 실행", "J", "P", "완성 계획을 먼저 세운다", "만들며 배우고 수정한다"),
    ("문제 해결", "T", "F", "원인 분석과 근거를 찾는다", "이해관계자 감정을 고려한다"),
    ("학습 선호", "S", "N", "절차와 예시로 배우기", "개념과 사례로 배우기"),
    ("소통 방식", "E", "I", "브레인스토밍/회의 선호", "문서/사고 정리 선호"),
]


def run_quiz() -> str:
    st.markdown("##### 8문항 빠른 진단")
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for idx, (q, a, b, at, bt) in enumerate(QUIZ, start=1):
        st.markdown(f"**Q{idx}. {q}**")
        choice = st.radio(" ", [at, bt], horizontal=True, key=f"q{idx}")
        if choice == at:
            scores[a] += 1
        else:
            scores[b] += 1
    mbti = ("E" if scores["E"] >= scores["I"] else "I") \
         + ("S" if scores["S"] >= scores["N"] else "N") \
         + ("T" if scores["T"] >= scores["F"] else "F") \
         + ("J" if scores["J"] >= scores["P"] else "P")
    return mbti


# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("MBTI 추천 웹앱")
mode = st.sidebar.radio("모드 선택", ["MBTI 선택", "빠른 진단", "대시보드"], index=0)

# ----------------------------
# Header
# ----------------------------
st.title("MBTI 기반 맞춤형 교육과정 추천")
st.caption("당신의 성향에 맞춘 실전형 커리큘럼을 찾아보세요.")

# ----------------------------
# Modes
# ----------------------------
if mode == "MBTI 선택":
    col1, col2 = st.columns([2, 1])
    with col1:
        mbti = st.selectbox("당신의 MBTI를 선택하세요", ALL_TYPES, index=ALL_TYPES.index("ENFP"))
        st.info(MBTI_DESCRIPTIONS[mbti])
        render_result(mbti, CATALOG)
    with col2:
        st.markdown("#### 직접 입력")
        manual = st.text_input("또는 직접 입력(예: INTP)")
        valid = validate_mbti(manual)
        if manual and not valid:
            st.warning("형식이 올바르지 않습니다. 예: ENFP, ISTJ …")
        if valid:
            st.success(f"인식된 유형: {valid}")
            render_result(valid, CATALOG)

elif mode == "빠른 진단":
    mbti = run_quiz()
    st.success(f"예상 MBTI: **{mbti}**")
    st.caption("*간단 진단 결과로, 정식 검사와 다를 수 있습니다.*")
    render_result(mbti, CATALOG)

else:  # 대시보드
    st.subheader("교육과정 카탈로그 개요")
    df = pd.DataFrame([{
        "ID": c.id,
        "제목": c.title,
        "난이도": c.difficulty,
        "시간(h)": c.duration_hours,
        "방식": c.delivery,
        "태그": ", ".join(c.tags),
        "링크": c.link
    } for c in CATALOG])

    c1, c2, c3 = st.columns(3)
    c1.metric("총 과정 수", len(CATALOG))
    c2.metric("평균 소요 시간", f"{int(df['시간(h)'].mean())}h")
    c3.metric("온라인 비율", f"{int((df['방식']=='Online').mean()*100)}%")

    st.dataframe(df, use_container_width=True, hide_index=True)

    st.download_button(
        "전체 카탈로그 CSV",
        data=df.to_csv(index=False).encode("utf-8-sig"),
        file_name="catalog.csv",
        mime="text/csv",
        use_container_width=True,
    )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption(
    "© 2025 MBTI Curriculum Recommender • 예시 링크는 대체 URL입니다. 실제 과정 링크로 교체하세요."
)

