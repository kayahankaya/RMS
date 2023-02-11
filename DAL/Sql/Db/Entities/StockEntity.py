import datetime

class StockEntity:

    def __init__(self):
        self.stock_id = 0
        self.stock_name = ''
        self.stock_weight = 0
        self.stock_unit = ''
        self.created_at = datetime.date(2002,6,12)
        self.updated_at = datetime.date(2002,6,12)