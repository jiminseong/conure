import streamlit as st
from PIL import Image
import re
import os
from openai import OpenAI
import folium
from streamlit_folium import st_folium
import third_second_trauma
    
# 세션 상태 초기화
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'third_trauma'
# 세션 상태 초기화
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
if 'page_history' not in st.session_state:
    st.session_state.page_history = []

image_files = []

st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');
    
            .main-title {
                font-family: 'Permanent Marker', cursive;
                font-size: 3em;
                color: #FF69B4;
                text-align: center;
                padding: 20px;
                background-color: #FFF0F5;
                border-radius: 15px;
            }
            </style>
            """, unsafe_allow_html=True)
# # # 제목 설정
# st.title('응급실 First Aid')
st.markdown('<div class="main-title">응급실 First Aid</div>', unsafe_allow_html=True)
def display_page3():
    # 로고 표시
    with open("../assets/logo.svg", "r") as f:
        svg_content = f.read()
    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>',
        unsafe_allow_html=True
    )
    
    st.write("세번째 페이지")

    # 파일 업로드 위젯
    st.markdown('<div class="description">', unsafe_allow_html=True)
    st.write("외상으로 생긴 상처 부위 사진 파일을 업로드하세요 (최대 4장까지)")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("상처 부위가 잘보이는 사진을 사용 시 더 빠르게 정확한 응급처치 방법을 볼 수 있습니다.")
    uploaded_files = st.file_uploader("'Browse files'를 눌러 사진 업로드", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="1")
    
    if uploaded_files:
        if len(uploaded_files) > 4:
            st.error("최대 4개의 파일만 업로드할 수 있습니다.")
            for uploaded_file in enumerate(uploaded_files[0:4]):
                file_size_kb = round(uploaded_file.size / 1000, 1)
                # 파일명과 파일 크기 출력
                st.write("파일 크기:", file_size_kb, "KB")
                # 이미지 표시
                image = Image.open(uploaded_file)
                st.image(image, caption='업로드한 사진', use_column_width=True)
        else:
            for idx, uploaded_file in enumerate(uploaded_files):
                file_size_kb = round(uploaded_file.size / 1000, 1)
                # 파일명과 파일 크기 출력
                st.write("파일 크기:", file_size_kb, "KB")
                # 이미지 표시
                image = Image.open(uploaded_file)
                st.image(image, caption=f'업로드한 사진 {idx + 1}', use_column_width=True)
                image_files.append(image)
        
        if st.button("응급닥터에게 물어보기"):
            st.session_state.page_history.append(st.session_state.current_page)
            st.session_state.current_page = 'third_second_trauma'
            st.experimental_rerun()
        
def go_back():
    if st.session_state.page_history:
        st.session_state.current_page = st.session_state.page_history.pop()
        st.experimental_rerun()

# 페이지 표시 함수 호출
if st.session_state.current_page == 'third_trauma':
    display_page3()
if st.session_state.current_page == 'third_second_trauma':
    if st.button("뒤로 가기"):
        go_back()
    third_second_trauma.display_result(image_files)
