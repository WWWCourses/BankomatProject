from bankomat.db import DB
from bankomat.bankomat import Bankomat


LINE_WIDTH = 80
MENU_OPTIONS = [
	"Withdraw Money",
	"Deposit Money",
	"Show Account Details",
]
CURRENCY='$'

def show_client_menu() -> None:
	# print menu footer
	print('*'*LINE_WIDTH)
	# print menu options
	for idx,option in enumerate(MENU_OPTIONS):
		print(f'*  {f"{idx+1}. {option}":<{LINE_WIDTH-4}s}*')
	# print menu footer
	print('*'*LINE_WIDTH)



if __name__=="__main__":
	bankomat = Bankomat()

	if not bankomat.client_login():
		print('Client is not logged in!')
		exit()

	show_client_menu()

	client_choice = input('Enter your choice: ')








