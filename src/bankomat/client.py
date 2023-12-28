class Client:
	@staticmethod
	def enter_pin()->str:
		""" Enter valid pin: 4 digits"""
		min_pin = '0000'
		max_pin = '9999'

		while True:
			pin = input(f'Enter your pin [{min_pin}-{max_pin}]: ')
			try:
				int(pin)
			except:
				print(f'PIN must be 4 digits!')
				continue

			#  if 0<1<9999
			if int(min_pin) < int(pin) < int(max_pin):
				return pin
			else:
				print(f'PIN must be in range: [{min_pin}-{max_pin}]')
	@staticmethod
	def enter_name() -> str:
		client_name = input('Enter your name: ')
		return client_name

	@staticmethod
	def enter_money_value(
			prompt:str,
			min_value:float,
			max_value:float
		)->float:

		range_info = f"[Min: {min_value}, Max: {max_value}]"

		while True:
			try:
				user_input = float(input(f'Enter amount {range_info}: '))
				# validate range
				if user_input < min_value or user_input > max_value:
					raise ValueError(f"Input must be in range {range_info}")

				return user_input
			except ValueError as e:
				print(f"{e}. Please try again.")
			except KeyboardInterrupt:
				print("\nKeyboardInterrupt detected. Exiting.")
				raise SystemExit