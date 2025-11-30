import cv2
import os

def detect_and_save_faces(image_path, output_directory="./src/resources/images"):
    # Asegurarse de que el directorio de salida exista
    os.makedirs(output_directory, exist_ok=True)

    # Cargar el clasificador pre-entrenado de Haar Cascade
    # cv2.data.haarcascades apunta a la carpeta donde estan los xml
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Lee la imagen
    img = cv2.imread(image_path)
    if img is None:
        print(f"ERROR: No se pudo cargar la imagen en: {image_path}")
        raise ValueError(f"No se pudo cargar la imagen en: {image_path}")
    else:
        print(f"Imagen cargada exitosamente desde: {image_path}")

    # Convertir a escala de grises (necesario para Haar Cascades)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar rostros
    # scaleFactor=1.1, minNeighbors=5 son valores estandar
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print(f"Rostros detectados: {len(faces)}")

    for (x, y, w, h) in faces:
        # Dibujar rectángulo
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    # Generar nombre de archivo de salida
    filename = os.path.basename(image_path)
    output_path = os.path.join(output_directory, f"detected_{filename}")

    # Guardar la imagen
    success = cv2.imwrite(output_path, img)
    if success:
        print(f"Imagen guardada exitosamente en: {output_path}")
    else:
        print(f"ERROR: No se pudo guardar la imagen en: {output_path}")
    
    return output_path
