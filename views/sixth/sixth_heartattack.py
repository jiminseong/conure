import streamlit as st


def display_page6():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    col1,col2,col3 = st.columns([1,5,1])
    with col2:
        st.subheader("119에 신고하셨나요?")
        _,center,_ = st.columns([1,3,1])
        with center:
            
            if st.button('네 신고했습니다!'):
                st.session_state.step = 6.2
                st.rerun()
        

    st.markdown(
        """
        <style>
        h3{
            text-align: center;
        }
        .st-emotion-cache-asc41u{
            width : 100%;
        }
        .st-emotion-cache-uwy95n{
            width : 100%;
        }
        </style>
        """,
            unsafe_allow_html=True
        )
