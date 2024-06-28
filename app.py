
import streamlit as st

from utils.session_state import initialize_session_state
from utils.styles import apply_styles
from views.fifth_toothdamage import display_page5
from views.first_home import display_page1
from views.zero_medicalinfo import display_page0
from views.fourth_colic import display_page4
from views.second_select import display_page2

from views.third.third_trauma import display_page3
from views.third.third_second_trauma import display_page3_2
from views.third.third_third_trauma import display_page3_3

from views.fourth_colic import display_page4
from views.fourth_second_colic import display_page4_2

from views.fifth_toothdamage import display_page5
from views.fifth_second_toothdamage import display_page5_2

from views.sixth.sixth_heartattack import display_page6
from views.sixth.sixth_second_heartattack import display_page6_2
from views.sixth.sixth_third_heartattack import display_page6_3
from views.sixth.sixth_fourth_heartattack import display_page6_4
from views.sixth.cpr.sixth_fifth_heartattack import display_page6_5
from views.sixth.cpr.sixth_sixth_heartattack import display_page6_6
from views.sixth.cpr.sixth_seventh_heartattack import display_page6_7
from views.sixth.cpr.sixth_eighth_heartattack import display_page6_8
from views.sixth.cpr.sixth_nineth_heartattack import display_page6_9
from views.sixth.cpr.sixth_tenth_heartattack import display_page6_10

from views.seventh.seventh_fracture import display_page7
from views.seventh.seventh_second_fracture import display_page7_2
from views.seventh.seventh_third_fracture import display_page7_3
from views.seventh.seventh_forth_fracture import display_page7_4
from views.seventh.seventh_fifth_fracture import display_page7_5
from views.seventh.seventh_sixth_fracture import display_page7_6
from views.seventh.seventh_seventh_fracture import display_page7_7
from views.seventh.seventh_eighth_fracture import display_page7_8
from views.seventh.seventh_ninth_fracture import display_page7_9
from views.seventh.seventh_tenth_fracture import display_page7_10
from views.seventh.seventh_eleventh_fracture import display_page7_11
from views.seventh.seventh_twelveth_fracture import display_page7_12

from views.eighth.eighth_heat import display_page8
from views.eighth.eighth_second_heat import display_page8_2




# 세션 상태 초기화
initialize_session_state()

# 전역 스타일 설정
apply_styles()

# 각페이지 렌더링하는 step
if st.session_state.step == 0:
    display_page0()
    
if st.session_state.step == 1:
    display_page1()

elif st.session_state.step == 2:
    display_page2()

elif st.session_state.step == 3: 
    display_page3()
    
elif st.session_state.step == 3.2:
    display_page3_2()
    

elif st.session_state.step == 3.3:
    display_page3_3()

elif st.session_state.step == 4:
    display_page4()
    
elif st.session_state.step == 4.2:
    display_page4_2()
    
elif st.session_state.step == 5:
    display_page5()

elif st.session_state.step==52:
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

elif st.session_state.step == 6.10:
    display_page6_10()
    
elif st.session_state.step==7:
    display_page7()

elif st.session_state.step==7.2:
    display_page7_2()

elif st.session_state.step==7.3:
    display_page7_3()

elif st.session_state.step==7.4:
    display_page7_4()

elif st.session_state.step==7.5:
    display_page7_5()

elif st.session_state.step==7.6:
    display_page7_6()

elif st.session_state.step==7.7:
    display_page7_7()

elif st.session_state.step==7.8:
    display_page7_8()

elif st.session_state.step==7.9:
    display_page7_9()

elif st.session_state.step==7.10:
    display_page7_10()

elif st.session_state.step==7.11:
    display_page7_11()

elif st.session_state.step==7.12:
    display_page7_12()


elif st.session_state.step == 8:
    display_page8()
    
elif st.session_state.step == 8.2:
    display_page8_2()