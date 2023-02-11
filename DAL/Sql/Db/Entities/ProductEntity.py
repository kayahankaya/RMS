import datetime

class ProductEntity:

    def __init__(self):
        self.product_id = 0
        self.product_name = ''
        self.product_price = 0
        self.product_category = ''
        self.created_at = datetime.date(2002,6,12)
        self.updated_at = datetime.date(2002,6,12)