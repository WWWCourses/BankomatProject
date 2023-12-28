from bankomat.account import Account
from bankomat.client import Client
from bankomat.db_mysql import DB

from typing import List, Optional

import logging

logger = logging.getLogger(__name__)

class Bankomat:
	def __init__(self) -> None:
		# connect to db:
		self.db = DB()

	def __str__(self):
		msg = f"Bankomat Object\n"
		return msg

	def block_account(self, account:Account) -> None:
		print(f"{account.client_name} account is blocked!")


	def get_client_account(self, client_name) -> Account:
		try:
			account = self.db.get_account_by_name(client_name)
			return account
		except Exception as err:
			logger.exception(err)
			raise Exception(f'Client {client_name} does not exist!')

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
		client_name = Client.enter_name()

		# get client's account details:
		try:
			self.client_account = self.get_client_account(client_name)
		except Exception as err:
			logger.exception(err)
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
		amount = Client.enter_money_value('Enter amount to withdraw', min_value=1, max_value=1_000)

		# withdraw if account balance is enough
		try:
			self.client_account.withdraw(amount)

			# update db
			self.db.update_account_balance(self.client_account)
		except Exception as err:
			logger.error(f'Error: {err}')


	def deposit(self):
		logger.debug(f'Deposit Money')

	def show_account_details(self):
		logger.debug('show_account_details')




