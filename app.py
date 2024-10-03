import streamlit as st
from styles import apply_css
from utils import initialize_session_state, on_textarea_change
from response_generator import response_generator

# CSS 스타일링 적용
apply_css()

# 서비스 제목과 부제목
st.markdown(
    "<h1><span style='color: blue;'>AI</span> Patent Maker!</h1>",
    unsafe_allow_html=True,
)
st.markdown("<p class='header-text'> </p>", unsafe_allow_html=True)

# 세션 상태 초기화
initialize_session_state()

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
        # 응답을 표시
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
