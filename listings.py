#Domain model / Business Layer
class Listing:
    def __init__(self, id, author_id, title, desc, price, category):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.desc = desc
        self.price = price
        self.category = category
        self.status = False
    
    @property
    def get_status(self):
        return self.status
    
    def sold(self):
        self.status = True
        
    def cancel(self):
        self.status = False
        
    @property
    def get_price(self):
        return self.price
   
    def set_price(self, price):
        #check to see if price given is a valid float
        if not isinstance(price, float):
            raise ValueError("expected type float")
        else:
            self.price = price

    @property        
    def get_category(self):
        return self.category
    
    @property    
    def get_title(self):
        return self.title

    @property
    def get_desc(self):
        return self.desc

    @property
    def get_author(self):
        return self.author
    
    @property
    def get_id(self):
        return self.id