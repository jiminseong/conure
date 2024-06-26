import streamlit as st
from utils.session_state import initialize_session_state
from utils.styles import apply_styles
from views.first_home import display_page1
from views.second_select import display_page2
from views.third_trauma import display_page3
from views.fourth_colic import display_page4
from views.fifth_toothdamage import display_page5
from views.sixth.sixth_heartattack import display_page6
from views.sixth.sixth_second_heartattack import display_page6_2
from views.sixth.sixth_third_heartattack import display_page6_3
from views.sixth.sixth_fourth_heartattack import display_page6_4
from views.sixth.cpr.sixth_fifth_heartattack import display_page6_5
from views.sixth.cpr.sixth_sixth_heartattack import display_page6_6
from views.sixth.cpr.sixth_seventh_heartattack import display_page6_7
from views.sixth.cpr.sixth_eighth_heartattack import display_page6_8
from views.sixth.cpr.sixth_nineth_heartattack import display_page6_9
from views.fifth_second_toothdamage import display_page5_2

# 세션 상태 초기화
initialize_session_state()

# 전역 스타일 설정
apply_styles()

# 각 페이지 렌더링하는 step
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
elif st.session_state.step == 52:
    display_page5_2()
elif st.session_state.step == 6:
    display_page6()
    
elif st.session_state.step == 6.2:
    display_page6_2()

elif st.session_state.step == 6.3:
    display_page6_3()
    
elif st.session_state.step == 6.4:
    display_page6_4()

elif st.session_state.step == 6.5:
    display_page6_5()

elif st.session_state.step == 6.6:
    display_page6_6()

elif st.session_state.step == 6.7:
    display_page6_7()

elif st.session_state.step == 6.8:
    display_page6_8()

elif st.session_state.step == 6.9:
    display_page6_9()

