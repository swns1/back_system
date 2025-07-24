from savingsacoount import SavingsAcount

user1 = SavingsAcount("001", "User1")
is_on = True

while is_on:
    user1.dashboard()
    choice = input("Choose an action: ")

    if choice == "1":
        withdraw_money = int(input("How much money do you want to withdraw: "))
        user1.withdraw(withdraw_money)
    elif choice == "2":
        deposit_money = int(input("How much money do you want to deposit: "))
        user1.deposit(deposit_money)
        user1.apply_interest()
    elif choice == "3":
        user1.display_balance()
    else:
        print("Invalid Input")