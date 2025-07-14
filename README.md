# Mini_rag
this is a minial implement of the RAG model for question
Requirements
-Python 3.8 or later
Install the required packages
$ pip install -r requirements.txt
Setup the environment variables
$ cp .env.example .env
Run Alembic Migration
$ alembic upgrade head
Set your environment variables in the .env file. Like OPENAI_API_KEY value.

Run Docker Compose Services
$ cd docker
$ cp .env.example .env
update .env with your credentials
$ cd docker
$ sudo docker compose up -d
Run the FastAPI server
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
POSTMAN Collection
Download the POSTMAN collection from /assets/mini-rag-app.postman_collection.json
