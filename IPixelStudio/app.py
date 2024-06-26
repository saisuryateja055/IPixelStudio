
import streamlit as st
from streamlit_option_menu import option_menu


from model import print_base64_image
st.set_page_config("IPixelStudio",page_icon='🖼️')

st.markdown("<h1 style='text-align: center; color: white; font-size: 60px;'>IPixelStudio</h1> <br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; color: white; font-size: 40px;'>Imaginations into Images...</h1>", unsafe_allow_html=True)
st.title("Text To Image")






with st.sidebar:
    st.markdown("<h1 style='text-align: left; color: white; font-size: 40px;'>IPixelStudio</h1> <br> <br>",
                unsafe_allow_html=True)
    st.title("Provide you EDEN.AI API key here...")
    api=st.text_input("Enter your API Key",value="")
    st.title("Provide you RESOLUTION here...")
    options = ["256X265", "512X512", "1024X1024"]

    choice = st.selectbox("Select one option:", options)
    st.write(f"You selected: {choice}")
    resol=choice


if api:
    user_prompt = st.chat_input("Enter your Imagination")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history=[]



    if user_prompt:
        resol='256X256'
        st.session_state.chat_history.append({'type': 'user', 'message': user_prompt})
        result_image = print_base64_image(user_prompt,resol,api)
        if result_image:
            st.session_state.chat_history.append({'type': 'bot', 'message': result_image})
            st.session_state.user_input = ""  # Reset input box after processing

    for chat in st.session_state.chat_history:
        if chat['type'] == 'user':

            with st.chat_message("human"):
                st.write(chat['message'])
        elif chat['type'] == 'bot':
            with st.chat_message("AI"):
                st.image(chat['message'], caption="Response")