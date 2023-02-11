import datetime

class OrderEntity:

    def __init__(self):
        self.order_id = 0
        self.product_id = 0
        self.bill_id = 0
        self.created_at = datetime.date(2002,6,12)
        self.updated_at = datetime.date(2002,6,12)
        self.user_id = 0
