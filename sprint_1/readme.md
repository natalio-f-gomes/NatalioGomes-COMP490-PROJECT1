# Author: Natalio Gomes
#### Class: COMP 490
#### Section: 003

## Project 1 – Sprint 1

### Prerequisites

- Git
- Python 3.11
- pyenv
- pip

## Setup Process

1. Clone the repository and navigate into the project folder

   ```bash
   git clone git@github.com:natalio-f-gomes/COMP490-Project1.git
   cd sprint-1
   ```

2. Check your current Python version

   ```bash
   python3 --version
   ```


3. Create and activate a virtual environment

   ```bash
   python -m venv DevEnv
   source DevEnv/bin/activate   # On Windows: DevEnv\Scripts\activate
   ```

4. Clone the Vosk API repository (needed for model files)

   ```bash
   git clone https://github.com/alphacep/vosk-api
   ```

5. Install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Open the project in **PyCharm** (or your preferred IDE)
2. Set the interpreter to the virtual environment (`DevEnv`)
3. Run the main script
4. Speak clearly into your microphone
5. Say the exit command to exit

The application uses **Vosk API** to perform offline speech-to-text transcription.

## Running Tests

```bash
pytest tests/
```


I found this article quite interesting: 
https://jatinchowdhury18.medium.com/some-thoughts-on-audio-data-types-2124d0a2defa
