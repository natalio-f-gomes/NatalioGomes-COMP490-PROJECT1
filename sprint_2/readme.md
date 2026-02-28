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
   git clone git@github.com:natalio-f-gomes/NatalioGomes-COMP490-PROJECT1.git
   cd sprint_2
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


5. Install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```
6. Env Secrets
Create a (.env) located inside sprint_2 dir and fill the secrets. By the way, the server address should not have a ":" at the end. And the port address should not have a "/" at the end.

```bash
EMAIL=
PASSWORD=
SERVER_ADDRESS=
SERVER_PORT=
```

7. Running the Application

```bash
python3 main.py # macOS
python main.py  # windows
```

Notes: The DisplayDataInTerminal located in the display_data.py exists to quickly CRUD the data

8. Running Tests

```bash
python -m pytest
```

9. Running GitHub Actions Workflows

Select the Sprint-2 Workflow and run the workflow.
The workflow also gets triggered automatically by a push to the main branch