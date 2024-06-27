import os

import streamlit as st
from openai import OpenAI

OpenAI.api_key = st.secrets["API_KEY"]


def request_chat_completion(
    prompt, system_role="복통 환자를 진료하는 간호사", model="gpt-4o", stream=True
):
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt},
    ]
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages, stream=stream
    )
    return chat_completion


def print_streaming_response(response):
    message = ""
    placeholder = st.empty()
    for chunck in response:
        delta = chunck.choices[0]["delta"]
        if "content" in delta:
            message += delta["content"]
            placeholder.markdown(message + " ▌")
        else:
            break
    placeholder.markdown(message)
    return message
