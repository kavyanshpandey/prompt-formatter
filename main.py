import streamlit as st

st.title("Format Your Prompt 🚀")
st.subheader("We are formatting your prompt as per your LLM requirments")

user_input = st.text_input("Enter prompt here:")

llm_options = ["Mistral AI-7b", "Google Gemma-2b", "Microsoft Phi-2b"]

selected_option = st.selectbox("Select LLM", llm_options)


def format_prompt(text, passed_llm):
    if passed_llm == "Microsoft Phi-2b":
        formatted_prompt = f"""Instruct: {text} \n Output:"""
    elif passed_llm == "Google Gemma-2b":
        formatted_prompt = f"""<bos><start_of_turn>user{text}<end_of_turn>\n<start_of_turn>model"""
    elif passed_llm == "Mistral AI-7b":
        formatted_prompt = f"""<s>[INST] {text} [/INST]"""
    return formatted_prompt


if st.button("Generate"):
    st.write("Copy it: ")
    st.write(format_prompt(user_input, selected_option))


