import streamlit as st

from chat_engine import ChatEngine


def chatbot_response(user_input):
    return st.session_state.chat_engine.chat(user_input)


def update_chat_history(user_input, response):
    st.session_state.chat_history.append(f"You: {user_input}")
    st.session_state.chat_history.append(f"Cinematch: {response.response}")

    if response.sources:
        st.session_state.question_context = response.sources[0].content


if __name__ == "__main__":
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if 'chat_engine' not in st.session_state:
        st.session_state.chat_engine = ChatEngine()

    if 'question_context' not in st.session_state:
        st.session_state.question_context = 'test'

    st.title("Cinematch - Your Guide to the Perfect Movie Match!")
    st.write("Chat History:")
    for message in st.session_state.chat_history:
        st.write(message)

    user_input = st.text_input("You: ", "")

    if st.button("Send") and user_input:
        response = chatbot_response(user_input)
        update_chat_history(user_input, response)

        st.rerun()

    st.write("Question Context used:")
    st.write(st.session_state.question_context)
