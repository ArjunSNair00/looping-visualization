import streamlit as st
import os
import numpy as np

st.image(os.path.join(os.getcwd(),"assets","images","loop.png"),width=80)
st.title("For loop visualization")
# Slider to control the upper limit of the loop
limit = st.slider("Loop up to the chosen limit", 1, 20, value=3)

forloop=f"""
for i in range({limit}):
  print(f"Value of i: {{i}}")
"""

st.write("Python Code: ")
st.markdown(
    f"""
    <pre style="background-color:#f4f4f4; color:black; padding:10px; border-radius:8px">
    <code>{forloop}</code>
    </pre>
    """,
    unsafe_allow_html=True
)

# or use st.code(forloop,language="python" instead of markdown)


# Loop up to the chosen limit
for i in range(limit):
    st.write(f"Value of :blue[***i***]: {i}")


st.divider()
st.title("Pandas DataFrame Visualization")

import pandas as pd
df = pd.DataFrame({
  'col1': [1, 10, 3, 4],
  'col2': [10, 20, 30, 40]
})

#also use just df
st.subheader("Metrics")
df2=st.data_editor(df) 
# st.dataframe(df2)


#metrics
col1mean = np.mean(df2['col1'])
col2mean = np.mean(df2['col2'])
col1median = np.median(df2['col1'])
col2median = np.median(df2['col2'])
col1, col2=st.columns(2)
with col1:
  st.metric(label=":violet[***Number of records:***] ",value=len(df2))
  st.metric(label="The mean of ':violet[***col1***]' is:",value=col1mean)
  st.metric(label="The median of ':violet[***col1***]' is:",value=col1median)
with col2:
  st.metric(label=":violet[***Number of features:***] ",value=len(df2.columns))
  st.metric(label="The mean of ':violet[***col2***]' is:",value=col2mean)
  st.metric(label="The median of ':violet[***col2***]' is:",value=col2median)

st.divider()
st.subheader("Using JSON")
samplejson={"Name":"Arjun S Nair","Age":19}
st.json(samplejson)

st.divider()
st.title("Displaying in the same line")
n=st.number_input(
    "Enter how many times to display 'hello'",
    min_value=0,
    max_value=None,
    value=5,
    step=1,
    format=None
)
n=int(n)
output = st.empty()
text = ""
for i in range(n):
    text += "hello "
    output.text(text)

st.divider()
st.header("Streamlit buttons behave like switches")
print('\nRun')
pressed=st.button("Press me")
pressed2=st.button("Press me 2")
print(pressed)
print(pressed2)
if pressed2:
    "you pressed the second button"
if pressed:
    "you pressed the first button"

st.markdown("This is **_Markdown_**")


#data visualization
st.subheader("Data Visualization")
scatter_data=pd.DataFrame({'x':np.random.randn(100),'y':np.random.randn(100)})
st.scatter_chart(scatter_data)

#map
st.subheader("Map")
#college coordinates
college_coords = [9.0035, 76.5310]

# Generate random points around the college location
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + college_coords,  # smaller spread
    columns=['lat', 'lon']
)
st.map(map_data)

# st.pyplot
