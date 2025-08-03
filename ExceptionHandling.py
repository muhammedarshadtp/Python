
def withdraw_money(balance):
    try:
        amount= int(input("enter the withdraw amount:"))

        if  amount > balance:
            raise ValueError("Insufficient balance!")
        if amount <=0:
            raise ValueError("Enter a positive amount!")
        balance -= amount
        print(f"✅ Withdrawal successful! New balance: ₹{balance}")

    except Exception as e:
        print("wrong:",e)
    except Exception :
        print("⚠️ Something went wrong. Please try again.")
    finally:
        print("Transaction Completed")    



withdraw_money(5000)
