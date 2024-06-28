import streamlit as st
import folium
from streamlit_folium import st_folium


def display_page3_3():
    
    # 로고 표시
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()
        
    st.markdown(
        f'<div style="display: flex; justify-content: center; margin-bottom: 5%;" align="center">{svg_content}</div>', 
        unsafe_allow_html=True
    )
    
    if st.button('홈으로 돌아가기'):
        st.session_state.step = 1
        
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
    

    
st.markdown("""
            <style>
            .map{
                width: 700px;
                height: 500px;
                margin: auto;
            }
            </style>
    """, unsafe_allow_html=True)