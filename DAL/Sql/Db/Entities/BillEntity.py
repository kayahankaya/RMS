import datetime

class BillEntity:

    def __init__(self):
        self.bill_id = 0
        self.table_name = ''
        self.bill_status = ''
        self.created_at = datetime.date(2002,6,12)
        self.updated_at = datetime.date(2002,6,12)
        self.paidby_cash = 0
        self.paidby_cc = 0
        self.mustpay = 0