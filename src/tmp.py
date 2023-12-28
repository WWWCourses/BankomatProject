from enum import Enum

class MenuOptions(Enum):
    WITHDRAW_MONEY = (1, "Withdraw Money")
    DEPOSIT_MONEY = (2, "Deposit Money")
    SHOW_ACCOUNT_DETAILS = (3, "Show Account Details")

for opt in MenuOptions:
    print(opt.value)