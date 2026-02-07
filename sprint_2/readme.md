# Author: Natalio Gomes
#### Class: COMP 490
#### Section: 003

## Project 1 – Sprint 2

### Prerequisites

- Git
- Python 3.11
- pyenv
- pip

## Setup Process

1. Clone the repository and navigate into the project folder

   ```bash
   git clone git@github.com:natalio-f-gomes/COMP490-Project1.git
   cd sprint-2
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


5. Install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Open the project in **PyCharm** (or your preferred IDE)
2. Set the interpreter to the virtual environment (`DevEnv`)
3. Run the main script

## Running Tests

```bash
pytest tests/
```
