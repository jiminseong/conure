import streamlit as st

def display_page6_8():

    with open("././assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    _,center,_ = st.columns([1,2,1])
    with center:
        st.write( "인공호흡을 해주세요 - 머리를 기울이고, 턱을 들어 올린 후 코를 막고, 환자 입으로 1초에 한 번씩 2회 호흡을 불어넣어주세요.")
        _,center,_ = st.columns([1,2,1])
        with center:
            if st.button("진행했습니다."):
                st.session_state.step = 6.9
                st.rerun()


    st.markdown(
    """
    <style>
    .st-emotion-cache-98upzg {
        color : red;
    }
    .st-emotion-cache-7ym5gk{
        width : 100%;
    }
    </style>
    """,
        unsafe_allow_html=True
    )