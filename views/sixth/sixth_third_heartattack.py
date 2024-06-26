import streamlit as st
import requests
from urllib.parse import urlencode
import pandas as pd
import xml.etree.ElementTree as ET
from geopy.distance import geodesic
import re

aed_api_key = st.secrets['AED_API_KEY']

def clean_xml_string(xml_string):
    # 잘못된 XML 문자를 정리합니다.
    xml_string = re.sub(r'[^\x09\x0A\x0D\x20-\x7F]', '', xml_string)
    return xml_string

def display_page6_3():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )

    # 사용자 위치를 입력받기 위한 폼
    with st.form("location_form"):
        st.write("사용자 위치 정보를 입력하세요.")
        user_lat = st.text_input("위도:", key="user_lat")
        user_lon = st.text_input("경도:", key="user_lon")
        submitted = st.form_submit_button("제출")

    if submitted:
        if user_lat and user_lon:
            try:
                user_location = (float(user_lat), float(user_lon))

                # URL 설정
                base_url = "http://safemap.go.kr/openApiService/data/getAedData.do"

                # 파라미터 설정
                service_key = st.secrets['AED_API_KEY']
                page_no = 1
                num_of_rows = 1000

                # 전체 데이터를 저장할 리스트
                all_data = []

                while True:
                    params = {
                        "serviceKey": service_key,
                        "pageNo": str(page_no),
                        "numOfRows": str(num_of_rows),
                        "type": "xml"
                    }

                    encoded_params = urlencode(params)
                    final_url = f"{base_url}?{encoded_params}"

                    response = requests.get(final_url)

                    if response.status_code == 200:
                        try:
                            clean_response_text = clean_xml_string(response.text)
                            root = ET.fromstring(clean_response_text)
                            items = root.findall(".//item")
                            if not items:
                                break

                            for item in items:
                                entry = {child.tag: child.text for child in item}
                                if 'LAT' in entry and 'LON' in entry:
                                    item_location = (float(entry['LAT']), float(entry['LON']))
                                    distance = geodesic(user_location, item_location).meters
                                    if distance <= 500:
                                        all_data.append(entry)

                            page_no += 1
                        except ET.ParseError as e:
                            st.error(f"XML Parse Error: {e}")
                            st.error(f"Response Text: {clean_response_text}")
                            break
                    else:
                        st.error(f"Error: {response.status_code}")
                        break

                if all_data:
                    df = pd.DataFrame(all_data)
                    df_map = df[['LAT', 'LON']].rename(columns={'LAT': 'lat', 'LON': 'lon'}).astype(float)
                    st.map(df_map)
                    st.success("지도에 500m 반경 내의 AED 데이터를 성공적으로 표시했습니다.")
                else:
                    st.warning("500m 반경 내의 데이터를 찾을 수 없습니다.")
            except ValueError:
                st.error("유효한 위도와 경도를 입력하세요.")
        else:
            st.error("위도와 경도를 모두 입력하세요.")

