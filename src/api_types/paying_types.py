from typing import Literal

PAYMENT_CURRENCIES = Literal[
    "RUB",  # Russian ruble
    "UAH",  # Ukrainian hryvnia
    "BYN",  # Belarusian ruble
    "KZT",  # Kazakhstani tenge
    "USD",  # US dollar
    "EUR",  # Euro
]


PAYMENT_METHODS = Literal[
    "qiwi",  # QIWI Wallet
    "ym",  # YooMoney
    "wm",  # WebMoney
    "card",  # Bank card
    "advcash",
    "pm",  # Perfect Money
    "applepay",
    "googlepay",
    "samsungpay",
    "sbp",
    "payeer",
    "btc",  # Bitcoin
    "eth",  # Ethereum
    "bch",  # Bitcoin Cash
    "ltc",  # Litecoin
    "dash",  # Dash
    "zec",  # Zcash
    "doge",  # Dogecoin
    "usdt",  # Tether
    "mts",
    "beeline",
    "megafon",
    "tele2",
    "term",  # Terminal
]
PAYMENT_CURRENCY_METHODS = Literal[
    'wm',
    'advcash',
    'pm'
]

PAYMENT_STATUS = Literal[
    'paid',
    'waiting',
    'refund',
    'canceled',
    'expired',
    'error'
]
