import os
import uuid
import streamlit as st
from Agent.text_extractor import extract_text

if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())
user_id = st.session_state["user_id"]

key = st.secrets["API_KEY"]
endpoint = st.secrets["API_ENDPOINT"]

st.title("De Imagen 🖼️ a Texto 📖")
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
        st.subheader("Texto Generado 📖")
        if os.path.exists(destino):
            if st.button("Extraer Texto", icon="📖"):
                carga = st.spinner("Procesando...", width = "stretch")
                with carga:
                    texto = extract_text(destino, key, endpoint)
                    st.session_state[f"texto_extraido_{user_id}"] = texto
                    st.session_state[f"texto_listo_{user_id}"] = True
                st.success("Texto extraido con exito ✅")
                
                if st.session_state.get(f"texto_listo_{user_id}"):
                    texto_final = st.session_state.get(f"texto_extraido_{user_id}", "")
                    st.code(texto_final, language="text")


