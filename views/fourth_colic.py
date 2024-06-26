import os
from datetime import date

import streamlit as st
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def display_page4():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>',
        unsafe_allow_html=True,
    )

    st.write("네번째 페이지")


type_emoji_gender = {"남자": "🚹", "여자": "🚺"}
example_male = {
    "name": "홍길동",
    "height": "174",
    "types": ["남자"],
    "weight": "68",
    "born": date(1981, 8, 22),
}
example_female = {
    "name": "홍길순",
    "height": "162",
    "types": ["여자"],
    "weight": "52",
    "born": date(1980, 7, 28),
}
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    auto_complete_option = st.radio(
        "평균 데이터로 채우기", options=["선택 안 함", "남자", "여자"], index=0
    )

    if auto_complete_option == "남자":
        example_data = example_male
    elif auto_complete_option == "여자":
        example_data = example_female
    else:
        example_data = {
            "name": "아무개",
            "height": 50,
            "types": [],
            "weight": 1,
            "born": date.today(),
        }

    with st.form(key="form"):
        st.markdown("**개인 정보를 작성해주세요**")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(
                label="이름",
                value=example_data["name"],
            )
            height = st.number_input(
                "키", 50.0, 231.0, value=float(example_data["height"])
            )
        with col2:
            types = st.multiselect(
                label="성별",
                options=list(type_emoji_gender.keys()),
                default=example_data["types"],
                max_selections=1,
            )
            weight = st.number_input(
                "몸무게", 1.0, 178.0, value=float(example_data["weight"])
            )
        born = st.date_input("생년월일", value=example_data["born"])
        st.markdown("**의심되는 음식을 최대 3개 작성해주세요**")
        col1, col2, col3 = st.columns(3)
        with col1:
            food_1 = st.text_input(label="음식1")
        with col2:
            food_2 = st.text_input(label="음식2")
        with col3:
            food_3 = st.text_input(label="음식3")
        symptom = st.selectbox(
            "어느 부위가 아픈가요?",
            ("", "우상", "좌상", "우하", "좌하", "복부 전체", "옆구리", "배꼽 주위"),
        )
        duration = st.number_input("기간", 0, 30)
        submit = st.form_submit_button(label="진단시작")
        if submit:
            if not food_1 or food_2 or food_3:
                st.error("먹은 음식은 말해주세요")
            elif len(types) == 0:
                st.error("성별을 선택해주세요.")
            elif len(symptom) == 0:
                st.error("부위를 선택해주세요.")
            else:
                st.success("진단을 시작하겠습니다")
