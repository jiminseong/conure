import streamlit as st
import base64
from scipy.io.wavfile import write
import numpy as np
import os

#비프음 파일 생성
def create_beep_wav():
    sample_rate = 44100  # 샘플링 주파수
    duration = 0.5  # 비프음 길이
    frequency = 1000  # 비프음 주파수

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    write("beep.mp3", sample_rate, wave.astype(np.float32))

create_beep_wav()

def display_page6_9():
    # SVG 로고 표시
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    _, center, _ = st.columns([1, 2, 1])
    with center:

        st.write("소리에 맞게 심장 압박을 해주세요 - 양쪽 유두 사이를 양손으로 압박해주세요.")
        st.write("35cm 깊이로 수직으로 압박하며, 소리에 따라 분당 100회 정도의 속도로 압박해주세요.")
        st.write("1인 소생술일 때는 매 15회 흉부압박에 연속 2회 구강 대 구강 인공호흡을 실시해주세요")
        st.write("상황 발생 후 4분 이내에 소생술을 시행해야 효과적입니다.")
        
        _, center, _ = st.columns([1, 2, 1])
        with center:
            if st.button("진행했습니다."):
                st.session_state.step = 2
                st.rerun()

            # 비프음 재생
            beep_file_path = "././assets/beep.mp3"
            if os.path.exists(beep_file_path):
                audio_file = open(beep_file_path, "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3", autoplay=True, loop=True)
            else:
                st.error("비프음 파일을 찾을 수 없습니다.")

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


