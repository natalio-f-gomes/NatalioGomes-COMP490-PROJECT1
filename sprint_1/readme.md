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
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

4. Clone the Vosk API repository (needed for model files)

   ```bash
   git clone https://github.com/alphacep/vosk-api
   ```

5. Install Python dependencies

   ```bash
   pip3 install -r requirements.txt #macOS
   pip install -r requirements.txt  #Windows
   ```

## Running the Application
1. cd sprint_1
```bash
python3 app.py # macOS
python app.py  # windows
```
2. Run the main script
3. Speak clearly into your microphone
4. Say the exit command to exit

## Running Tests

```bash
python -m pytest
```
The application uses **Vosk API** to perform offline speech-to-text transcription.

## Running Tests

```bash
pytest tests/
```

I found this article quite interesting: 
https://jatinchowdhury18.medium.com/some-thoughts-on-audio-data-types-2124d0a2defa
