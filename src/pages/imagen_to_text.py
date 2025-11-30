import streamlit as st
import os
st.title("De Imagen 🖼️ a Texto 📖")
st.divider()

st.markdown("Sube una Imagen")

archivo = st.file_uploader("Sube tu imagen aqui", accept_multiple_files=False, type=["jpg", "jpeg", "png"])  
if archivo is not None:
    # Especifica la carpeta donde deseas guardar el archivo
    save_folder = "archivos_subidos"
    os.makedirs(save_folder, exist_ok=True)
    save_path = os.path.join(save_folder, archivo.name)
    # Guarda el archivo en el disco
    with open(save_path, "wb") as f:
        f.write(archivo.getbuffer())
    destino = f"archivos_subidos/image.png"
    if os.path.exists(destino):
        os.remove(destino)
    os.rename(save_path, destino)
    st.success(f"Archivo guardado subido con exito ✅")
    st.image(archivo)
st.divider()

st.button
