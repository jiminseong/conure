import streamlit as st

from utils.session_state import initialize_session_state
from utils.styles import apply_styles
from views.fifth_toothdamage import display_page5
from views.first_home import display_page1
from views.fourth_colic import display_page4
from views.second_select import display_page2
from views.sixth_heartattack import display_page6
from views.third_trauma import display_page3

# 세션 상태 초기화
initialize_session_state()

# 전역 스타일 설정
apply_styles()

# 각페이지 렌더링하는 step
if st.session_state.step == 1:
    display_page1()

elif st.session_state.step == 2:
    display_page2()
elif st.session_state.step == 3:
    display_page3()

elif st.session_state.step == 4:
    display_page4()

elif st.session_state.step == 5:
    display_page5()

elif st.session_state.step == 6:
    display_page6()
