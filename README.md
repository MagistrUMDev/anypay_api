
## A small API wrapper for AnyPay bank system made for a project.

- Creating a payment

- Getting payments list


## Installation

Install AnyPay API with pip

```bash
  pip install anypay_api
  cd my-project
```
    
## Environment Variables

To use the class, you need to provide API_KEY and API_ID

`API_KEY`

`API_ID`




## Usage/Examples

Creating a payment 
```python
from anypay_api import PayApi
api = PayApi(API_ID, API_KEY, PROJECT_ID)
async def create_payment():
    payment = await api.create_payment(pay_id, amount, currency, desc, method, method_currency)
    print(payment.payment_url)  - https://anypay.io/pay/de13d3493-4508-4c6a-90d4
```
Getting a payment 
```python
from anypay_api import PayApi
api = PayApi(API_ID, API_KEY, PROJECT_ID)
async def create_payment():
    payments = await api.get_payments(payout_id)
    print(payments.total)  - 2
```


## Feedback

I would be very pleased for a star ⭐️