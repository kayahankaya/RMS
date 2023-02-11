import DAL.Sql.Db.DbManager as DbManager
from DAL.Sql.Db.Entities.BillEntity import BillEntity

class BillRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_bill_by_bill_id(self,bill_id):

        cur = self.dbcontext.cursor()
        cur.execute("select * from bills where bill_id=%s",(bill_id))
        row = cur.fetchone()

        temp_bill = BillEntity()

        temp_bill.bill_id = row[0]
        temp_bill.table_name = row[1]
        temp_bill.bill_status = row[2]
        temp_bill.created_at = row[3]
        temp_bill.updated_at = row[4]
        temp_bill.paidby_cash = row[5]
        temp_bill.paidby_cc = row[6]
        temp_bill.mustpay = row[7]

        return temp_bill
    
    def get_bill_by_table_name(self,table_name):

        cur = self.dbcontext.cursor()
        cur.execute("select * from bills where table_name=%s",(table_name))
        row = cur.fetchone()

        temp_bill = BillEntity()

        temp_bill.bill_id = row[0]
        temp_bill.table_name = row[1]
        temp_bill.bill_status = row[2]
        temp_bill.created_at = row[3]
        temp_bill.updated_at = row[4]
        temp_bill.paidby_cash = row[5]
        temp_bill.paidby_cc = row[6]
        temp_bill.mustpay = row[7]

        return temp_bill

    def get_bill_by_bill_status(self,bill_status):

        cur = self.dbcontext.cursor()
        cur.execute("select * from bills where bill_status=%s",(bill_status))
        row = cur.fetchone()

        temp_bill = BillEntity()

        temp_bill.bill_id = row[0]
        temp_bill.table_name = row[1]
        temp_bill.bill_status = row[2]
        temp_bill.created_at = row[3]
        temp_bill.updated_at = row[4]
        temp_bill.paidby_cash = row[5]
        temp_bill.paidby_cc = row[6]
        temp_bill.mustpay = row[7]

        return temp_bill

    def update_bill_mustpay_by_table_name(self,rounded_total_withtax,selectedtable):

        cur = self.dbcontext.cursor()   
        cur.execute("""
        UPDATE bills 
        SET bills.mustpay = %s 
        WHERE table_name = %s AND bill_status = 'Open'""", (rounded_total_withtax,selectedtable))
        self.dbcontext.commit()

    def get_paids_by_table_name(self,selectedtable):

        cur = self.dbcontext.cursor()   
        cur.execute("""
        SELECT paidby_cash, paidby_cc 
        FROM bills 
        WHERE table_name = %s AND bill_status = 'Open' 
        ORDER BY bill_id 
        DESC LIMIT 1""", (selectedtable))

        temp_bill = cur.fetchone()

        return temp_bill

    def get_bill_id_by_table_name(self,selectedtable):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        SELECT bill_id 
        FROM bills 
        WHERE bills.table_name = %s and bills.bill_status = 'Open'""", (selectedtable))
        temp_bill = cur.fetchone()

        return temp_bill

    def insert_table_name_to_bill(self,selectedtable):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        INSERT INTO bills (bills.table_name) 
        VALUES(%s)""", selectedtable)
        self.dbcontext.commit()


    def change_table_number(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE others 
        SET others.table_count = %s 
        WHERE other_id = 1""",  (var))
        self.dbcontext.commit()

    def update_change_by_paidcash_and_table_name(self,payby_cash,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE bills 
        SET bills.paidby_cash = bills.paidby_cash + %s 
        WHERE table_name = %s AND bill_status = 'Open'""", (payby_cash,var))
        self.dbcontext.commit()

    def update_change_by_paidcc_and_table_name(self,payby_cc,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE bills 
        SET bills.paidby_cc = bills.paidby_cc + %s 
        WHERE table_name = %s AND bill_status = 'Open'""", (payby_cc,var))
        self.dbcontext.commit()

    def get_paids_by_table_name(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        SELECT bills.paidby_cash, bills.paidby_cc 
        FROM bills 
        WHERE bills.table_name = %s and bills.bill_status = 'Open'""", (var))
        temp_paids = cur.fetchone()

        return temp_paids

    def get_mustpay_by_table_name(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        SELECT mustpay 
        FROM bills 
        WHERE bills.table_name = %s and bills.bill_status = 'Open'""", (var))
        mustpay_check = cur.fetchone()

        return mustpay_check

    def close_bill_by_table_name(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE bills 
        SET bills.bill_status = 'Close' 
        WHERE table_name = %s AND bill_status = 'Open'""",  (var))
        self.dbcontext.commit()

    def total_paid_by_by_tablename(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        SELECT (paidby_cash+paidby_cc) as total_paid
        FROM bills 
        WHERE table_name = %s AND bill_status = 'Open'""",  (var))
        total_paid = cur.fetchone()

        return total_paid

    def update_remain_check_by_tablename(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE bills 
        SET bills.remain_check = bills.mustpay - (bills.paidby_cc + bills.paidby_cash)
        WHERE table_name = %s AND bill_status = 'Open'""",  (var))
        self.dbcontext.commit()

    def select_remain_check_by_tablename(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        SELECT remain_check
        FROM bills 
        WHERE table_name = %s AND bill_status = 'Open'""",  (var))
        remaining_check = cur.fetchone()

        return remaining_check

    def insert_mustpay_by_order_id(self,var,bill_id):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE bills 
        SET bills.mustpay = bills.mustpay + %s
        WHERE bill_id = %s AND bill_status = 'Open'""",  (var, bill_id))
        self.dbcontext.commit()

    def decrease_mustpay_by_order_id(self,var,bill_id):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE bills 
        SET bills.mustpay = bills.mustpay - %s
        WHERE bill_id = %s AND bill_status = 'Open'""",  (var, bill_id))
        self.dbcontext.commit()

    def set_head_count(self,var, bill_id):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        UPDATE bills 
        SET bills.head_count = %s
        WHERE bill_id = %s AND bill_status = 'Open'""",  (var, bill_id))
        self.dbcontext.commit()

    def get_head_count(self,var):

        cur = self.dbcontext.cursor() 
        cur.execute("""
        SELECT head_count
        FROM bills 
        WHERE table_name = %s AND bill_status = 'Open'""",  (var))
        head_count = cur.fetchone()

        return head_count











            

        


