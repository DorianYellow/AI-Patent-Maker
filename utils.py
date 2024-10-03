import streamlit as st


def initialize_session_state():
    """세션 상태 초기화"""
    if "response" not in st.session_state:
        st.session_state["response"] = ""
    if "generated" not in st.session_state:
        st.session_state["generated"] = False
    if "error" not in st.session_state:
        st.session_state["error"] = ""
    if "prompt" not in st.session_state:
        st.session_state["prompt"] = ""


def on_textarea_change():
    """입력란 변경 시 호출되는 콜백 함수"""
    prompt = st.session_state["prompt"]
    if len(prompt) > 0:
        if len(prompt) < 100:
            st.session_state["error"] = (
                f"100자 이상 입력해야 합니다 ({len(prompt)}자 입력중)"
            )
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
