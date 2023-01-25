from dataclasses import dataclass
from typing import List


class ResponseError(Exception):
    pass


@dataclass
class ResponseErrorData:
    code: int
    message: str


@dataclass
class ResponsePaymentCreation:
    transaction_id: int
    pay_id: int
    status: str
    payment_url: str


@dataclass
class PaymentData:
    transaction_id: int
    pay_id: int
    status: str
    method: str
    amount: int
    currency: str
    profit: int
    email: str
    desc: str
    date: str
    pay_date: str


@dataclass
class ResponsePaymentGetting:
    total: int
    payments: List[PaymentData]
