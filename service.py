from sqlalchemy.orm import Session
from typing import List
from fastapi import Request, UploadFile
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_accounts(db: Session, raw_data: schemas.GetAccounts):
    account_id:str = raw_data.account_id
    account_number:str = raw_data.account_number
    account_type:str = raw_data.account_type
    balance:str = raw_data.balance
    status:str = raw_data.status


    record_to_be_added = {'account_id': account_id, 'account_number': account_number, 'account_type': account_type, 'balance': balance, 'status': status}
    new_accounts = models.Accounts(**record_to_be_added)
    db.add(new_accounts)
    db.commit()
    db.refresh(new_accounts)
    accounts_inserted_record = new_accounts


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/posts/1',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    external_api_placeholder = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    headers['Authorization'] = 'Bearer '
    payload = {}
    apiResponse = requests.get(
        'https://reqres.in/api/users/2',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    get_url = apiResponse.json() if 'dict' == 'raw' else apiResponse.text
    res = {
        'accounts_inserted_record': accounts_inserted_record,
    }
    return res

async def get_accounts_account_id(db: Session, account_id: int):

    accounts_one = db.query(models.Accounts).filter(models.Accounts.account_id == 'account_id').first()
    res = {
        'accounts_one': accounts_one,
    }
    return res

async def post_accounts(db: Session, raw_data: schemas.PostAccounts):
    account_id:str = raw_data.account_id
    account_number:str = raw_data.account_number
    account_type:str = raw_data.account_type
    balance:str = raw_data.balance
    status:str = raw_data.status


    record_to_be_added = {'account_id': account_id, 'account_number': account_number, 'account_type': account_type, 'balance': balance, 'status': status}
    new_accounts = models.Accounts(**record_to_be_added)
    db.add(new_accounts)
    db.commit()
    db.refresh(new_accounts)
    accounts_inserted_record = new_accounts


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/posts/1',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    external_api_placeholder = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {}
    headers['Authorization'] = 'Bearer '
    payload = {}
    apiResponse = requests.get(
        'https://reqres.in/api/users/2',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    get_url = apiResponse.json() if 'dict' == 'raw' else apiResponse.text


    import requests

    headers = {'user_id': 1, 'first_name': shivam}
    
    payload = {'user_id': 1, 'first_name': test, 'last_name': }
    apiResponse = requests.post(
        'https://reqres.in/api/users',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    post_api = apiResponse.json() if 'dict' == 'raw' else apiResponse.text
    res = {
        'accounts_inserted_record': accounts_inserted_record,
    }
    return res

async def put_accounts_account_id(db: Session, raw_data: schemas.PutAccountsAccountId):
    account_id:str = raw_data.account_id
    account_number:str = raw_data.account_number
    account_type:str = raw_data.account_type
    balance:str = raw_data.balance
    status:str = raw_data.status


    accounts_edited_record = db.query(models.Accounts).filter(models.Accounts.account_id == account_id).first()
    for key, value in {'account_id': account_id, 'account_number': account_number, 'account_type': account_type, 'balance': balance, 'status': status}.items():
          setattr(accounts_edited_record, key, value)
    db.commit()
    db.refresh(accounts_edited_record)
    accounts_edited_record = accounts_edited_record

    res = {
        'accounts_edited_record': accounts_edited_record,
    }
    return res

async def delete_accounts_account_id(db: Session, account_id: int):

    accounts_deleted = None
    record_to_delete = db.query(models.Accounts).filter(models.Accounts.account_id == account_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        accounts_deleted = record_to_delete
    res = {
        'accounts_deleted': accounts_deleted,
    }
    return res

async def get_transactions(db: Session):

    Transactions_all = db.query(models.Transactions).order_by(models.Transactions.id).all()
    res = {
        'Transactions_all': Transactions_all,
    }
    return res

async def get_transactions_transaction_id(db: Session, transaction_id: int):

    Transactions_one = db.query(models.Transactions).filter(models.Transactions.transaction_id == 'transaction_id').first()
    res = {
        'Transactions_one': Transactions_one,
    }
    return res

async def post_transactions(db: Session, raw_data: schemas.PostTransactions):
    transaction_id:str = raw_data.transaction_id
    account_id:str = raw_data.account_id
    amount:str = raw_data.amount


    record_to_be_added = {'transaction_id': transaction_id, 'account_id': account_id, 'amount': amount}
    new_Transactions = models.Transactions(**record_to_be_added)
    db.add(new_Transactions)
    db.commit()
    db.refresh(new_Transactions)
    Transactions_inserted_record = new_Transactions
    res = {
        'Transactions_inserted_record': Transactions_inserted_record,
    }
    return res

async def put_transactions_transaction_id(db: Session, raw_data: schemas.PutTransactionsTransactionId):
    transaction_id:str = raw_data.transaction_id
    account_id:str = raw_data.account_id
    amount:str = raw_data.amount


    Transactions_edited_record = db.query(models.Transactions).filter(models.Transactions.transaction_id == transaction_id).first()
    for key, value in {'transaction_id': transaction_id, 'account_id': account_id, 'amount': amount}.items():
          setattr(Transactions_edited_record, key, value)
    db.commit()
    db.refresh(Transactions_edited_record)
    Transactions_edited_record = Transactions_edited_record

    res = {
        'Transactions_edited_record': Transactions_edited_record,
    }
    return res

async def delete_transactions_transaction_id(db: Session, transaction_id: int):

    Transactions_deleted = None
    record_to_delete = db.query(models.Transactions).filter(models.Transactions.transaction_id == transaction_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Transactions_deleted = record_to_delete
    res = {
        'Transactions_deleted': Transactions_deleted,
    }
    return res

