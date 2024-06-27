import streamlit as st


def display_page1():

    
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    col1,col2,col3 = st.columns([1,1,1])
    with col2:
        if st.button('응급진료 시작하기'):
            st.session_state.step = 2
            st.rerun()
        if st.button('오늘의 의료 지식 배우기'):
            st.session_state.step = 7
            st.rerun()
st.markdown(
"""
<style>

.st-emotion-cache-uwy95n{
    width : 100%;
}
</style>
""",
    unsafe_allow_html=True
)
