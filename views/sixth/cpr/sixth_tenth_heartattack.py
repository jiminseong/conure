import streamlit as st


def display_page6_10():
    # SVG 로고 표시
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    _, center, _ = st.columns([1, 2, 1])
    with center:

        st.write("머리를 세게 부딪힌 적이 있는거서 같나요?")

        
        _, center, _ = st.columns([1, 2, 1])
        with center:
            if st.button("네 그런거 같습니다."):
                st.warning("뇌진탕일 수 있습니다. 근처 병원을 방문하세요")
                st.rerun()

        
    st.markdown(
        """
        <style>
        .st-emotion-cache-n6b53v>.p {
            color: red;
        }
        .st-emotion-cache-7ym5gk{
        width : 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
)


