import PyPDF2
import requests
from io import BytesIO

def get_pdf_from_drive(drive_url):
    try:
        file_id = drive_url.split("/d/")[1].split("/")[0]
    except IndexError:
        raise ValueError("Google Drive link is invalid.")

    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"

    response = requests.get(download_url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception(f"Échec du téléchargement. Code HTTP : {response.status_code}")
    
def convert_pdf_to_text(file_path, text_file):
    try:
        reader = PyPDF2.PdfReader(file_path)
        with open('text_file.txt', 'w', encoding='utf-8') as txt_file:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    txt_file.write(text + "\n")
        print(f"Le texte a été extrait et enregistré dans : {text_file}")
    except Exception as e:
        raise Exception(f"Erreur lors de l'extraction du texte : {e}")
    

if __name__ == "__main__":
    drive_url = "https://drive.google.com/file/d/1Vg86jmDW_jDGdaiy2Dyu_Coaxe76guDU/view?usp=sharing"
    text_file = "vault.txt"

    try:
        pdf_stream = get_pdf_from_drive(drive_url)

        convert_pdf_to_text(pdf_stream, text_file)
    except Exception as err:
        print(f"Erreur : {err}")
