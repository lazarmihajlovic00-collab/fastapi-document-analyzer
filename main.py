from fastapi import FastAPI
from pydantic import BaseModel
import re

#Ovo je naš DTO (Data Transfer Object)
class DocumentRequest(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/analyze")
def analyze_document(doc: DocumentRequest):
    # 1. Standardni Regex šablon za pronalaženje email adresa
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # 2. re.findall pronalazi SVA poklapanja u tekstu i vraća ih kao listu (List<String>)
    found_emails = re.findall(email_pattern, doc.text)
    
    # 3. Vraćamo nazad originalni tekst i listu pronađenih mejlova
    return {
        "original_length": len(doc.text),
        "extracted_emails": found_emails
    }