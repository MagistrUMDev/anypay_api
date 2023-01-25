from hashlib import sha256
import aiohttp
from api_types import *


class PayApi():
    def __init__(self, api_id: str, api_key: str, project_id: int):
        self.api_id: str = api_id
        self.api_key: str = api_key
        self.project_id: int = project_id

    def generate_sign(self, method: str, *args) -> str:
        """Generate a control signature."""
        params = ''.join([str(i) for i in args])
        return sha256(f'{method}{self.api_id}{params}{self.api_key}'.encode()).hexdigest()

    async def create_request(self, path: str, sign: str, **params):
        params['sign'] = sign
        url = f"https://anypay.io/api/{path}/{self.api_id}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "multipart/form-data",
        }
        async with aiohttp.ClientSession() as session:
            async with session.request('POST', headers=headers, url=url, params=params) as response:
                res = await response.json()
                try:
                    return res['result']
                except:
                    err_data = res['error']
                    error = ResponseErrorData(**err_data)
                    raise ResponseError(
                        f'Exception while creating request: {error.code}:{error.message}')

    async def create_payment(
        self,
        pay_id: int,
        amount: int,
        currency: PAYMENT_CURRENCIES,
        desc: str,
        method: PAYMENT_METHODS,
        method_currency: PAYMENT_CURRENCY_METHODS,
        email: str,
        phone: int = None,
        tail: int = None,
        success_url: str = None,
        fail_url: str = None,
        lang: str = None,
    ) -> ResponsePaymentCreation:
        sign = self.generate_sign(
            "create-payment", self.project_id, pay_id, amount, currency, desc, method
        )
        response = await self.create_request(
            "create-payment",
            sign,
            pay_id=pay_id,
            amount=amount,
            currency=currency,
            desc=desc,
            method=method,
            email=email,
            method_currency=method_currency,
            phone=phone,
            tail=tail,
            success_url=success_url,
            fail_url=fail_url,
            lang=lang
        )
        return ResponsePaymentCreation(**response)

    async def get_payments(self, trans_id: int, offset: int = None, payout_id: int = None) -> ResponsePaymentGetting:
        sign = self.generate_sign(
            "payments", self.project_id
        )
        response = await self.create_request(
            "payments",
            sign,
            project_id=self.project_id,
            trans_id=trans_id,
            offset=offset,
            payout_id=payout_id,
        )
        return ResponsePaymentGetting(**response)
