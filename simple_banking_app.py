balance=0.0
kyc_documents={}
def check_balance():
    print(f"Your Current Balance is {balance}")
    print("=========================")


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Please enter a valid amount")
        print("=========================")



def withdraw(amount):
    global balance
    if amount <= 0:
        print("Please enter a valid amount")
        print("=========================")
    elif amount >balance:
        print("Can't withdraw. Insufficient Amount.")
        print("=========================")
    else:
        balance -= amount

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
        print("=========================")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")
            print("=========================")





if __name__=="__main__":
    print("=========================")
    print("Welcome to ABS Banking App")
    print("=========================")
    while True:
        print("1. Check Your Balance")
        print("2. Deposit an Amount")
        print("3. Withdraw an Amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Exit")
        choice = input("Enter your choice (1-6):")

        if choice == '1':
            check_balance()


        elif choice == '2':
            amt = float(input("Enter your Amount to deposit: "))
            deposit(amt)
            print(f"Amount {amt} deposited successfully")
            print("=========================")

        elif choice == '3':
            amt = float(input("Enter your Amount to withdraw: "))
            withdraw(amt)
            print(f"Amount {amt} withdrew successfully")
            print("=========================")

        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs={}
            n_documents=int(input("Enter the no. of Document(s) you want to add: "))
            for i in range (n_documents):
                key= input("Enter the document type ")
                value= input("Enter the document number ")
                kyc_docs[key]=value
            update_kyc(kyc_docs)
            print(f"KYC Updated!!")
            print("=========================")

        elif choice == '6':
            print("Quiting application, Have a good day")
            print("=========================")
            break
        else:
            print("Please enter a valid choice")
            print("=========================")
    print()

    print("Thank you for using our application")