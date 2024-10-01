import streamlit as st
import ollama

# CSS 스타일링 적용
st.markdown(
    """
    <style>
    /* Noto Sans KR 폰트 링크 추가 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

    .block-container {
        max-width: 70%;
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

# 서비스 제목과 부제목
st.markdown(
    "<h1><span style='color: blue;'>&nbsp;&nbsp;&nbsp;AI</span> Patent Maker!</h1>",
    unsafe_allow_html=True,
)
st.markdown("<p class='header-text'> </p>", unsafe_allow_html=True)


# Streamed response emulator
def response_generator(prompt):
    # 실제 응답 생성 로직을 여기에 추가
    response = ollama.generate(model="test_model3", prompt=prompt, stream=True)
    for chunk in response:
        if chunk["response"] == "\n":
            chunk["response"] = "\n\n"
        yield chunk["response"]


# 세션 상태 초기화
if "response" not in st.session_state:
    st.session_state["response"] = ""
if "generated" not in st.session_state:
    st.session_state["generated"] = False
if "error" not in st.session_state:
    st.session_state["error"] = ""
if "prompt" not in st.session_state:
    st.session_state["prompt"] = ""


# 입력 변경 시 호출되는 콜백 함수 정의
def on_textarea_change():
    prompt = st.session_state["prompt"]
    if len(prompt) > 0:
        if len(prompt) < 100:
            st.session_state["error"] = "100자 이상 입력해야 합니다"
            st.session_state["generated"] = False
            st.session_state["response"] = ""
        else:
            st.session_state["error"] = ""
            st.session_state["generated"] = True
            st.session_state["response"] = ""
    else:
        st.session_state["error"] = ""
        st.session_state["generated"] = False
        st.session_state["response"] = ""


# 입력과 출력을 위한 두 개의 컬럼 생성
col1, col2 = st.columns(2)

with col1:
    # 소제목
    st.markdown(
        "<h2 class='subheader'>당신의 발명에 대해 설명해주세요</h2>",
        unsafe_allow_html=True,
    )
    # 입력란 (레이블 제공 및 숨김)
    st.text_area(
        "발명 설명 입력란",  # 레이블 제공
        height=200,
        key="prompt",
        on_change=on_textarea_change,
        label_visibility="collapsed",  # 레이블 숨김
    )
    # 에러 메시지 위치 고정 (플레이스홀더 사용)
    error_placeholder = st.empty()
    # 에러 메시지 업데이트
    if st.session_state["error"]:
        error_placeholder.markdown(
            f"<p class='error-message'>{st.session_state['error']}</p>",
            unsafe_allow_html=True,
        )
    else:
        error_placeholder.markdown(
            "<p class='error-message'></p>", unsafe_allow_html=True
        )

    # 좌측 하단에 예시 입력을 담은 expander 버튼 추가
    with st.expander("예시 입력 보기"):
        st.markdown(
            """
        본 발명의 다이 본딩 방법은 다이를 기판에 부착하는 과정에서 다이렉트 본딩 또는 이단계 본딩 방식 중 하나를 선택할 수 있습니다. 다이를 어태치 필름에서 분리하고, 선택한 본딩 방식에 따라 기판에 부착합니다. 다이렉트 본딩 방식은 다이를 직접 기판에 부착하는 것이고, 이단계 본딩 방식은 다이를 임시로 다이 스테이지에 배치한 후, 다시 픽업하여 기판에 부착하는 방식입니다. 이 과정에서 다이의 위치를 추가로 측정할 수 있으며, 여러 본딩 헤드를 사용해 다양한 다이를 동시에 본딩할 수 있습니다. 이 방법을 통해 여러 종류의 다이를 효율적으로 처리할 수 있습니다.
        """
        )

    # 예시 설명 문구 (글머리 기호 및 글자 크기 조정)
    st.markdown(
        """
    <ul class='instruction-list'>
        <li>발명의 '과제 해결 수단'인 구성요소를 중심으로 설명해주세요</li>
        <li>100자 이상 입력하신 뒤 ctrl enter를 입력해주세요</li>
        <li>상세하게 설명할 수록 더 좋은 퀄리티의 결과물이 생성됩니다</li>
    </ul>
    """,
        unsafe_allow_html=True,
    )

with col2:
    # 소제목 플레이스홀더 생성
    header_placeholder = st.empty()
    if not st.session_state["generated"]:
        header_placeholder.markdown(
            "<h2 class='subheader'>특허문서 생성전</h2>", unsafe_allow_html=True
        )
        st.empty()
    else:
        header_placeholder.markdown(
            "<h2 class='subheader'>특허문서 생성중...</h2>", unsafe_allow_html=True
        )
        # 응답을 st.chat_message 스타일로 표시
        with st.chat_message("user"):
            full_response = ""
            message_placeholder = st.empty()
            for chunk in response_generator(st.session_state["prompt"]):
                # 응답 업데이트
                full_response += chunk
                message_placeholder.markdown(full_response)
            # 전체 응답 저장
            st.session_state["response"] = full_response
        # 생성 완료 후 헤더 업데이트
        header_placeholder.markdown(
            "<h2 class='subheader'>특허문서가 생성되었습니다</h2>",
            unsafe_allow_html=True,
        )
