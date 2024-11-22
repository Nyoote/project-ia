import PyPDF2
import requests
from io import BytesIO
import json
import argparse
from openai import OpenAI

def get_pdf_from_drive(drive_url):
    try:
        file_id = drive_url.split("/d/")[1].split("/")[0]
    except IndexError:
        raise ValueError("Le lien Google Drive est invalide.")

    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = requests.get(download_url)
    
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception(f"Échec du téléchargement. Code HTTP : {response.status_code}")

def convert_pdf_to_text(file_path):
    extracted_text = ""
    try:
        reader = PyPDF2.PdfReader(file_path)
        with open('vault.txt', 'w', encoding='utf-8') as txt_file:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    txt_file.write(text + "\n")
                    extracted_text += text + "\n"
        print(f"Le texte a été extrait et enregistré dans : vault.txt")
        return extracted_text
    except Exception as e:
        raise Exception(f"Erreur lors de l'extraction du texte : {e}")

if __name__ == "__main__":
    drive_url = "https://drive.google.com/file/d/1aP0TDiB5JuABGo8VgNTryQS7exlWxWwu/view?usp=sharing"
    ollama_api_url = "http://localhost:11434/v1"
    
    try:
        file_path = get_pdf_from_drive(drive_url)
        
        extracted_text = convert_pdf_to_text(file_path) 

        parser = argparse.ArgumentParser(description="Ollama Chat")
        parser.add_argument("--model", default="llama3.2:1b", help="Ollama model to use (default: llama3.2:1b)")
        args = parser.parse_args()

    
        print("Starting chat system. Type 'quit' to exit.")
        conversation_history = [] 

        vault_embeddings_tensor, vault_content = initialize_rag()
        print("Starting chat system. Type 'quit' to exit.")
        conversation_history = []
        system_message = "You are a helpful assistant that is an expert at extracting the most useful information from a given text. Also bring in extra relevant information to the user query from outside the given context."

        user_input = "No questions for now"
        print("\nTraitement de votre question...\n")
        response = ollama_chat(user_input, system_message, 
                            vault_embeddings_tensor,
                            extracted_text, args.model, 
                            conversation_history)
        print("Réponse:\n", response)
        
    except Exception as err:
        print(f"Erreur : {err}")

