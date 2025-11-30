from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")
endpoint = os.getenv("API_ENDPOINT")

def extract_text(image_path: str):
    loader = AzureAIDocumentIntelligenceLoader(
        file_path=image_path,
        api_key=key,
        api_endpoint=endpoint
    )
    documents = loader.load()
    doc = documents[0].page_content
    return str(doc)
     

# Pruebas
#texto = extract_text("C:\\Users\\usuario\\OneDrive\\Escritorio\\FaceApp\\FaceApp\\archivos_subidos\\urresti.jpg")
#print(texto)
#print(type(texto))