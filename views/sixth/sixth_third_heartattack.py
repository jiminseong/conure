import streamlit as st
import requests
import folium
from folium.plugins import MiniMap
import numpy as np
import pandas as pd
import collections

map_api_key = st.secrets['MAP_API_KEY']

# 카카오 API 호출 함수
def whole_region(keyword, start_x, start_y, end_x, end_y):
    page_num = 1
    all_data_list = []
    
    while True:
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
        params = {
            'query': keyword,
            'page': page_num,
            'rect': f'{start_x},{start_y},{end_x},{end_y}'
        }
        headers = {
            "Authorization": map_api_key,
        }
        
        resp = requests.get(url, params=params, headers=headers)
        search_count = resp.json()['meta']['total_count']
        
        if search_count > 45:
            dividing_x = (start_x + end_x) / 2
            dividing_y = (start_y + end_y) / 2
            
            all_data_list.extend(whole_region(keyword, start_x, start_y, dividing_x, dividing_y))
            all_data_list.extend(whole_region(keyword, dividing_x, start_y, end_x, dividing_y))
            all_data_list.extend(whole_region(keyword, start_x, dividing_y, dividing_x, end_y))
            all_data_list.extend(whole_region(keyword, dividing_x, dividing_y, end_x, end_y))
            
            return all_data_list
        
        else:
            if resp.json()['meta']['is_end']:
                all_data_list.extend(resp.json()['documents'])
                return all_data_list
            else:
                page_num += 1
                all_data_list.extend(resp.json()['documents'])

# 겹치는 데이터 처리 함수
def overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y):
    overlapped_result = []
    
    for i in range(1, num_x + 1):
        end_x = start_x + next_x
        initial_start_y = start_y
        
        for j in range(1, num_y + 1):
            end_y = initial_start_y + next_y
            each_result = whole_region(keyword, start_x, initial_start_y, end_x, end_y)
            overlapped_result.extend(each_result)
            initial_start_y = end_y
        
        start_x = end_x
    
    return overlapped_result

# 지도 생성 함수
def make_map(df):
    m = folium.Map(location=[33.4935, 126.6266], zoom_start=12)
    minimap = MiniMap()
    m.add_child(minimap)
    
    for i in range(len(df)):
        folium.Marker([float(df['Y'][i]), float(df['X'][i])],
        tooltip=df['stores'][i],
        popup=df['place_url'][i]).add_to(m)
    
    return m

# Streamlit 애플리케이션
def display_page6_3():
    st.title('카카오 API를 사용한 주변 공영주차장 검색 및 지도 표시')
    
    # 사용자 입력
    keyword = st.text_input('검색할 키워드를 입력하세요', '공영주차장')
    start_x = st.number_input('시작 X 좌표', value=126.45)
    start_y = st.number_input('시작 Y 좌표', value=33.47)
    next_x = st.number_input('증가 X 값', value=0.01)
    next_y = st.number_input('증가 Y 값', value=0.01)
    num_x = st.number_input('X 방향 분할 수', min_value=1, value=12)
    num_y = st.number_input('Y 방향 분할 수', min_value=1, value=6)
    
    # API 호출 및 데이터 처리
    overlapped_result = overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y)
    results = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in overlapped_result)))
    
    # 데이터 프레임 생성
    X = []
    Y = []
    stores = []
    road_address = []
    place_url = []
    ID = []
    
    for place in results:
        X.append(float(place['x']))
        Y.append(float(place['y']))
        stores.append(place['place_name'])
        road_address.append(place['road_address_name'])
        place_url.append(place['place_url'])
        ID.append(place['id'])
    
    ar = np.array([ID, stores, X, Y, road_address, place_url]).T
    df = pd.DataFrame(ar, columns=['ID', 'stores', 'X', 'Y', 'road_address', 'place_url'])
    
    # 결과 출력
    st.subheader(f'총 {len(df)}개의 검색 결과')
    st.write(df.head())
    
    # 지도 표시
    st.subheader('지도')
    map_result = make_map(df)
    folium_static(map_result)

