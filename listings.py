class Listing:
    def __init__(self, id, author_id, title, desc, price, category):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.desc = desc
        self.price = price
        self.category = category
        self.status = False
    
    def cancel(self):
        self.status = False
    
    def sold(self):
        self.status = True
        
    def get_status(self):
        return self.status
    
    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        return self.price