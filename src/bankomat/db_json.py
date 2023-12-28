from bankomat.account import Account
import json
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class DB:
	def __init__(self, accounts_file='./data/accounts.json') -> None:
		self.accounts_file =accounts_file

	def get_all_accounts(self) -> List[Account]:
		try:
			with open(self.accounts_file, 'r') as f:
				# get accounts data:
				accounts_dict = json.load(f)
				logger.debug(accounts_dict)

				# convert list of dict to list of Account Instances
				if accounts_dict:
					return [Account(acc_dict) for acc_dict in accounts_dict ]
				else:
					return []
		except Exception as err:
			logger.exception(f'Error: {err}')
			exit()

	def save_accounts(self, accounts:List[Account]):
		try:
			with open(self.accounts_file, 'w') as f:
				# convert list of Account Instances to list of dict:
				accounts_dict = [acc.to_dict() for acc in accounts]

				json.dump(accounts_dict,f,indent=4)
				print(f"Accounts data has been saved to {self.accounts_file}")
		except Exception as err:
			logger.exception(f'Error: {err}')
			exit()



if __name__ =="__main__":
	# print(f'!!!!!!CWD: {os.getcwd()}')

	db = DB()
	data = db.get_all_accounts()
	print(data)


