import streamlit as st
from PIL import Image

st.title("Skin Cancer Detection")
st.write("Apni skin ki tasveer upload karein")

uploaded_file = st.file_uploader("Tasveer Yahan Upload Karein", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Tumhari Tasveer", use_column_width=True)
    st.write("Checking...")
    st.success("Result: Ye tasveer Normal lag rahi hai. (Demo Result)")
    st.write("Note: Ye demo version hai. Asli result ke liye doctor se check karwayein.")
