import requests
import PyPDF2
from io import BytesIO

PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

def get_pdf_from_drive(drive_url):
    try:
        file_id = drive_url.split("/d/")[1].split("/")[0]
    except IndexError:
        print(PINK + "Google Drive link is invalid" + RESET_COLOR)
        raise ValueError("Google Drive link is invalid")

    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = requests.get(download_url)
    
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        print(PINK + "Failed Download" + RESET_COLOR)
        raise Exception("Failed Download")
    
def convert_pdf_to_text(file_path):
    try:
        reader = PyPDF2.PdfReader(file_path)
        with open('vault.txt', 'w', encoding='utf-8') as txt_file:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    txt_file.write(text + "\n")
        print(GREEN + "Text has been created and saved in vault.txt" + RESET_COLOR)
    except Exception as e:
        print(PINK + "Error while extracting text" + RESET_COLOR)
        raise Exception(f"Error while extracting text : {e}")

def upload_text():
    drive_url = "https://drive.google.com/file/d/1HpRnlEpXu0TK51V0uvgeCkxwHAw762IN/view?usp=sharing"
    try:
        file_path = get_pdf_from_drive(drive_url)

        convert_pdf_to_text(file_path)
    except Exception as err:
        print(PINK + f"Error : {err}")