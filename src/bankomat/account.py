from bankomat.custom_types import AccountDict
from decimal import Decimal

class Account:
	def __init__(self, account:AccountDict) -> None:
		self.id = account['id']
		self.client_name = account['client_name']
		self.pin = account['pin']
		self.balance = Decimal(account['balance'])

	def __str__(self) -> str:
		return f"{self.__dict__}"

	def to_dict(self) -> dict:
		return {
			'id': self.id,
			'client_name': self.client_name,
			'pin': self.pin,
			'balance': self.balance
		}

	def withdraw(self, amount):
		amount = Decimal(amount)
		if self.balance > amount:
			self.balance-=amount
		else:
			raise Exception(f'Current balance ({self.balance}) is less than amount ({amount})')


	def depost(self, amount):
		print('Deposit')

	def get_balance(self):
		return self.balance
