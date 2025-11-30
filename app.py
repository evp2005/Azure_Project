import streamlit as st

sidebar_logo = "src\images\logo.png"
main_body_logo = "src\images\icon.png"

st.logo(
    sidebar_logo,
    icon_image=main_body_logo
    )

navigator = st.navigation(["src/pages/imagen_to_text.py", "src/pages/face_detection.py"])

navigator.run()

