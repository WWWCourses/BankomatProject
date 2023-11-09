import json
import os

class DB:
	def __init__(self) -> None:
		self.accounts_file = '../data/accounts.json'

	def get_all_accounts(self):
		try:
			with open(self.accounts_file, 'r') as f:
				data = json.load(f)
				return data
		except Exception as err:
			print(f'ERROR: {err}')
			exit()

	def save_accounts(self, accounts):
		try:
			with open(self.accounts_file, 'w') as f:
				json.dump(accounts,f)
				return data
		except Exception as err:
			print(f'ERROR: {err}')
			exit()




if __name__ =="__main__":
	# print(f'!!!!!!CWD: {os.getcwd()}')

	db = DB()
	data = db.get_all_accounts()
	print(data)


