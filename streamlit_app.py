import streamlit as st

# 페이지 설정
st.set_page_config(page_title="교수의 포트폴리오", page_icon="👨‍🏫", layout="wide")

# 사이드바
with st.sidebar:
    st.header("👨‍🏫 김희정")
    st.image("https://via.placeholder.com/150", caption="프로필 사진")
    st.write("**연락처:**")
    st.write("📧 heejeongkim@korea.ac.kr")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("🐙 [GitHub](https://github.com)")

# 메인 콘텐츠
st.title("🚀 김희정 교수의 개발자 & 연구자 포트폴리오")

# 소개 섹션
col1, col2 = st.columns([2, 1])
with col1:
    st.header("📖 소개")
    st.write("""
    안녕하세요! 저는 열정적인 개발자이자 수학교육 연구자입니다.

코드와 데이터, 수학교육이론의 발전을 통해 세상을 더 나아지게 만드는 것을 좋아합니다.
    """)
with col2:
    st.metric("경력", "11년")
    st.metric("현재 진행 프로젝트", "4개")
    st.metric("SSCI 논문", "10편 이상")

# 수학교육 연구 내용
st.header("🔬 수학교육 연구 내용")
st.write("**주요 연구 분야:**")
st.markdown("- 수학 교육 방법론 및 커리큘럼 개발")
st.markdown("- AI와 머신러닝을 활용한 학습 분석")
st.markdown("- 데이터 기반 교육 평가 및 피드백 시스템")
st.markdown("- 디지털 도구를 활용한 수학 학습 환경 구축")

with st.expander("연구 성과 및 논문"):
    st.write("SSCI 저널에 발표된 주요 논문:")
    st.markdown("- 논문 제목 1 (저자, 연도)")
    st.markdown("- 논문 제목 2 (저자, 연도)")
    st.write("현재 진행 중인 연구 프로젝트: 4개")

# 프로젝트
st.header("💼 주요 프로젝트")
with st.expander("프로젝트 1: AI 기반 데이터 분석 도구"):
    st.write("설명: 이 프로젝트는...")
    st.code("print('Hello, World!')", language="python")

with st.expander("프로젝트 2: 웹 애플리케이션 개발"):
    st.write("설명: 이 프로젝트는...")
    st.code("console.log('Hello, World!');", language="javascript")

# 연구 관심사
st.header("🔬 연구 관심사")
st.write("""
- 인공지능과 머신러닝
- 데이터 사이언스
- 소프트웨어 엔지니어링
""")

# 취미
st.header("🎨 취미")
st.write("읽기, 코딩, 여행")

# 푸터
st.markdown("---")
st.write("© 2026 교수. All rights reserved.")
