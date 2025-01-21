from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Accounts(Base):
    __tablename__ = 'accounts'
    account_id = Column(Integer, primary_key=True)
    account_number = Column(String, primary_key=False)
    account_type = Column(String, primary_key=False)
    balance = Column(Integer, primary_key=False)
    status = Column(String, primary_key=False)

class Transactions(Base):
    __tablename__ = 'Transactions'
    transaction_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, primary_key=False)
    amount = Column(Integer, primary_key=False)

