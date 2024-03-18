from listings import Listing
from account import Account
def main():
    # Creating a sample listing
    listing1 = Listing(1, 123, "Sample Listing", "This is a sample description.", 50.0)

    # Getting initial status and price
    print("Initial Status:", listing1.get_status())
    print("Initial Price:", listing1.get_price())

    # Changing status and price
    listing1.set_status(True)
    listing1.set_price(60.0)

    # Getting updated status and price
    print("Updated Status:", listing1.get_status())
    print("Updated Price:", listing1.get_price())

    # Creating a sample account
    account1 = Account(1, "123 Main St, Pittsburgh, PA", "admin", "admin")
    
if __name__ == "__main__":
    main()