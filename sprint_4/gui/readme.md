# Author: Natalio Gomes
#### Class: COMP 490
#### Section: 003

## Project 1 – Sprint 4 GUI

### Prerequisites

- Git
- Python 3.11
- pyenv
- pip

## Setup Process

1. Clone the repository and navigate into the project folder

   ```bash
   git clone git@github.com:natalio-f-gomes/NatalioGomes-COMP490-PROJECT1.git
   cd sprint_4/gui
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

5. Upgrade Pip and Install Python dependencies

   ```bash
   pip3 install --upgrade pip
   pip3 install -r requirements.txt
   ```

6. Running the Application

```bash
python3 main.py # macOS
python main.py  # windows
```

Notes: Evrytime the user deletes a room, it writes the report located in Report/report.csv

8. Running Tests

```bash
python3 -m pytest tests/*
```
