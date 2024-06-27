import streamlit as st
import random

def display_page7():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()
    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom: 5%; text-align: center;">{svg_content}</div>',
        unsafe_allow_html=True
    )

    _,_,right = st.columns([5,5,3])
    with right:
        if st.button('홈으로 가기'):
            st.session_state.step = 1
            st.rerun()
    # 유튜브 영상 URL 리스트
    video_urls = [
        "https://www.youtube.com/embed/bpjtsREKQ1A?si=BWPtQnCxVgJLoFLR",
        "https://www.youtube.com/embed/L76QgcTSM1s?si=cnHohPGiZowlOUao",
        "https://www.youtube.com/embed/DZGchjXa0nM?si=Fjufvn2f1SHA6WPj",
        "https://www.youtube.com/embed/_ppLC_oRcX0?si=TvG-RYC41bblLGgm",
        "https://www.youtube.com/embed/fjGGfrhnqEU?si=DVvKxs-6FzD-ahAG",
        "https://www.youtube.com/embed/pJINJgi1cyc?si=aMw04nIV6wllQQ7U",
        "https://www.youtube.com/embed/taweXe969zo?si=mQezwYfPKgnt36LC",
        "https://www.youtube.com/embed/dGGbMC6CnPk?si=2ug88ivKtRgEEMP-",
        "https://www.youtube.com/embed/1sOIzPl9hY8?si=xZ44MFIbzieEGzAF",
        "https://www.youtube.com/embed/bJvbAgKsoaw?si=hDncUQnH1xjM1QPa",
        "https://www.youtube.com/embed/jWaQNfVyS6M?si=Tn3ft-wtGo927RKn",
        "https://www.youtube.com/embed/USYtjzxqQ2E?si=ob74vl8uP8PbniiJ",
        "https://www.youtube.com/embed/M_5dBA7w8q0?si=rH9MOnpFwfXHXlRm",
        "https://www.youtube.com/embed/Kw60TCaPtYg?si=z1MXN7ZtqiOgZf7t",
        "https://www.youtube.com/embed/_l5NZ46Dz9Q?si=cO9z1kBSmmtpGfab",
        "https://www.youtube.com/embed/KaCzqKKvEmc?si=5YX66cpJ0GKKcUhg",
        "https://www.youtube.com/embed/giH5GP9ZLao?si=CzLok1HbxQm-mtzh",
    ]

    # 랜덤으로 두 개의 영상 선택
    random_videos = random.sample(video_urls, 2)

    # HTML을 사용하여 subheader를 가운데 정렬
    st.markdown(
        f'<h3 style="text-align: center;">오늘의 첫번째 의료정보</h3>',
        unsafe_allow_html=True
    )
    # 첫번째 영상을 iframe으로 임베드하고 가운데 정렬
    st.markdown(
        f'<div style="display: flex; justify-content: center; margin-bottom: 20px;">'
        f'<iframe width="560" height="315" src="{random_videos[0]}" frameborder="0" allowfullscreen></iframe>'
        f'</div>',
        unsafe_allow_html=True
    )
    
    # HTML을 사용하여 subheader를 가운데 정렬
    st.markdown(
        f'<h3 style="text-align: center;">오늘의 두번째 의료정보</h3>',
        unsafe_allow_html=True
    )
    # 두번째 영상을 iframe으로 임베드하고 가운데 정렬
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<iframe width="560" height="315" src="{random_videos[1]}" frameborder="0" allowfullscreen></iframe>'
        f'</div>',
        unsafe_allow_html=True
    )


