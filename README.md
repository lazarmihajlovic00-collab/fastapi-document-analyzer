# FastAPI Document Analyzer 🚀

A high-performance REST API service built with **Python** and **FastAPI** that asynchronously parses text documents, extracts key entities (such as email addresses) using Regex, and persists the structured data in a **PostgreSQL** database. 

This project demonstrates modern Python backend development, ORM integration, and containerized deployment.

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Web Server:** Uvicorn
* **Containerization:** Docker & Docker Compose

## ✨ Features

* **Asynchronous Processing:** Built from the ground up for high concurrency using FastAPI.
* **Regex Extraction:** Automated pattern matching to extract valuable entities from raw text.
* **Relational Data Modeling:** Structured persistence using SQLAlchemy ORM.
* **Auto-generated Documentation:** Interactive API exploration via Swagger UI / OpenAPI.
* **Dockerized Database:** Zero-install local database setup via Docker Compose.

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites
* Python 3.10+
* Docker Desktop

### 1. Clone the repository
```bash
git clone https://github.com/lazarmihajlovic00-collab/fastapi-document-analyzer.git
cd fastapi-document-analyzer
```

### 2. Set up the Database (Docker)
Start the PostgreSQL database container in the background:
```bash
docker-compose up -d
```

### 3. Set up the Python Environment
Create a virtual environment and install the dependencies:
```bash
python -m venv venv
# On Windows: .\venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate

pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

### 4. Run the API Server
Start the Uvicorn web server with auto-reload enabled:
```bash
python -m uvicorn main:app --reload
```

## 📖 API Documentation

Once the server is running, navigate to the following URL in your browser to access the interactive Swagger UI documentation:

**http://127.0.0.1:8000/docs**

### Available Endpoints:
* `GET /` - Root health check
* `POST /analyze` - Submit a document text for regex analysis and DB storage
* `GET /documents` - Retrieve all analyzed documents from the PostgreSQL database