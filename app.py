import streamlit as st



sidebar_logo = "src/resources/images/logo.png"
main_body_logo = "src/resources/images/icon.png"

def __main__():
    st.logo(
    sidebar_logo,
    icon_image=main_body_logo
    )
    pg = st.navigation(["src/pages/imagen_to_text.py", "src/pages/face_detection.py"])
    pg.run()

if '__main__' == __name__:
    __main__()

