import os
from datetime import date
import streamlit as st
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]
OpenAI.api_key = st.secrets["API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
    
def request_chat_completion(data):
    # open api 사용 시 주석 풀기
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": f"{data}",
    #         },
    #         {
    #             "role": "system",
    #             "content": """
    #                 복통 환자를 진료하는 간호사
    #                 """,
    #         }
    #     ],
    #     model="gpt-4o",
    # )
    # result = chat_completion.choices[0].message.content
    result = "예시용 문자 데이터"
    return result

# def request_chat_completion(
#     prompt, system_role="복통 환자를 진료하는 간호사", model="gpt-4o", stream=True
# ):
#     messages = [
#         {"role": "system", "content": system_role},
#         {"role": "user", "content": prompt},
#     ]

#     chat_completion = client.chat.completions.create(
#         model=model, messages=messages, stream=stream
#     )
    
#     # result = chat_completion.choices[0].message.content
#     result = "예시용문자"
#     return result

# def print_streaming_response(response):
#     message = ""
#     for chunk in response:
#         delta = chunk.choices[0]["delta"]
#         if "content" in delta:
#             message += delta["content"]
#         else:
#             break
#     return message

def display_page4():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )

    gender_type = {"남자", "여자"}
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
    prompt_template = """
            환자의 이름은 {Name}
            배의 {symptom_location}쪽이 아픕니다.
            먹은 음식은 {food} 입니다.
            이 경우에 복통을 완화하는 방법을 알려주세요.
            먹으면 좋은 음식과 약을 추천해주세요
            ___
            키: {height}
            성별: {gender}
            몸무게: {weigh}
            생년월일: {birth}
            ___
            """.strip()

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
                "name": "",
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
                    label="이름", value=example_data["name"], placeholder="아무개"
                )
                height = st.number_input(
                    "키", 50.0, 231.0, value=float(example_data["height"]), placeholder=50
                )
            with col2:
                types = st.multiselect(
                    label="성별",
                    options=list(gender_type),
                    default=example_data["types"],
                    max_selections=1,
                )
                weight = st.number_input(
                    "몸무게",
                    1.0,
                    178.0,
                    placeholder="1",
                    value=float(example_data["weight"]),
                )
            born = st.date_input("생년월일", value=example_data["born"])
            st.markdown("**의심되는 음식을 최대 3개 작성해주세요**")
            col1, col2, col3 = st.columns(3)
            with col1:
                food_1 = st.text_input(
                    label="음식1", label_visibility="collapsed", placeholder="음식 1"
                )
            with col2:
                food_2 = st.text_input(
                    label="음식2", label_visibility="collapsed", placeholder="음식 2"
                )
            with col3:
                food_3 = st.text_input(
                    label="음식3", label_visibility="collapsed", placeholder="음식 3"
                )
            symptom = st.selectbox(
                "어느 부위가 아픈가요?",
                ("", "우상", "좌상", "우하", "좌하", "복부 전체", "옆구리", "배꼽 주위"),
            )
            duration = st.number_input("기간(일수)", 0, 30)
            submit = st.form_submit_button(label="진단시작")
            if submit:
                if not food_1 or food_2 or food_3:
                    st.error("먹은 음식은 말해주세요")
                elif len(types) == 0:
                    st.error("성별을 선택해주세요.")
                elif len(symptom) == 0:
                    st.error("부위를 선택해주세요.")
                else:
                    food_list = [food_1, food_2, food_3]
                    food_list = [x for x in food_list if x]
                    prompt_template.format(
                        Name=name,
                        height=height,
                        gender=types,
                        weigh=weight,
                        birth=born,
                        food=food_list,
                        symptom_location=symptom,
                    )
    
                    with st.spinner("진단 중입니다."):
                        response = request_chat_completion(prompt_template)
                        st.session_state.colic_result = response
                        st.session_state.step = 4.2
                        st.rerun
                        

                    

