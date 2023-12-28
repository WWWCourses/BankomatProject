from typing import TypedDict, Type

# # Type for account dictionaries
class AccountDict(TypedDict):
	id:int
	client_name:str
	pin:str
	balance:float
