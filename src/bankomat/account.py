from bankomat.custom_types import AccountDict

class Account:
	def __init__(self, account:AccountDict) -> None:
		self.client_name = account['client_name']
		self.pin = account['pin']
		self.balance = account['balance']

	def __str__(self) -> str:
		return f"{self.__dict__}"



class Accounts:
	def to_list_of_dict(self):
		pass

	def from_list_of_dict(self,accounts_dict):
		return  [Account(d) for d in accounts_dict]





