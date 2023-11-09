from bankomat.db import DB
from bankomat.account import Account, Accounts


if __name__=="__main__":
	# create DB connection:
	db = DB()

	# get data
	accounts_dict = db.get_all_accounts()
	# print(accounts_dict)
	accounts = Accounts.from_list_of_dict(accounts_dict)
	print(accounts)

	# change first account balance
	accounts[0].balance = 0
	for account in accounts:
		print(account)




