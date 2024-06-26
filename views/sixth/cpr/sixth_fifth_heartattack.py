import streamlit as st

def display_page6_5():
    with open("././assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    _,center,_ = st.columns([1,2,1])
    with center:
        st.write("자세를 교정해주세요 - 경추를 보호하며 환자가 하늘을 바라보도록 똑바로 눕혀주세요.")
        _,center,_ = st.columns([1,2,1])
        with center:
            if st.button("진행했습니다."):
                st.session_state.step = 6.6
                st.rerun()


    st.markdown(
    """
    <style>
    .st-emotion-cache-98upzg {
        color : red;
    }
    .st-emotion-cache-uwy95n{
        width : 100%;
    }
    </style>
    """,
        unsafe_allow_html=True
    )