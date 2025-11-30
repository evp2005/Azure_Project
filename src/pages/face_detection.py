import os
import uuid
import streamlit as st
from Agent.detection_face import detect_and_save_faces

if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())
user_id = st.session_state["user_id"]

st.title("Deteccion de Rostros 😏")
st.divider()

archivo = st.file_uploader("Sube tu imagen aqui", accept_multiple_files=False, type=["jpg", "jpeg", "png"])  
if archivo is not None:
    # Especifica la carpeta donde deseas guardar el archivo
    save_folder = "archivos_subidos"
    os.makedirs(save_folder, exist_ok=True)
    save_path = os.path.join(save_folder, archivo.name)
    # Guarda el archivo en el disco
    with open(save_path, "wb") as f:
        f.write(archivo.getbuffer())
    destino = f"archivos_subidos/image{user_id}.png"
    if os.path.exists(destino):
        os.remove(destino)
    os.rename(save_path, destino)
    st.success(f"Archivo subido con exito ✅")
st.divider()

col1, col2 = st.columns(2)

if archivo is not None:
    with col1:
        st.subheader("Imagen Subida 🖼️")
        st.image(archivo)
    with col2:
        st.subheader("Detección de Rostros 🤯")
        if os.path.exists(destino):
            if st.button("Detectar Rostro", icon="🤖"):
                carga = st.spinner("Procesando...", width = "stretch")
                with carga:
                    imagen_final = detect_and_save_faces(destino)
                    st.session_state[f"imagen_procesada_{user_id}"] = imagen_final
                    st.session_state[f"rostro_detectado_{user_id}"] = True
                st.success("Rostro detectado con exito ✅")
                
                if st.session_state.get(f"rostro_detectado_{user_id}"):
                    imagen_final = st.session_state.get(f"imagen_procesada_{user_id}", "")
                    st.image(imagen_final)


