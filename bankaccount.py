class bankAccounts:
  
   BANK_NAME = "SBI"

   def __init__(self,name,mob,age,dob,balance):
       self.name = name
       self.mob = mob
       self.age = age
       self.dob = dob
       self.balance = balance

   def show_info(self):
       print(self.name,
            self.age,
            self.balance)
   def deposit(self, amounts):
        if amounts > 0:
            self.balance += amounts
        else:
            print("Invalid Amounts.")


   def withdraw(self,amounts):
        if amounts <= self.balance and amount > 0:
            self.balance -= amounts
        else:
             print("Invalid Amounts.")

accounts = []

accounts.append(bankAccounts("raj","111",32,567,100))
accounts.append(bankAccounts("rajesh","222",32,567,200))
accounts.append(bankAccounts("rajverr","333",32,567,300))
accounts.append(bankAccounts("raju","444",32,567,400))


def search_accounts(mob):
    for x in accounts:
        if x.mob == mob:
            return x 
    return False

user = search_accounts(444)
if user:
    print(user.name)
else:
    print("Account Not Found")


while True:
    print("""
    A: Create
    B: Check
    C: Withdraw
    D: Deposit
    E: Exit
    """)

    choice = input("Enter A option: ")
    mob = input("Enter mob: ")

    if choice == "A":
        name = input("Enter Name: ")
        age = input("Enter age: ")
        dob = input("Enter dob: ")

        user = search_accounts(mob)
        if user:
            print("A user with this mob exist.")
        else:
            accounts.append(
                bankAccounts(name,mob,age,dob,500)
            )

    if choice == "B":
        user = search_accounts(mob)
        if user:
            user.show_info()

    if choice == "C":
        amount = input("Enter amount: ")
        amount =int(amount)
        user = search_accounts(mob)
        if user:
            user.withdraw(amount)

    if choice == "D":
        amount = input("Enter amount: ")
        amount =int(amount)
        user = search_accounts(mob)
        if user:
            user.deposit(amount)
        
       

    if choice =="E":
        exit(0)

    if choice not in "ABCDE":
        print("Invaild")
    