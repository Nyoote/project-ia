import torch
import os
import argparse
import ollama
from localrag import ollama_chat
from upload import upload_text

PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

if __name__ == "__main__":

    print(GREEN + "Parsing command-line arguments..." + RESET_COLOR)
    parser = argparse.ArgumentParser(description="Ollama Chat")
    parser.add_argument("--model", default="llama3.2:1b", help="Ollama model to use (default: llama3.2:1b)")
    parser.add_argument("--no-rag", action="store_false", dest="rag", help="Start script without localrag")
    parser.add_argument("--temperature", type=float, help="Temperature setting for the model")
    args = parser.parse_args()

    vault_content = []
    vault_embeddings = []

    if args.rag :
        upload_text()
        if os.path.exists("vault.txt"):
            print(GREEN + "Loading vault content..." + RESET_COLOR)
            with open("vault.txt", "r", encoding='utf-8') as vault_file:
                vault_content = vault_file.readlines()
            print(GREEN + "Generating embeddings for the vault content..." + RESET_COLOR)
            for content in vault_content:
                response = ollama.embeddings(model='mxbai-embed-large', prompt=content)
                vault_embeddings.append(response["embedding"])
            print(GREEN + "Converting embeddings to tensor..." + RESET_COLOR)
        else:
            print(PINK + "No vault to embed, pls try again." + RESET_COLOR)
    else :
        print(PINK + "No localrag" + RESET_COLOR)


    vault_embeddings_tensor = torch.tensor(vault_embeddings) 

    print(GREEN + "Starting conversation loop..." + RESET_COLOR)
    conversation_history = []
    system_message = "You are a helpful assistant that is an expert at extracting the most useful information from a given text. Also bring in extra relevant infromation to the user query from outside the given context."

    while True:
        if args.rag :
            user_input = input(YELLOW + "Ask a question about volley-ball (or type 'quit' to exit): " + RESET_COLOR)
        else:
            user_input = input(YELLOW + "Ask a question (or type 'quit' to exit): " + RESET_COLOR)
        if user_input.lower() == 'quit':
            break
        
        response = ollama_chat(user_input, system_message, vault_embeddings_tensor, vault_content, 
                       args.model, conversation_history, temperature=args.temperature)
        print(GREEN + "Response: \n\n" + response + RESET_COLOR)