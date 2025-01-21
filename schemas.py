from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Accounts(BaseModel):
    account_id: int
    account_number: str
    account_type: str
    balance: int
    status: str


class ReadAccounts(BaseModel):
    account_id: int
    account_number: str
    account_type: str
    balance: int
    status: str
    class Config:
        from_attributes = True


class Transactions(BaseModel):
    transaction_id: int
    account_id: int
    amount: int


class ReadTransactions(BaseModel):
    transaction_id: int
    account_id: int
    amount: int
    class Config:
        from_attributes = True




class GetAccounts(BaseModel):
    account_id: str
    account_number: str
    account_type: str
    balance: str
    status: str

    class Config:
        from_attributes = True



class PostAccounts(BaseModel):
    account_id: str
    account_number: str
    account_type: str
    balance: str
    status: str

    class Config:
        from_attributes = True



class PutAccountsAccountId(BaseModel):
    account_id: str
    account_number: str
    account_type: str
    balance: str
    status: str

    class Config:
        from_attributes = True



class PostTransactions(BaseModel):
    transaction_id: str
    account_id: str
    amount: str

    class Config:
        from_attributes = True



class PutTransactionsTransactionId(BaseModel):
    transaction_id: str
    account_id: str
    amount: str

    class Config:
        from_attributes = True

