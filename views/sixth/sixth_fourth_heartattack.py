import streamlit as st

def display_page6_4():
    with open("assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    _,center,_ = st.columns([1,2,1])
    with center:
        st.write("의식을 확인해주세요 - 말을 걸어보고, 손을 대보고, 어깨를 흔들어 의식을 확인해주세요.")
        _,center,_ = st.columns([1,2,1])
        with center:
            if st.button("의식이 없습니다!"):
                st.session_state.step = 6.5
                st.rerun()
        with center:
            if st.button("의식이 있어요!"):
                st.session_state.step = 6.
                st.rerun()

    st.markdown(
    """
    <style>
    st-emotion-cache-98upzg.e1nzilvr4{
        color : red;
    }
    .st-emotion-cache-98upzg {
        color : red;
    }
    .st-emotion-cache-uwy95n{
        width : 100%;
    }
    .st-emotion-cache-7ym5gk{
        width : 100%;
    }
    </style>
    """,
        unsafe_allow_html=True
    )


    
    
    
