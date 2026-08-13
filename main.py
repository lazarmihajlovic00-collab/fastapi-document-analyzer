import re
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Importujemo naše stvari za bazu
from database import engine, SessionLocal, Base
from models import DocumentDB

# 1. SQLAlchemy komanda koja kreira tabele u bazi ako ne postoje (Kao ddl-auto=update u Springu)
Base.metadata.create_all(bind=engine)

app = FastAPI()

class DocumentRequest(BaseModel):
    text: str

# 2. Dependency Injection funkcija. 
# Otvara konekciju ka bazi za svaki zahtev i zatvara je kada se zahtev završi.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 3. Ubačen db: Session parametar! FastAPI će automatski pozvati get_db() i ubaciti konekciju.
@app.post("/analyze")
def analyze_document(doc: DocumentRequest, db: Session = Depends(get_db)):
    # Regex logika (ostaje ista)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    found_emails = re.findall(email_pattern, doc.text)
    
    # 4. Spašavanje u bazu
    # Pošto u model.py čuvamo mejlove kao String, spojićemo listu mejlova zarezima
    emails_string = ",".join(found_emails)
    
    # Kreiramo objekat koji ide u bazu (kao new Entity() u Javi)
    new_db_document = DocumentDB(original_text=doc.text, extracted_emails=emails_string)
    
    # Dodajemo i komitujemo
    db.add(new_db_document)
    db.commit()
    
    # Osvežavamo objekat kako bismo dobili ID koji je Postgres automatski generisao
    db.refresh(new_db_document)
    
    return {
        "message": "Uspesno sacuvano u bazu!",
        "document_id": new_db_document.id, # Vraćamo generisani ID klijentu
        "extracted_emails": found_emails
    }

# GET ruta za čitanje iz baze
@app.get("/documents")
def get_all_documents(db: Session = Depends(get_db)):
    # db.query(ImeKlase).all() je ekvivalent repository.findAll()
    all_documents = db.query(DocumentDB).all()
    
    # FastAPI će automatski pretvoriti listu objekata u JSON format!
    return all_documents