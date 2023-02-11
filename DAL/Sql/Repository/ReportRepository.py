import DAL.Sql.Db.DbManager as DbManager

class ReportRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_soldproduct_report(self,time1,time2,date1,date2):

        temp_list = []

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT orders.product_id, COUNT(orders.product_id) AS product_count, products.product_name, products.product_price 
        FROM orders 
        JOIN products ON orders.product_id = products.product_id 
        JOIN bills ON orders.bill_id = bills.bill_id AND bills.bill_status = 'Close' AND DATE(orders.created_at) BETWEEN DATE(%s) AND DATE(%s) AND TIME(orders.created_at) BETWEEN TIME(%s) AND TIME(%s) 
        GROUP BY orders.product_id 
        ORDER BY (COUNT(orders.product_id) * products.product_price) DESC""", (date1,date2,time1,time2))
        closed_orders = cur.fetchall()

        for i in closed_orders:
            product_count = i[1]
            product_name = i[2]
            product_price = float((i[3]).replace(',', '.'))
            product_total = product_price * product_count
            temp_list.append((product_name,product_count,product_total))
        
        return temp_list

    def get_soldtables_report(self,time1,time2,date1,date2):
        
        temp_list = []

        cur = self.dbcontext.cursor()
        cur.execute("""
        SELECT LPAD(bills.table_name,2,0), COUNT(bills.bill_id) as bill_count, FORMAT(SUM(paidby_cc+paidby_cash),2) 
        FROM bills 
        WHERE bills.bill_status = 'Close' AND DATE(bills.created_at) BETWEEN DATE(%s) AND DATE(%s) AND TIME(bills.created_at) BETWEEN TIME(%s) AND TIME(%s) 
        GROUP BY bills.table_name 
        ORDER BY SUM(paidby_cc + paidby_cash) DESC""", (date1,date2,time1,time2))

        closed_orders = cur.fetchall()

        for i in closed_orders:
            table_name = i[0]
            count = i[1]
            mustpaid = i[2]
            temp_list.append(('Table '+str(table_name),count,mustpaid))
        
        return temp_list

    def get_solduser_report(self,time1,time2,date1,date2):
        
        temp_list = []

        cur = self.dbcontext.cursor()
        cur.execute('''
        SELECT user_id, COUNT(DISTINCT bills.bill_id) AS bill_count, SUM(paidby_cc+paidby_cash) AS total_paid 
        FROM bills INNER JOIN (SELECT DISTINCT bill_id, user_id FROM orders) as o  ON o.bill_id = bills.bill_id 
        WHERE bills.bill_status = 'Close' AND DATE(bills.created_at) BETWEEN DATE(%s) AND DATE(%s) AND TIME(bills.created_at) 
        BETWEEN TIME(%s) AND TIME(%s) 
        GROUP BY user_id 
        ORDER BY SUM(paidby_cc + paidby_cash) DESC''', (date1,date2,time1,time2))

        closed_orders = cur.fetchall()

        for i in closed_orders:
            user_name = i[0]
            count = i[1]
            mustpaid = i[2]
            temp_list.append((user_name,count,mustpaid))

        return temp_list

    def daily_graph_report(self,date1,date2):

        date_list = []
        total_list = []

        cur = self.dbcontext.cursor()
        cur.execute('''
        SELECT DATE(bills.created_at), SUM(paidby_cash + paidby_cc) 
        FROM bills 
        WHERE bills.bill_status = 'Close' AND DATE(bills.created_at) BETWEEN DATE(%s) AND DATE(%s) 
        GROUP BY DATE(bills.created_at) 
        ORDER BY DATE(bills.created_at) DESC''', (date1,date2))
        closed_orders = cur.fetchall()
        
        for i in closed_orders:
            created_at = i[0]
            total = i[1]
            date_list.append(str(created_at)[5:])
            total_list.append(int(total))
        
        return (date_list, total_list)

    def weekly_graph_report(self,date1,date2):

        date_list = []
        total_list = []

        cur = self.dbcontext.cursor()
        cur.execute('''
        SELECT WEEKOFYEAR(bills.created_at), SUM(paidby_cash + paidby_cc) 
        FROM bills 
        WHERE bills.bill_status = 'Close' AND DATE(bills.created_at) BETWEEN DATE(%s) AND DATE(%s) 
        GROUP BY WEEKOFYEAR(bills.created_at) 
        ORDER BY WEEKOFYEAR(bills.created_at) DESC''', (date1,date2))
        closed_orders = cur.fetchall()

        for i in closed_orders:
            created_at = i[0]
            total = i[1]
            date_list.append(str(created_at))
            total_list.append(int(total))
         
        return (date_list, total_list)

    def monthly_graph_report(self,date1,date2):

        date_list = []
        total_list = []

        cur = self.dbcontext.cursor()
        cur.execute('''
        SELECT MONTHNAME(bills.created_at), SUM(paidby_cash + paidby_cc) 
        FROM bills 
        WHERE bills.bill_status = 'Close' AND DATE(bills.created_at) BETWEEN DATE(%s) AND DATE(%s) 
        GROUP BY MONTHNAME(bills.created_at) 
        ORDER BY MONTHNAME(bills.created_at) DESC''', (date1,date2))
        closed_orders = cur.fetchall()

        for i in closed_orders:
            created_at = i[0]
            total = i[1]
            date_list.append(str(created_at))
            total_list.append(int(total))
            
        return (date_list, total_list)




