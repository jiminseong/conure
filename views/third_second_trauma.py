import streamlit as st
from PIL import Image
import re
import os
from openai import OpenAI
import folium
from streamlit_folium import st_folium
import third_trauma

# os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'third_trauma'

if 'doctor_consulted' not in st.session_state:
    st.session_state.doctor_consulted = False
# 세션 상태 초기화
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

st.markdown("""
            <style>
            .map{
                width: 700px;
                height: 500px;
                margin: auto;
            }
            </style>
            """, unsafe_allow_html=True)

def summary_prompting(image_files):
    # # 실제 OpenAI API를 사용 시 아래 주석을 해제
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": f"{image}",
    #         },
    #         {
    #             "role": "system",
    #             "content": """
    #                 입력된 데이터는 사용자의 현재 외상을 입은 상태를 보여주는 사진이야.
    #                 사용자는 지금 다급하게 이 외상을 치료해야해.
    #                 어떤 외상을 입은 것인지, 어떻게 치료해야 하는지 알려줘야해.
    #                 사용자는 아파서 당황하고 긴급할테니, 사용자가 한눈에 알아보게 깔끔하게 대답해줘
    #                 """,
    #         }
    #     ],
    #     model="gpt-4o",
    # )
    result = '''
    사진에 보이는 상처는 긁힌 자국처럼 보입니다. 이런 종류의 상처를 치료하려면 다음과 같은 단계를 따르세요:

    상처 세척: 깨끗한 물과 비누로 상처 부위를 세척하여 오염물을 제거합니다.
    소독: 소독제를 사용하여 상처를 소독합니다. 과산화수소나 알코올 등을 사용할 수 있습니다.
    상처 보호: 상처 부위를 건조시키고, 상처용 연고(항생제 포함)를 바른 후, 깨끗한 붕대나 반창고로 보호합니다.
    관찰: 상처가 덧나지 않도록 하루에 한두 번씩 상태를 확인하고, 붕대를 교체합니다.
    만약 상처 부위가 붉어지거나, 부어오르거나, 고름이 나오는 등의 감염 증상이 나타난다면, 즉시 의사의 진료를 받으세요.
    '''
    # result = chat_completion.choices[0].message.content
    return result


def display_result(image_files):
    # 로고 표시
    with open("../assets/logo.svg", "r") as f:
        svg_content = f.read()
    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>',
        unsafe_allow_html=True
    )
    
    st.write("세번째의 두번째 페이지")
    
    with st.spinner("빠르게 치료 방법 찾는중..."):
        result = summary_prompting(image_files)
        st.write(result)
        st.session_state.doctor_consulted = True
    
    # if st.button('주변 가까운 약국 보기'):
    #         st.session_state.button_clicked = True

    # 버튼이 클릭된 경우 지도 표시
    if st.button('주변 가까운 약국 보기'):
        st.session_state.button_clicked = not st.session_state.button_clicked
    
    if st.session_state.button_clicked:
        # 가천대학교 역의 위도와 경도
        latitude = 37.448278
        longitude = 127.127978

        # Folium 지도 생성
        map = folium.Map(location=[latitude, longitude], zoom_start=17)

        # 약국 위치 예제 (위도, 경도, 이름)
        pharmacies = [
            {"name": "약국 A", "lat": 37.450000, "lon": 127.127500},
            {"name": "약국 B", "lat": 37.449000, "lon": 127.128000},
            {"name": "약국 C", "lat": 37.448500, "lon": 127.129000},
        ]

        # 약국 위치를 지도에 마커로 추가
        for pharmacy in pharmacies:
            folium.Marker(
                location=[pharmacy["lat"], pharmacy["lon"]],
                popup=pharmacy["name"],
                icon=folium.Icon(icon="cloud"),
            ).add_to(map)
            
        # 가천대학교 역에 학교 모양 빨간색 마커 추가
        school_icon = folium.Icon(color='red', icon='info-sign')  # 학교 모양 아이콘 지정
        folium.Marker(
            location=[37.448278, 127.127978],
            popup="가천대학교 역",
            icon=school_icon
        ).add_to(map)

        # 지도 표시
        st.markdown("<div class='map'>", unsafe_allow_html=True)
        st_folium(map, width=700, height=500)
        st.markdown("</div>", unsafe_allow_html=True)