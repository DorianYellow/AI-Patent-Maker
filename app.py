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
    with st.expander("예시 입력 1 : 물건 발명"):
        st.markdown(
            """
        본 발명의 일례로 제시된 액정 렌즈 패널은 복수의 렌즈 전극과 배향막, 실런트, 차광 패턴을 포함합니다. 이 패널은 렌즈 전극을 갖춘 제2 렌즈 기판과 그에 대응하는 제1 렌즈 기판으로 구성되어 있습니다. 또한, 두 기판 사이의 간격을 유지하기 위해 컬럼 스페이서가 사용되며, 차광 영역과 액티브 영역에 따라 각각 다른 크기의 컬럼 스페이서를 배치할 수 있습니다. 차광 패턴은 금속 또는 유기 물질로 구성되며, 이 패턴을 통해 기판 간의 간격을 일정하게 유지할 수 있습니다.
        """
        )

    with st.expander("예시 입력 2 : 방법 발명"):
        st.markdown(
            """
        본 발명의 일 실시예에 따른 과일 가공 방법은 과일을 진공상태로 유지하여 팽창시키는 과정을 포함한다. 먼저, 과일을 압력 탱크에 삽입한 후 진공상태로 90초 동안 유지하여 과일을 팽창시킨다. 이때 과일의 표면은 진공상태로 인해 외부로 당겨지며, 과일의 표면과 내부 사이에는 공간이 형성된다. 이후 압력 탱크에서 공기를 외부로 배출하면 과일은 원상태로 복귀하고, 이 과정에서 표면과 내부 사이에 공간이 계속 유지된다. 그 다음, 비타민, 콜라겐, 바닐라액 중 선택된 침투물질을 물이나 식용용매에 용해하여 탱크 내부에 스프레이로 분무한다. 이후 1.1 ∼ 5atm의 압축공기를 공급하여 25초 동안 가압하고, 50초 동안 유지하여 과일의 표면과 내부 사이로 침투물질이 침투되도록 한다. 다음으로 압력 탱크에 압축공기를 30초 동안 배출하는 감압 과정을 거친 후, 10초 동안 유지하여 안정화시킨다. 이 과정이 끝나면 다시 압력 탱크에 침투물질을 공급하고, 가압 및 감압하여 안정화시키는 과정을 반복하여 침투물질을 과일 조직 내부로 침투시키는 가공단계를 포함한다.
        """
        )

    # 예시 설명 문구 (글머리 기호 및 글자 크기 조정)
    st.markdown(
        """
    <ul class='instruction-list'>
        <li>발명의 구성요소를 중심으로 서술해 주세요.</li>
        <li>구성요소들 사이의 논리적 연결관계를 기술적 특징과 함께 작성하시면 됩니다.</li>
        <li>100자 이상 입력하신 뒤 <kbd>Ctrl</kbd> + <kbd>Enter</kbd>를 입력해주세요.</li>
        <li>상세하게 설명할수록 더 좋은 퀄리티의 결과물이 생성됩니다.</li>
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
