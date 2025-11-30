import os
from dotenv import load_dotenv
from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader

def extract_text(image_path: str, key: str, endpoint: str):
    loader = AzureAIDocumentIntelligenceLoader(
        file_path=image_path,
        api_key=key,
        api_endpoint=endpoint
    )
    print("Loader creado, credenciales validas")
    print("=======================================")
    documents = loader.load()
    doc = documents[0].page_content
    print("Texto Extraido")
    print("=======================================")
    return str(doc)
     

# Pruebas
#texto = extract_text("C:\\Users\\usuario\\OneDrive\\Escritorio\\FaceApp\\FaceApp\\archivos_subidos\\urresti.jpg")
#print(texto)
#print(type(texto))