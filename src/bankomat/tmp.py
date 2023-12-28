def get_client_pin() -> str:
	max_tries = 3

	while max_tries>0:
		client_pin = input('Enter pin')
		if client_pin=='0001':
			return client_pin
		max_tries-=1

	return ''


print( get_client_pin() )