from sqlalchemy import Column, Integer, String, Text
from database import Base

class DocumentDB(Base):
    __tablename__ = "documents"  # Tačno ime tabele kako će se zvati u Postgresu

    # Definišemo kolone
    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    extracted_emails = Column(String, nullable=False)  # Lista mejlova, čuvaćemo je kao string odvojen zarezima