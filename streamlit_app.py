import streamlit as st

st.title("🎈 My first app")
st.write("Hello world")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}")

button = st.button("Click me")

if button:
    st.write(f"Button was clicked")
else:
    st.write(f"not clicked")

st.checkbox("Check me")