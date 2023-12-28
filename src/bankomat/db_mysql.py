from bankomat.account import Account
import mysql.connector
from typing import List
import logging

logger = logging.getLogger(__name__)

class DB:
	def __init__(self,
				 host='localhost',
				 user='test',
				 password='test1234',
				 database='bankomatdb'):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

	def create_accounts_table(self):
		pass


	def get_connection(self):
		return mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
		)

	def get_account_by_name(self, client_name: str) -> Account:
		try:
			connection = self.get_connection()
			cursor = connection.cursor(dictionary=True)

			query = f"SELECT * FROM accounts WHERE client_name = '{client_name}' LIMIT 1;"
			cursor.execute(query)
			account_data = cursor.fetchone()
			logger.debug(f'account_data: {account_data}')

			cursor.close()
			connection.close()

			if account_data:
				return Account(account_data)
			else:
				raise Exception(f'Account for client {client_name} not found in the database.')
		except Exception as err:
			logger.exception(f'Error: {err}')
			exit()

	def get_all_accounts(self) -> List[Account]:
		try:
			connection = self.get_connection()
			cursor = connection.cursor(dictionary=True)

			cursor.execute("SELECT * FROM accounts")
			accounts_data = cursor.fetchall()
			logger.debug(f'accounts_data: {accounts_data}')

			cursor.close()
			connection.close()

			if accounts_data:
				accounts = [Account(acc_data) for acc_data in accounts_data]
				return accounts
			else:
				return []
		except Exception as err:
			logger.exception(f'Error: {err}')
			exit()

	def update_account_balance(self, account_data: Account) -> None:
		try:
			connection = self.get_connection()
			cursor = connection.cursor()

			query = f"UPDATE accounts SET balance = {account_data.balance} WHERE client_name = '{account_data.client_name}';"
			cursor.execute(query)
			logger.debug(f"Account {account_data.client_name} balance updated in the database.")

			connection.commit()
			cursor.close()
			connection.close()
		except Exception as err:
			logger.exception(f'Error: {err}')
			exit()

	def save_accounts(self, accounts: List[Account]):
		try:
			connection = self.get_connection()
			cursor = connection.cursor()

			connection.start_transaction()

			cursor.execute("TRUNCATE TABLE accounts")  # Clear existing data in the table

			for account in accounts:
				query = """INSERT INTO accounts
					(id, client_name, pin, balance)
					VALUES (%s, %s, %s, %s)"""
				values = (account.id, account.client_name, account.pin, account.balance)
				cursor.execute(query, values)

			connection.commit()

			cursor.close()
			connection.close()

			print("Accounts data has been saved to MySQL database")
		except Exception as err:
			logger.exception(f'Error: {err}')
			exit()


if __name__ == "__main__":
	db_mysql = DB()
	print(data_mysql)
