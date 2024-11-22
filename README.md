
# Project-Ia

### ℹ️ Project description

This project is a virtual chat with Ollama.

## Getting started

### ⚙️ Prerequisites

Make sure you have the following installed before proceeding:

- [Python](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/download)

### 🚦 Run the project

Follow these steps to run the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Nyoote/project-ia.git
   ```
2. **Navigate to the project directory:**

   ```bash
   cd project-ia
   ```
3. **Install the dependencies:**

   - Requirements

     ```bash
     pip install -r requirements.txt
     ```
     ```bash
     pip3 install --no-cache-dir \
         --index-url https://download.pytorch.org/whl/nightly/cpu \
         torch \
         torchvision \
         torchaudio
     ```
   - Ollama:

     ```bash
     ollama pull llama3.2:1b
     ```
     ```bash
     ollama pull mxbai-embed-large
     ```
4. **Run project:**

    With this command, Ollama takes into account the pdf information by default

     ```bash
     python3 app.py
     ```
5. **Add args to start Project:**

    If you want you can add arguments to your command in order to start the project.

   - You can avoid to use rag so Ollama does not take pdf information into account:

   ```bash
   python3 app.py --no-rag
   ```
   - You can choose the temperature for Ollama's response:

   ```bash
   python3 app.py --temperature <from 0 to 1>
   ```
   - You can add as multiple arguments. Example:

   ```bash
   python3 app.py --no-rag --temperature 0.2
   ```
  