import streamlit as st


def apply_css():
    """CSS 스타일링 적용"""
    st.markdown(
        """
        <style>
        /* Noto Sans KR 폰트 링크 추가 */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

        .block-container {
            max-width: 66%;
            padding-top: 2rem;
            margin: auto;
        }
        h1 {
            text-align: center;
            margin-left: auto;
            margin-right: auto;
            font-size: 3rem;
        }
        h1 span {
            color: blue;
        }
        h2.subheader {
            text-align: center;
            font-size: 1.2rem;
            margin-bottom: 0.5rem;  /* 소제목과 입력란 사이 간격 조절 */
        }
        .header-text {
            text-align: center;
            font-size: 1.3rem;
            color: gray;
            margin-bottom: 4rem;
        }
        .error-message {
            color: red;
            font-size: 0.9rem;
            min-height: 1.2rem;  /* 에러 메시지 공간 확보 */
        }
        .instruction-list {
            font-size: 0.9rem;
            font-family: 'Noto Sans KR', sans-serif;  /* 전체 폰트 변경 */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
