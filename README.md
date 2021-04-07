# API Money

This app manage to keep the money transactions on a user account. On the other hands the application could generate 
statistic of transactions in daily, weekely, monthly and yearly time. 


### Account

- create an account
- delete an account
- modify an account
- show an account

CRUD

Account:
* name
* description
* initial_balance

### Transaction 


- create a transaction
- delete a transaction
- modify a transaction
- show a transaction

Transaction:
* amount
* transaction_type
* account
* description


### Statistic
Generate statistics for accounts and aggregate transaction value

## To Start:

- git clone git@github.com:wesolyigor/drf_api_blog.git

- pipenv install

- move to config.api_money package file `.env-default` and change name to `.env`

- python manage.py runserver
