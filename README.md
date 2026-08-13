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
git clone https://github.com/TVOJ_USERNAME/fastapi-document-analyzer.git
cd fastapi-document-analyzer