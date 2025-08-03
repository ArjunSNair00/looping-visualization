import streamlit as st
import streamlit.components.v1 as components

try:
    with open("idk.html", "r") as f:
        html_data = f.read()
    components.html(html_data, height=400, width=700)
except FileNotFoundError:
    st.error("idk.html not found. Please create it or provide the correct path.")