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
	data_mysql = db_mysql.get_all_accounts()
	print(data_mysql)
