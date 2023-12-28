from bankomat.custom_types import AccountDict

class Account:
	def __init__(self, account:AccountDict) -> None:
		self.client_name = account['client_name']
		self.pin = account['pin']
		self.balance = account['balance']

	def __str__(self) -> str:
		return f"{self.__dict__}"

	def withdraw(self, amount):
		print('Withdraw')

	def depost(self, amount):
		print('Deposit')

	def get_balance(self):
		return self.balance
