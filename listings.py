class Listing:
    def __init__(self, id, author_id, title, desc, price, category):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.desc = desc
        self.price = price
        self.category = category
        self.status = False
    
    def set_status(self, status):
        self.status = status
        
    def get_status(self):
        return self.status
    
    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        return self.price
    
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

if __name__ == "__main__":
    main()