from bankomat.account import Account
from bankomat.client import Client
from bankomat.db import DB

from typing import List

class Bankomat:
	def __init__(self) -> None:
		# get accounts data
		db = DB()
		self.accounts_list:List[Account] = db.get_all_accounts()
		self.client_account:Account|None = None

	def block_account(self, account:Account) -> None:
		print(f"{account.client_name} account is blocked!")

	def get_client_name(self) -> str:
		client_name = input('Enter your name: ')
		return client_name

	def get_client_account(self, client_name) -> Account|None:
		matched = [account for account in self.accounts_list if account.client_name==client_name ]
		if matched:
			return matched[0]
		else:
			return None

	def is_valid_client_pin(self) -> bool :
		max_tries = 3

		while max_tries>0:
			client_pin = Client.enter_pin()
			if client_pin==self.client_account.pin:
				return True

			max_tries-=1


		return False

	def client_login(self) -> bool:
		# ask client to enter name
		client_name = self.get_client_name()

		# get client's account details:
		self.client_account = self.get_client_account(client_name)

		if not self.client_account:
			print('No such client!')
			exit()

		# ask client to enter pin
		if self.is_valid_client_pin():
			return True
		else:
			# login not successful = > block account
			self.block_account(self.client_account)
			exit()

	def withdraw(self):
		# get value to withdraw
		value = Client.enter_money_value('Enter amount to withdraw', min_value=1, max_value=1_000)


