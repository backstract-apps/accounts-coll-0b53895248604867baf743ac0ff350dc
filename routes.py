from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/accounts/')
async def get_accounts(raw_data: schemas.GetAccounts, db: Session = Depends(get_db)):
    try:
        return await service.get_accounts(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/accounts/account_id')
async def get_accounts_account_id(account_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_accounts_account_id(db, account_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/accounts/')
async def post_accounts(raw_data: schemas.PostAccounts, db: Session = Depends(get_db)):
    try:
        return await service.post_accounts(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/accounts/account_id/')
async def put_accounts_account_id(raw_data: schemas.PutAccountsAccountId, db: Session = Depends(get_db)):
    try:
        return await service.put_accounts_account_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/accounts/account_id')
async def delete_accounts_account_id(account_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_accounts_account_id(db, account_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/transactions/')
async def get_transactions(db: Session = Depends(get_db)):
    try:
        return await service.get_transactions(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/transactions/transaction_id')
async def get_transactions_transaction_id(transaction_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_transactions_transaction_id(db, transaction_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/transactions/')
async def post_transactions(raw_data: schemas.PostTransactions, db: Session = Depends(get_db)):
    try:
        return await service.post_transactions(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/transactions/transaction_id/')
async def put_transactions_transaction_id(raw_data: schemas.PutTransactionsTransactionId, db: Session = Depends(get_db)):
    try:
        return await service.put_transactions_transaction_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/transactions/transaction_id')
async def delete_transactions_transaction_id(transaction_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_transactions_transaction_id(db, transaction_id)
    except Exception as e:
        raise HTTPException(500, str(e))

