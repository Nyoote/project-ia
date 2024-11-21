import PyPDF2

def convert_pdf_to_text():
    file_path = "panda-roux-infographie.pdf"
    text_file = 'vault.txt'
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
    

convert_pdf_to_text()
