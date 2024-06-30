# Python API Architecture

🇺🇸 This project aims to design and implement a simple, efficient API architecture using Python. It will cover essential topics such as RESTful API design, authentication, database integration, and error handling. By the end, you'll know how to create and manage APIs effectively.

🇧🇷 Este projeto visa projetar e implementar uma arquitetura de API simples e eficiente usando Python. Abrangerá tópicos essenciais como design de API RESTful, autenticação, integração com banco de dados e tratamento de erros. Ao final, você saberá como criar e gerenciar APIs de forma eficaz.

🇪🇸 Este proyecto tiene como objetivo diseñar e implementar una arquitectura de API simple y eficiente usando Python. Cubrirá temas esenciales como diseño de API RESTful, autenticación, integración con bases de datos y manejo de errores. Al final, sabrás cómo crear y gestionar APIs de manera efectiva.

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
