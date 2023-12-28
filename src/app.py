from bankomat.bankomat import Bankomat
from bankomat.constants import MENU_OPTIONS, LINE_WIDTH, CURRENCY

import logging
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s-%(name)s:%(levelname)s : %(message)s')

logger = logging.getLogger(__name__)


def show_client_menu() -> None:
	# print menu footer
	print('*'*LINE_WIDTH)
	# print menu options
	for idx,option in MENU_OPTIONS.values():
		print(f'*  {f"{idx}. {option}":<{LINE_WIDTH-4}s}*')
	# print menu footer
	print('*'*LINE_WIDTH)

def is_valid_option(value)-> bool:
	return 1<=value<=len(MENU_OPTIONS)

def get_client_choice()->int:
	while True:
		try:
			client_choice = int(input('Enter your choice: '))
			if is_valid_option(client_choice):
				break
		except KeyboardInterrupt:
			print("\nKeyboardInterrupt detected. Bye!")
			exit()
		except:
			print(f'Enter a number [{1}..{len(MENU_OPTIONS)}] ')


	return client_choice


if __name__=="__main__":
	bankomat = Bankomat()

	# login
	if not bankomat.client_login():
		print('Client is not logged in!')
		exit()

	# show menu
	show_client_menu()

	# get valid user choice
	client_choice = get_client_choice()
	logger.debug(f'Client choice: {client_choice}')

	if client_choice==MENU_OPTIONS['WITHDRAW_MONEY'][0]:
		bankomat.withdraw()
	elif client_choice==MENU_OPTIONS['DEPOSIT_MONEY'][0]:
		bankomat.deposit()
	elif client_choice==MENU_OPTIONS['SHOW_ACCOUNT_DETAILS'][0]:
		bankomat.show_account_details()
	else:
		logger.debug(f'Not such option:{client_choice}')



