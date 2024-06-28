import streamlit as st
import time

def display_page6_7():
    with open("././assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
       f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.write("호흡을 확인해주세요 - 눈으로 보고(가슴 상승 여부), 귀로 듣고(숨소리), 볼로 숨결을 느껴 호흡을 확인해주세요.(5~10초간)")
        _,center,_ = st.columns([1,2,1])
        with center:
            if st.button("진행했습니다."):
                st.session_state.step = 6.8
                st.rerun()
        
            # 타이머 추가
            timer_placeholder = st.empty()
            for seconds in range(5, 0, -1):
                timer_placeholder.write(f"타이머: {seconds} 초 남음")
                time.sleep(1)

            # 타이머 종료 후 버튼 표시
            timer_placeholder.empty()
            st.write("타이머 종료!")
    

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

