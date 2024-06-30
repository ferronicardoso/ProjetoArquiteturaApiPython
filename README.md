# Projeto - Arquitetura Api Python

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/ferronicardoso/ProjetoArquiteturaApiPython.git
    cd ProjetoArquiteturaApiPython
    ```

2. Create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file with your database configuration (example provided above).

5. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Running Tests

To run the tests, use:
```bash
pytest
