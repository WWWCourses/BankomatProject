import json
from typing import List
from bankomat.account import Account

class DB:
	def __init__(self) -> None:
		self.accounts_file = '../data/accounts.json'

	def get_all_accounts(self) -> List[Account]:
		try:
			with open(self.accounts_file, 'r') as f:
				# get accounts data:
				accounts_dict = json.load(f)

				# convert list of dict to list of Account Instances
				if accounts_dict:
					return [Account(acc_dict) for acc_dict in accounts_dict ]
				else:
					return []
		except Exception as err:
			print(f'ERROR: {err}')
			exit()

	def save_accounts(self, accounts_obj:List[Account|None]):
		try:
			with open(self.accounts_file, 'w') as f:
				# convert list of Account Instances to list of dict:
				accounts_dict = [acc.__dict__ for acc in accounts_obj]

				json.dump(accounts_dict,f)
				print(f"Accounts data has been saved to {self.accounts_file}")
				return data
		except Exception as err:
			print(f'ERROR: {err}')
			exit()



if __name__ =="__main__":
	# print(f'!!!!!!CWD: {os.getcwd()}')

	db = DB()
	data = db.get_all_accounts()
	print(data)


