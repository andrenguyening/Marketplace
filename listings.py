#Domain model / Business Layer
class Listing:
    def __init__(self, id, author_id, title, desc, price, category):
        self._id = id
        self._author_id = author_id
        self._title = title
        self._desc = desc
        self._price = price
        self._category = category
        self._status = False
    
    @property
    def status(self):
        return self._status
        
    def sold_label(self):
        # business logic
        if self._status:
            return "Sold"   #show sold to user
        elif not self._status:
            return "Available"

    def is_sold(self):
        return self._status == 1
    
    @property
    def price(self):
        return self._price
   
    @price.setter
    def set_price(self, price):
        #check to see if price given is a valid float
        if not isinstance(price, float):
            raise ValueError("Expected type float")
        else:
            self._price = price

    @property
    def category(self):
        return self._category
    
    @category.setter
    def set_cat(self, cat):
        #check to see if price given is a valid string
        if not isinstance(cat, str):
            raise ValueError("Expected type str")
        else:
            self.category = cat
    
    @property
    def title(self):
        return self._title
    
    @property 
    def desc(self):
        return self._desc
    
    @desc.setter
    def set_desc(self, desc):
        #check to see if price given is a valid string
        if not isinstance(desc, str):
            raise ValueError("Expected type str")
        else:
            self._desc = desc

    @property
    def author(self):
        return self._author_id
    
    @property
    def id(self):
        return self._id