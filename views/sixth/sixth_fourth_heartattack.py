import streamlit as st

def display_page6_4():
    with open("assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    # 안내 메시지 표시
    st.container()
    _,center,_ = st.columns([1,2,1])
    with center:
        st.write("의식을 확인해주세요 - 말을 걸어보고, 손을 대보고, 어깨를 흔들어 의식을 확인해주세요.")
        _,center,_ = st.columns([1,2,1])
        with center:
            if st.button("의식이 없습니다!"):
                st.session_state.step = 6.5
        with center:
            if st.button("의식이 있어요!"):
                st.session_state.step = 6.1

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


    # cpr_steps = [
        
    #     "자세를 교정해주세요 - 경추를 보호하며 환자가 하늘을 바라보도록 똑바로 눕혀주세요.",
    #     "기도를 유지해주세요 - 머리를 뒤로 기울이고 턱을 들어 올려주세요.",
    #     "호흡을 확인해주세요 - 눈으로 보고(가슴 상승 여부), 귀로 듣고(숨소리), 볼로 숨결을 느껴 호흡을 확인해주세요.(5~10초간)",
    #     "인공호흡을 해주세요 - 머리를 기울이고, 턱을 들어 올린 후 코를 막고, 환자 입으로 1초에 한 번씩 2회 호흡을 불어넣어주세요.",
    #     "소리에 맞게 심장 압박을 해주세요 - 양쪽 유두 사이를 양손으로 압박해주세요. 35cm 깊이로 수직으로 압박하며, 분당 80~100회 정도의 속도로 압박해주세요.\n 1인 소생술일 때는 매 15회 흉부압박에 연속 2회 구강 대 구강 인공호흡을 실시해주세요.\n 상황 발생 후 4분 이내에 소생술을 시행해야 효과적입니다."
    # ]
    
    
    
