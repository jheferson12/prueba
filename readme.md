# My FastAPI Project

This project is a REST API built with FastAPI and MySQL.

## Prerequisites

- Python 3.7+
- MySQL
- phpMyAdmin (optional, for database management)

## Setup

1. Clone the repository:
   ```
   git clone https://jheferson12.github.io/bases_datos.git
   cd bases_datos
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and configure environment variables:
   ```
   APP_NAME=My FastAPI App
   DEBUG=True
   DATABASE_URL=mysql://user:password@localhost/db_name
   ```
   Replace `user`, `password`, and `db_name` with your MySQL credentials.

5. Create the database in MySQL:
   - Use phpMyAdmin or MySQL client to create a new database.
   - The database name should match the one specified in `DATABASE_URL`.

6. Create database tables:
   ```
   python -m app.database
   ```

## Running the Application

To start the development server:
```
uvicorn main:app --reload
```