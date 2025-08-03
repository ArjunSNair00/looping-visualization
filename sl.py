import streamlit as st

st.title("For loop visualization")
# Slider to control the upper limit of the loop
limit = st.slider("Loop up to the chosen limit", 1, 20, value=10)

# Loop up to the chosen limit
for i in range(limit):
    st.write(f"Value of :blue[***i***]: {i}")