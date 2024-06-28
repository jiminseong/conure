import streamlit as st

def display_page6_2():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()
    
    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    
    
    _,center,_ = st.columns([1,2,1])
    with center:
        if st.button('심폐소생술 따라하기'):
            st.session_state.step = 6.4
            st.rerun()
            
    st.markdown(
    """
    <style>

    .st-emotion-cache-7ym5gk{
        width : 100%;
    }
    </style>
    """,
        unsafe_allow_html=True
    )
